from abc import ABC, abstractmethod

from platform.core.project import ProjectConfig
from platform.core.result import Result


class Validator(ABC):
    """
    Interface for model validation implementations.
    """

    @abstractmethod
    def validate(
        self,
        project: ProjectConfig,
        model
    ) -> Result:
        """
        Validate a trained model for a app.
        """
        raise NotImplementedError