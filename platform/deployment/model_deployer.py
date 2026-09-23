from typing import Any, Callable

from platform.core.project import ProjectConfig
from platform.core.result import Result
from platform.interfaces.deployer import Deployer


class ModelDeployer(Deployer):
    """
    Generic implementation of the Deployer interface.
    """

    def __init__(
        self,
        deploy_function: Callable[[ProjectConfig, Any], Any],
    ):
        self.deploy_function = deploy_function

    def deploy(
        self,
        project: ProjectConfig,
        model,
    ) -> Result:
        try:
            deployment_result = self.deploy_function(
                project,
                model,
            )

            return Result.ok(
                message="Deployment completed.",
                data=deployment_result,
            )

        except Exception as exc:
            return Result.failure(
                message=f"Deployment failed: {exc}",
            )