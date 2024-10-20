from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

# reply keyboard under input
startsMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Покажи свой функционал"),
            KeyboardButton(text="Закончить диалог"),
        ]
    ],
    input_field_placeholder="Выбери действие:"
)

# inline keyboard in message box
actionsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Плюсовать числа", callback_data='plus'),
            InlineKeyboardButton(text="Множить числа", callback_data='multiply'),
        ]
    ]
)