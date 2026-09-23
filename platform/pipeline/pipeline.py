from platform.core.project import ProjectConfig
from platform.core.result import PipelineResult

from platform.interfaces.trainer import Trainer
from platform.interfaces.validator import Validator
from platform.interfaces.monitor import Monitor
from platform.interfaces.registry import Registry
from platform.interfaces.deployer import Deployer


class MLOpsPipeline:
    """
    Orchestrates the MLOps lifecycle.
    """

    def __init__(
        self,
        monitor: Monitor,
        trainer: Trainer,
        validator: Validator,
        registry: Registry,
        deployer: Deployer,
    ):
        self.monitor = monitor
        self.trainer = trainer
        self.validator = validator
        self.registry = registry
        self.deployer = deployer

    def run(self, project: ProjectConfig) -> PipelineResult:

        monitor_result = self.monitor.check(project)

        if not monitor_result.success:
            return PipelineResult(
                success=False,
                retrained=False,
                message=monitor_result.message,
            )

        if not monitor_result.data:
            return PipelineResult(
                success=True,
                retrained=False,
                message="No retraining required.",
            )

        training_result = self.trainer.train(project)

        if not training_result.success:
            return PipelineResult(
                success=False,
                retrained=True,
                message=training_result.message,
            )

        model = training_result.data

        validation_result = self.validator.validate(
            project,
            model,
        )

        if not validation_result.success:
            return PipelineResult(
                success=False,
                retrained=True,
                message=validation_result.message,
            )

        registry_result = self.registry.register(
            project,
            model,
        )

        if not registry_result.success:
            return PipelineResult(
                success=False,
                retrained=True,
                message=registry_result.message,
            )

        registered_model = registry_result.data

        deployment_result = self.deployer.deploy(
            project,
            registered_model,
        )

        if not deployment_result.success:
            return PipelineResult(
                success=False,
                retrained=True,
                model_id=registered_model,
                deployment_successful=False,
                message=deployment_result.message,
            )

        return PipelineResult(
            success=True,
            retrained=True,
            model_id=registered_model,
            deployment_successful=True,
            message="Pipeline completed successfully.",
        )