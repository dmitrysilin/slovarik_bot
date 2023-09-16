from telebot import TeleBot, types

bot = TeleBot(token='6439597091:AAHOglQDPnmuaxDX-N_dTHfvv9lswcHmi34', parse_mode='html')

DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'тестирование': 'Тестирование это поиск и сравнение разницы между ожидаемым и фактическим поведением',
    'http': 'HTTP (HyperText Transfer Protocol) - это протокол передачи данных, используется для обмена информацией на веб-серверах и клиентах. Простыми словами, HTTP позволяет компьютеру говорить с другими компьютерами в интернете и получать информацию, которую вы хотите видеть на экране.',
}


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, http',
    )


@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
        message.text.lower(),
    )
    if definition is None:
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        return
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
