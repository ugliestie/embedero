from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.i18n import gettext as _

def kb_start():
    inline_kb_list = [
        [InlineKeyboardButton(text=("tap me!"), switch_inline_query='')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)