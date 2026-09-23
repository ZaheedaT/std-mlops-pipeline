class PipelineException(Exception):
    """
    Base exception for MLOps pipeline errors.
    """
    pass


class TrainingException(PipelineException):
    """Raised when model training fails."""
    pass


class ValidationException(PipelineException):
    """Raised when model validation fails."""
    pass


class RegistrationException(PipelineException):
    """Raised when model registration fails."""
    pass


class DeploymentException(PipelineException):
    """Raised when model deployment fails."""
    pass


class MonitoringException(PipelineException):
    """Raised when model monitoring fails."""
    pass