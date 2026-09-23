from abc import ABC, abstractmethod

from platform.core.project import ProjectConfig
from platform.core.result import Result


class Deployer(ABC):
    """
    Interface for model deployment implementations.
    """

    @abstractmethod
    def deploy(
        self,
        project: ProjectConfig,
        model
    ) -> Result:
        """
        Deploy a model for a project.
        """
        raise NotImplementedError