from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.admin_orm.base_manager import BaseAdminManager
from app.admin.keyboards.keyboards import InlineKeyboardManager
from models.models import Info


class DeleteState(StatesGroup):
    """Класс состояний для удаления."""

    select = State()
    confirm = State()


class DeleteManager(BaseAdminManager):
    """
    Менеджер для удаления объектов из базы данных.

    Этот класс предоставляет функциональность для получения списка объектов,
    выбора объекта для удаления, подтверждения удаления и выполнения операции удаления.
    Он взаимодействует с базой данных через CRUD-операции и управляет состоянием
    пользователя в процессе удаления.

    Methods:
        get_all_model_names(session: AsyncSession) -> list[str]:
            Получает список названий объектов из таблицы БД.

        select_obj_to_delete(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
            Запрашивает у пользователя, какой объект он хочет удалить, и отображает список объектов.

        confirm_delete(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
            Подтверждает выбор объекта для удаления и запрашивает подтверждение от пользователя.

        delete_obj(callback: CallbackQuery, state: FSMContext, session: AsyncSession) -> None:
            Удаляет выбранный объект из базы данных и сбрасывает состояние.
    """

    async def get_all_model_names(self, session: AsyncSession) -> list[str]:
        """Получить список названий объектов из таблицы БД."""
        models = await self.model_crud.get_multi(session)
        return [model.name for model in models]

    async def select_obj_to_delete(
        self,
        callback: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
    ) -> None:
        obj_list_by_name = await self.get_all_model_names(session)
        await callback.message.edit_text(
            "Какой объект удалить?",
            reply_markup=self.keyboard.add_extra_buttons(obj_list_by_name),
        )
        await state.set_state(DeleteState.select)

    async def confirm_delete(
        self,
        callback: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
    ) -> None:
        self.obj_to_delete = await self.model_crud.get_by_string(
            callback.data, session
        )
        obj_data = (
            self.obj_to_delete.question
            if isinstance(self.obj_to_delete, Info)
            else self.obj_to_delete.name
        )
        await callback.message.edit_text(
            f"Вы уверены, что хотите удалить этот вопрос?\n\n {obj_data}",
            reply_markup=InlineKeyboardManager.get_inline_confirmation(
                cancel_option=self.keyboard.previous_menu
            ),
        ),
        await state.set_state(DeleteState.confirm)

    async def delete_obj(
        self,
        callback: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
    ) -> None:
        """Удалить объект из БД."""
        try:
            await self.model_crud.remove(self.obj_to_delete, session)
            await callback.message.edit_text(
                "Данные удалены!",
                reply_markup=InlineKeyboardManager.get_back_button(
                    self.keyboard.previous_menu
                ),
            )
            await state.clear()
        except Exception as e:
            await callback.message.answer(f"Произошла ошибка: {e}")
