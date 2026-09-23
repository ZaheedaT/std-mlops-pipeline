from typing import Any, Callable

from platform.core.project import ProjectConfig
from platform.core.result import Result
from platform.interfaces.registry import Registry


class ModelRegistry(Registry):
    """
    Concrete implementation of the Registry interface.
    """

    def __init__(
        self,
        register_function: Callable[[ProjectConfig, Any], Any],
    ):
        self.register_function = register_function

    def register(
        self,
        project: ProjectConfig,
        model,
    ) -> Result:
        try:
            registry_result = self.register_function(
                project,
                model,
            )

            return Result.ok(
                message="Model registration completed.",
                data=registry_result,
            )

        except Exception as exc:
            return Result.failure(
                message=f"Model registration failed: {exc}",
            )