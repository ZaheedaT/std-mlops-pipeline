from pathlib import Path

from platform.config.entrypoint import EntrypointLoader
from platform.config.loader import ConfigLoader
from platform.core.project import ProjectConfig

from platform.deployment.model_deployer import ModelDeployer
from platform.monitoring.model_monitor import ModelMonitor
from platform.pipeline.pipeline import MLOpsPipeline
from platform.registry.model_registry import ModelRegistry
from platform.training.model_trainer import ModelTrainer
from platform.validation.model_validator import ModelValidator


def load_project_config() -> ProjectConfig:
    """
    Load the project configuration.
    """

    config_path = Path("project/config.yaml")

    loader = ConfigLoader(str(config_path))
    config = loader.load()

    return ProjectConfig.from_dict(config)


def create_pipeline(project: ProjectConfig) -> MLOpsPipeline:
    """
    Create the MLOps pipeline using the project's
    configured concrete implementations.
    """

    if not project.monitoring_entrypoint:
        raise ValueError(
            "Monitoring entrypoint is not configured."
        )

    if not project.registry_entrypoint:
        raise ValueError(
            "Registry entrypoint is not configured."
        )

    if not project.deployment_entrypoint:
        raise ValueError(
            "Deployment entrypoint is not configured."
        )

    monitor_function = EntrypointLoader.load(
        project.monitoring_entrypoint
    )

    registry_function = EntrypointLoader.load(
        project.registry_entrypoint
    )

    deployment_function = EntrypointLoader.load(
        project.deployment_entrypoint
    )

    monitor = ModelMonitor(
        check_function=monitor_function,
    )

    trainer = ModelTrainer()

    validator = ModelValidator()

    registry = ModelRegistry(
        register_function=registry_function,
    )

    deployer = ModelDeployer(
        deploy_function=deployment_function,
    )

    return MLOpsPipeline(
        monitor=monitor,
        trainer=trainer,
        validator=validator,
        registry=registry,
        deployer=deployer,
    )


def run() -> None:
    """
    Load the project and execute the MLOps pipeline.
    """

    project = load_project_config()

    pipeline = create_pipeline(project)

    result = pipeline.run(project)

    print(result.message)


if __name__ == "__main__":
    run()