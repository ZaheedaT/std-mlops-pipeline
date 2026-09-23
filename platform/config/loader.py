import os
import re
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


class ConfigLoader:
    """
    Loads app configuration from a YAML file
    and resolves environment variables.
    """

    ENV_PATTERN = re.compile(r"\$\{([^}]+)\}")

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

        env_file = self.config_path.parent.parent / ".env"
        load_dotenv(env_file)

    def load(self) -> dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with self.config_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            content = file.read()

        content = self._resolve_environment_variables(content)

        return yaml.safe_load(content) or {}

    def _resolve_environment_variables(
        self,
        content: str,
    ) -> str:

        def replace(match):
            variable_name = match.group(1)

            value = os.getenv(variable_name)

            if value is None:
                raise ValueError(
                    f"Required environment variable "
                    f"'{variable_name}' is not set."
                )

            return value

        return self.ENV_PATTERN.sub(replace, content)