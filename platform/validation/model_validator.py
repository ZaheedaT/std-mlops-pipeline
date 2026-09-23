from typing import Any, Callable

from platform.config.entrypoint import EntrypointLoader
from platform.core.project import ProjectConfig
from platform.core.result import Result
from platform.interfaces.validator import Validator


class ModelValidator(Validator):
    """
    Concrete implementation of the Validator interface.
    """

    def __init__(
        self,
        validate_function: Callable[[ProjectConfig, Any], Any] | None = None,
    ):
        self.validate_function = validate_function

    def validate(
        self,
        project: ProjectConfig,
        model,
    ) -> Result:
        try:
            if self.validate_function is None:
                if not project.validation_entrypoint:
                    return Result.failure(
                        message="No validation entrypoint configured."
                    )

                self.validate_function = EntrypointLoader.load(
                    project.validation_entrypoint
                )

            validation_result = self.validate_function(
                project,
                model,
            )

            return Result.ok(
                message="Validation completed.",
                data=validation_result,
            )

        except Exception as exc:
            return Result.failure(
                message=f"Validation failed: {exc}",
            )