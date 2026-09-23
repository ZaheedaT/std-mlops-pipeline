from abc import ABC, abstractmethod

from platform.core.project import ProjectConfig
from platform.core.result import Result


class Registry(ABC):
    """
    Interface for model registry implementations.
    """

    @abstractmethod
    def register(
        self,
        project: ProjectConfig,
        model
    ) -> Result:
        """
        Register a model for a app.
        """
        raise NotImplementedError