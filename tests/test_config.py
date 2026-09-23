from platform.config.loader import ConfigLoader
from platform.core.project import ProjectConfig


def main():
    loader = ConfigLoader("project/config.yaml")

    config = loader.load()

    project = ProjectConfig.from_dict(config)

    print("Configuration loaded successfully.")
    print(f"Project name: {project.name}")
    print(f"Model name: {project.model_name}")
    print(f"Training entrypoint: {project.training_entrypoint}")
    print(f"Validation entrypoint: {project.validation_entrypoint}")
    print(f"Deployment namespace: {project.deployment_namespace}")
    print(f"Deployment replicas: {project.deployment_replicas}")
    print(f"ECR repository: {project.ecr_repository}")


if __name__ == "__main__":
    main()