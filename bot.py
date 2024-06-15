import discord
from bot_logic import handle_conversation

intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('здравствуйте') or message.content.startswith('привет'):
        await message.channel.send('Привет! Пришли мне тип мусора и я расскажу тебе сколько он разлагается.')
   
    else:
        await handle_conversation(client, message)

client.run('') 
