from aiogram import Dispatcher, types
from tg_parser import get_channel_post

dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    if message.text.startswith('/parse'):
        try:
            # Предполагаем, что после /parse идет @username канала
            channel = message.text.split()[1]
            posts = await get_channel_post(channel, limit=1)
            
            if posts:
                post = posts[0]
                response = f"Последний пост из {channel}:\n\n{post['text']}\n\nДата: {post['date']}"
                await message.reply(response)
            else:
                await message.reply("Не удалось получить посты")
                
        except IndexError:
            await message.reply("Укажите канал после команды, например: /parse @durov")