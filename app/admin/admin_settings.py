import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_CHAT_IDS = os.getenv("TELEGRAM_CHAT_IDS").split(", ")
admin_list = [int(admin_id) for admin_id in TELEGRAM_CHAT_IDS]


def get_buttons(menu: dict[str, str]) -> list[str]:
    """Возвращает список кнопок для бота."""
    return [button for button in menu.values()]


# Первое сообщение бота после команды /start
GREETINGS = (
    "Здравствуйте!\n"
    "Я ваш виртуальный помощник.\n"
    "Воспользуйтесь экранной клавиатурой для выбора опции."
)


# Кнопки админа
ADMIN_BASE_OPTIONS = {
    "create": "Добавить",
    "update": "Изменить",
    "delete": "Удалить",
}
ADMIN_PORTFOLIO_OPTIONS = {
    "change_url": "Адрес ссылки на портфолио",
}
ADMIN_BASE_KEYBOARD = get_buttons(ADMIN_BASE_OPTIONS)
ADMIN_PORTFOLIO_KEYBOARD = get_buttons(ADMIN_PORTFOLIO_OPTIONS)
ADMIN_BASE_REPLY_OPTIONS = {
    "main_menu": "Главное меню",
    "callback_case": "Заявки на обратный звонок",
    "feedback": "Посмотреть отзывы",
}
ADMIN_BASE_BUTTONS = get_buttons(ADMIN_BASE_REPLY_OPTIONS)
ADMIN_UPDATE_OPTIONS = {
    "name": "Название",
    "content": "Содержание",
}
ADMIN_UPDATE_BUTTONS = get_buttons(ADMIN_UPDATE_OPTIONS)
ADMIN_CONTENT_OPTIONS = {
    "url": "Ссылка",
    "description": "Текст",
    "media": "Картинка",
}
ADMIN_CONTENT_BUTTONS = get_buttons(ADMIN_CONTENT_OPTIONS)
ADMIN_QUESTION_OPTIONS = {"question": "Вопрос", "answer": "Ответ"}
ADMIN_QUESTION_BUTTONS = get_buttons(ADMIN_QUESTION_OPTIONS)
ADMIN_SPECIAL_OPTIONS = {
    "manager_request": "Запросы на обратный звонок",
    "support_request": "Запросы на техподдержку",
    "feedbacks": "Отзывы",
}
ADMIN_SPECIAL_BUTTONS = get_buttons(ADMIN_SPECIAL_OPTIONS)
SUPERUSER_SPECIAL_OPTIONS = {
    "manager_request": "Запросы на обратный звонок",
    "support_request": "Запросы на техподдержку",
    "feedbacks": "Отзывы",
    "promotion": "Управление персоналом",
}
SUPERUSER_SPECIAL_BUTTONS = get_buttons(SUPERUSER_SPECIAL_OPTIONS)
SUPERUSER_PROMOTION_OPTIONS = {
    "manager_list": "Список менеджеров",
    "promote": "Добавить менеджера",
    "demote": "Убрать менеджера",
}
SUPERUSER_PROMOTION_BUTTONS = get_buttons(SUPERUSER_PROMOTION_OPTIONS)
# Кнопки экранной клавиатуры
BASE_BUTTONS = {
    "main_menu": "Главное меню",
    "call_manager": "Связаться с менеджером",
    "rate_us": "Оставить отзыв",
}
BASE_KEYBOARD_BUTTONS = get_buttons(BASE_BUTTONS)

# Главное меню - кнопки и текст
MAIN_MENU_TEXT = "Главное меню"
MAIN_MENU_OPTIONS = {
    "company_bio": "Информация о компании",
    "products": "Продукты и услуги",
    "support": "Техническая поддержка",
    "portfolio": "Портфолио",
    "admin_special": "Дополнительно",
}
MAIN_MENU_BUTTONS = get_buttons(MAIN_MENU_OPTIONS)

# Техподдержка - кнопки и текст
SUPPORT_MENU_TEXT = "Какой вид поддержки Вам нужен?"
SUPPORT_OPTIONS = {
    "general_questions": "Общие вопросы",
    "problems_with_products": "Проблемы с продуктами",
    "callback_request": "Запрос на обратный звонок",
}
SUPPROT_MENU_BUTTONS = get_buttons(SUPPORT_OPTIONS)


# Информация о компании - кнопки и текст
COMPANY_ABOUT = "Вот несколько вариантов информации о нашей компании. Что именно вас интересует?"


# Портфолио - кнопки и текст
PORTFOLIO_MENU_TEXT = "Ниже ссылка на наше портфолио и другие наши проекты"
PORTFOLIO_OTHER_PROJECTS_TEXT = "Еще примеры наших работ:"
PORTFOLIO_MENU_OPTIONS = {
    "portfolio_button": "Наше портфолио",
    "other_projects": "Посмотреть другие проекты",
}
PORTFOLIO_URL = "https://scid.ru/cases"
PORTFOLIO_BUTTONS = get_buttons(PORTFOLIO_MENU_OPTIONS)
PORTFOLIO_DEFAULT_DATA = {"name": "Портфолио", "url": "https://scid.ru/cases"}

# Продукты
PRODUCT_LIST_TEXT = (
    "Мы предлагаем следющие продукты и услуги. Что Вас интересует?"
)

# Константы проекта
DEFAULT_STR_LEN = 150
PHONE_NUMBER_LEN = 25
PHONE_NUMBER_REGEX = r"(\+\d{5,25}$|\d{5,25}$)"
USER_CALLBACK_PAGINATION = 5
FEEDBACK_PAGINATION = 5
DATETIME_FORMAT = '%d-%m-%Y %H:%M'