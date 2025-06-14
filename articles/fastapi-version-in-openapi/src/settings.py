"""Settings module for the FastAPI application.

This module provides:
- AppSettings: A Pydantic settings class for the application configuration.
"""

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
)


class ProjectSettings(BaseSettings):
    """Loading values from the `project` table of the `pyproject.toml` file.

    If a specified key is not found in the `project` table in the `pyproject.toml` file,
    Pydantic will try to use it's other default setting sources to load the value from,
    and falling back to the default field value defined in this class.
    Docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/#pyprojecttoml
    """

    version: str = (
        "0.1.0"  # default value is identical to FastAPI's default version value
    )

    # all remaining code in this class is needed for Pydantic to load values from the `project` table in pyproject.toml
    # you could ignore it, except you want to understand the details
    model_config = SettingsConfigDict(
        extra="ignore",
        pyproject_toml_depth=1,  # pyproject.toml file is in the parent directory relative to the `src/` folder
        pyproject_toml_table_header=(
            "project",
        ),  # read keys from table `project` in `pyproject.toml`
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Read values from the `project` table in the `pyproject.toml` file as first priority.

        Customises priority for reading settings from sources.

        Args:
            settings_cls (type[BaseSettings]): The Settings class.
            init_settings (PydanticBaseSettingsSource): The `InitSettingsSource` instance.
            env_settings (PydanticBaseSettingsSource): The `EnvSettingsSource` instance.
            dotenv_settings (PydanticBaseSettingsSource): The `DotEnvSettingsSource` instance.
            file_secret_settings (PydanticBaseSettingsSource): The `SecretsSettingsSource` instance.

        Returns:
            tuple[PydanticBaseSettingsSource, ...]: A tuple with sources in their order for loading settings values.
        """
        setting_source_order = super().settings_customise_sources(
            settings_cls=settings_cls,
            init_settings=init_settings,
            env_settings=env_settings,
            dotenv_settings=dotenv_settings,
            file_secret_settings=file_secret_settings,
        )

        # add pyproject.toml file as first priority source when loading the settings
        return (PyprojectTomlConfigSettingsSource(settings_cls), *setting_source_order)


class AppSettings(BaseSettings):
    """Settings for the application."""

    environment: str = "DEV"
    project: ProjectSettings = ProjectSettings()
