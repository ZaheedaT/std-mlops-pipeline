from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Result:
    """ Standard return type for MLOps pipeline operations.
    Encapsulates whether an operation succeeded,
    a message describing the outcome,
    and optional data produced by the operation.
    """

    success: bool
    message: str
    data: Optional[Any] = None

    @classmethod
    def ok(
        cls,
        message: str,
        data: Optional[Any] = None,
    ) -> "Result":
        return cls(
            success=True,
            message=message,
            data=data,
        )

    @classmethod
    def failure(
        cls,
        message: str,
        data: Optional[Any] = None,
    ) -> "Result":
        return cls(
            success=False,
            message=message,
            data=data,
        )


@dataclass
class PipelineResult:
    """
    Represents the final result of an MLOps pipeline execution.
    """

    success: bool
    retrained: bool
    message: str
    model_id: Optional[str] = None
    deployment_successful: bool = False