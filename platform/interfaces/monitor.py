from abc import ABC, abstractmethod

from platform.core.project import ProjectConfig
from platform.core.result import Result


class Monitor(ABC):
    """
    Interface for model monitoring implementations.
    """

    @abstractmethod
    def check(self, project: ProjectConfig) -> Result:
        """
        Check whether retraining is required for a app.
        """
        raise NotImplementedError