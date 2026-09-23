from typing import Any, Callable

from platform.core.project import ProjectConfig
from platform.core.result import Result
from platform.interfaces.monitor import Monitor


class ModelMonitor(Monitor):
    """
    Concrete implementation of the Monitor interface.
    """

    def __init__(
        self,
        check_function: Callable[[ProjectConfig], bool],
    ):
        self.check_function = check_function

    def check(self, project: ProjectConfig) -> Result:
        try:
            retraining_required = self.check_function(project)

            return Result.ok(
                message="Monitoring check completed.",
                data=retraining_required,
            )

        except Exception as exc:
            return Result.failure(
                message=f"Monitoring check failed: {exc}",
            )