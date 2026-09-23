from platform.core.project import ProjectConfig


def check(project: ProjectConfig) -> bool:
    """
    Project-specific monitoring check.

    Return True when retraining is required.
    Return False when the current model can remain deployed.
    """

    return False