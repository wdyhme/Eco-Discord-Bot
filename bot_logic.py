import random
import asyncio


async def handle_conversation(client, message):
    
    command = message.content.lower()
    user_id = message.author.id  
    

    if command == 'пластик':
        await message.channel.send('Пластик разлагается более 100 лет')

    elif command == 'бумага':
        await message.channel.send('Бумага разлагается около 2 лет')   

    elif command == 'фольга':
        await message.channel.send('Фольга разлагается до 100 лет')

    elif command == 'картон':
        await message.channel.send('Картон разлагается до 1 года')

    elif command == 'стекло':
        await message.channel.send('Стекло разлагается более 1000 лет')

    elif command == 'аллюминий':
        await message.channel.send('Аллюминий разлагается около 500 лет')   


    elif command == 'батарейки':
        await message.channel.send('Батарейки разлагается до 100 лет')   

    elif command == 'пищевые отходы':
        await message.channel.send('Пищевые отходы разлагаются до 1 месяца')               