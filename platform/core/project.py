from dataclasses import dataclass
from typing import Optional


@dataclass
class ProjectConfig:
    name: str
    model_name: str

    training_entrypoint: str
    validation_entrypoint: Optional[str] = None

    monitoring_workspace: Optional[str] = None
    monitoring_project: Optional[str] = None
    monitoring_entrypoint: Optional[str] = None

    registry_entrypoint: Optional[str] = None

    deployment_namespace: str = "default"
    deployment_replicas: int = 1
    deployment_entrypoint: Optional[str] = None

    ecr_repository: Optional[str] = None

    @classmethod
    def from_dict(cls, config: dict) -> "ProjectConfig":
        project = config["app"]
        training = config["training"]
        validation = config.get("validation", {})
        monitoring = config.get("monitoring", {})
        registry = config.get("registry", {})
        deployment = config.get("deployment", {})

        return cls(
            name=project["name"],
            model_name=project["model_name"],
            training_entrypoint=training["entrypoint"],
            validation_entrypoint=validation.get("entrypoint"),
            monitoring_workspace=monitoring.get("workspace"),
            monitoring_project=monitoring.get("app"),
            monitoring_entrypoint=monitoring.get("entrypoint"),
            registry_entrypoint=registry.get("entrypoint"),
            deployment_namespace=deployment.get(
                "namespace",
                "default",
            ),
            deployment_replicas=deployment.get(
                "replicas",
                1,
            ),
            deployment_entrypoint=deployment.get(
                "entrypoint",
            ),
            ecr_repository=deployment.get(
                "ecr_repository",
            ),
        )