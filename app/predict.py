from typing import Any

from platform.core.project import ProjectConfig


def predict(
    project: ProjectConfig,
    model: Any,
    data: Any,
) -> Any:
    """
    Project-specific model prediction entrypoint.

    Implement the app's prediction logic here.
    """

    return model.predict(data)