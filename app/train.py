from typing import Any

from platform.core.project import ProjectConfig


def train(project: ProjectConfig) -> Any:
    """
    Project-specific model training entrypoint.

    Implement the app's training logic here.
    """

    raise NotImplementedError(
        f"Training implementation has not been defined "
        f"for app '{project.name}'."
    )