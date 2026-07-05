import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, полученный от @BotFather
bot = telebot.TeleBot('8892479839:AAHEIji6KtNgRKujqfUs4sR4Bb8PDwd3TNY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь команду /vpn, чтобы получить VPN-ключ.")

@bot.message_handler(commands=['vpn'])
def send_vpn_key(message):
    # Здесь должна быть логика генерации или получения реального VPN-ключа
    vpn_key = "Ваш VPN-ключ: wg://пример_ключа"
    bot.reply_to(message, vpn_key)

# Запуск бота
bot.polling()