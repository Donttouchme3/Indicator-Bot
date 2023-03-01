from aiogram import Dispatcher, executor, Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from random import randint
import os
from dotenv import load_dotenv

from Keyboards import GenerateCategories
from GetData import CheckCategory, GetArticleId, GetArticleData
load_dotenv()
BOT = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(BOT)


@dp.message_handler(commands=['start', 'help', 'about'])
async def StartBot(message:  Message):
    if message.text == '/start':
        await message.answer(f'Вы вошли в мир научных статьей. Бот создан не для коммерческих целей.', reply_markup=GenerateCategories())
    elif message.text == '/help':
        await message.answer('По вопросам обращаться к @shavkatov3.')
    elif message.text == '/about':
        await message.answer('Бот создан не для коммерческих целей. Здесь вы найдете интересные для себя статьи')

@dp.message_handler(content_types='text')
async def StartCategories(message: Message):
    if CheckCategory(message.text):
        try:
            ArticleFirstId, ArticleLastId = GetArticleId(CheckCategory(message.text)[0])
            RandomId = randint(int(*ArticleFirstId), int(*ArticleLastId))
            ChatId = message.chat.id
            Data = GetArticleData(RandomId)
            Title, Image, Content, Author = Data[0], Data[1], Data[2], Data[3]

            await BOT.send_photo(ChatId,  caption=f'{Title}\n\n\n'
                                                  f'{Content}\n\n'
                                                  f'{Author}',
                                 photo=Image)
        except:
            await message.answer('Данной категории не существует. Пожалуйста убедитесь что данные верны.')
    else:
        await message.answer('Данной категории не существует. Пожалуйста убедитесь что данные верны.')


if __name__ == '__main__':
    executor.start_polling(dp)

