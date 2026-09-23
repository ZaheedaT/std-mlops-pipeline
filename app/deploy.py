from typing import Any

from platform.core.project import ProjectConfig


def deploy(
    project: ProjectConfig,
    model: Any,
) -> Any:
    """
    Project-specific model deployment.
    """

    # Implement app deployment here.
    return model