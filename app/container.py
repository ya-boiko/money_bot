"""Container."""

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    """Dependency injection container."""

    wiring_config = containers.WiringConfiguration(packages=["app"])
    config = providers.Configuration()

    # telegram
    dp = providers.Singleton(Dispatcher)
    bot = providers.Singleton(
        Bot,
        token=config.tg.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
