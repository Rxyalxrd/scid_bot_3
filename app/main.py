import logging
import asyncio

from core.db import AsyncSessionLocal
from middlewares.middleware import DataBaseSession
from core.bot_setup import bot, dispatcher, check_token
from bot.handlers import router as message_router
from bot.callbacks import router as callback_router
from bot.fsm_context import router as fsm_context_router
from core.init_db import add_portfolio

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Логирование в консоль, при диплое убираем
        logging.FileHandler("bot.log", encoding='utf-8')  # Логирование в файл
    ]
)

logger = logging.getLogger(__name__)


async def main() -> None:
    """Запуск SCID бота."""

    try:
        check_token()
    except ValueError as e:
        logger.error(f"Ошибка проверки токена: {e}")
        return

    dispatcher.include_router(message_router)
    dispatcher.include_router(callback_router)
    dispatcher.include_router(fsm_context_router)

    try:
        logger.info("Запуск бота...")
        dispatcher.update.middleware(
            DataBaseSession(session_pool=AsyncSessionLocal)
        )
        await add_portfolio()
        await dispatcher.start_polling(bot)

    except Exception as e:
        logger.error(f"Критическая ошибка в работе бота: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем.")

    except Exception as e:
        logger.error(f"Произошла непредвиденная ошибка: {e}")
