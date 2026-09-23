from typing import Any

from platform.core.project import ProjectConfig


def validate(
    project: ProjectConfig,
    model: Any,
) -> Any:
    """
    Project-specific model validation entrypoint.

    Implement the app's validation logic here.
    """

    raise NotImplementedError(
        f"Validation implementation has not been defined "
        f"for app '{project.name}'."
    )