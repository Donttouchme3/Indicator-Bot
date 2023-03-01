from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from GetData import GetCategories


def GenerateCategories():
    Markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    Buttons = []
    Categories = GetCategories()
    for i in Categories:
        Button = Buttons.append(*i)
    Markup.add(*Buttons)
    return Markup
