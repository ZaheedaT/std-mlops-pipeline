from typing import Any

from platform.core.project import ProjectConfig


def register(
    project: ProjectConfig,
    model: Any,
) -> Any:
    """
    Project-specific model registration.
    """

    # Implement app model registration here.
    return model