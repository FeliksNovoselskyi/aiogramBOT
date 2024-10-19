from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

startsMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Покажи свой функционал"),
            KeyboardButton(text="Закончить диалог"),
        ]
    ],
    input_field_placeholder="Выбери действие:"
)