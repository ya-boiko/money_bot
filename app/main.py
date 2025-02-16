"""Main script."""

from .container import Container
from .settings import Settings


def main():
    """Creates the application."""
    container = Container()
    container.config.from_dict(Settings().model_dump())

    return build_app()


def build_app():
    """Builds the application."""

    ...
