from abc import ABC, abstractmethod

from platform.core.project import ProjectConfig
from platform.core.result import Result


class Trainer(ABC):
    """
    Interface for model training implementations.
    """

    @abstractmethod
    def train(self, project: ProjectConfig) -> Result:
        """
        Train a machine learning model for a project.
        """
        raise NotImplementedError