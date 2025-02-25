from telethon import TelegramClient
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

# Telethon
api_id = 12345678
api_hash = 'aa11bb22cc33dd44'
phone = '+79999999999'
client = TelegramClient('session_name', api_id, api_hash)

# Aiogram
bot = Bot(token="123456789:AaBB123AAbbCC123_Ddd4dD4", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def get_channel_posts(channel_username: str, limit: int = 1):
    try:
        await client.start(phone)
        channel = await client.get_entity(channel_username)
        posts = []
        async for message in client.iter_messages(channel, limit=limit):
            post_data = {
                'message_id': message.id,
                'date': message.date,
                'text': message.text or message.caption or '',
                'has_media': False
            }
            if message.photo:
                post_data['has_media'] = True
                post_data['media_type'] = 'photo'
            posts.append(post_data)
        return posts
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return None
	# --- закрывает сессии из всех других устройств
    '''finally:
        await client.disconnect()'''

@dp.message()
async def handle_message(message: types.Message):
    if message.text.startswith('/parse'):
        try:
            channel = message.text.split()[1]
            if not channel.startswith('@'):
                await message.reply("Укажите юзернейм с @, например: /parse @durov")
                return
            posts = await get_channel_posts(channel, limit=1)
            if posts:
                post = posts[0]
                response = f"Последний пост из {channel}:\n\n{post['text']}\n\nДата: {post['date']}"
                await message.reply(response)
            else:
                await message.reply("Не удалось получить посты")
        except IndexError:
            await message.reply("Укажите канал после команды, например: /parse @durov")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())