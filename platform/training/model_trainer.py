from typing import Any, Callable

from platform.config.entrypoint import EntrypointLoader
from platform.core.project import ProjectConfig
from platform.core.result import Result
from platform.interfaces.trainer import Trainer


class ModelTrainer(Trainer):
    """
    Concrete implementation of the Trainer interface.
    """

    def __init__(
        self,
        train_function: Callable[[ProjectConfig], Any] | None = None,
    ):
        self.train_function = train_function

    def train(self, project: ProjectConfig) -> Result:
        try:
            if self.train_function is None:
                self.train_function = EntrypointLoader.load(
                    project.training_entrypoint
                )

            model = self.train_function(project)

            return Result.ok(
                message="Training completed.",
                data=model,
            )

        except Exception as exc:
            return Result.failure(
                message=f"Training failed: {exc}",
            )