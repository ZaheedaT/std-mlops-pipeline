import importlib
from typing import Any, Callable


class EntrypointLoader:
    """
    Loads a Python callable from a configured entrypoint.

    Expected format:
        package.module:function
    """

    @staticmethod
    def load(entrypoint: str) -> Callable[..., Any]:
        if ":" not in entrypoint:
            raise ValueError(
                f"Invalid entrypoint '{entrypoint}'. "
                "Expected format 'module:function'."
            )

        module_name, function_name = entrypoint.split(":", 1)

        module = importlib.import_module(module_name)

        try:
            function = getattr(module, function_name)
        except AttributeError as exc:
            raise AttributeError(
                f"Function '{function_name}' not found "
                f"in module '{module_name}'."
            ) from exc

        if not callable(function):
            raise TypeError(
                f"Entrypoint '{entrypoint}' is not callable."
            )

        return function