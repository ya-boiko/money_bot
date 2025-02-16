"""Container."""

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    """Dependency injection container."""

    wiring_config = containers.WiringConfiguration(packages=["app"])
    config = providers.Configuration()
