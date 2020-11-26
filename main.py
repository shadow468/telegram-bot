import telebot

from pyowm.owm import OWM

from pyowm.utils.config import get_default_config
bot = telebot.TeleBot('1493922349:AAHVQMEDFscf1q50j2HS-IRSbfdHrt3x5zI')

@bot.message_handler(commands=['start'])
def start(message):

	send_mess = (f"Привет {message.from_user.first_name}. Я бот богоды.\nВведите название города или деревни")
	bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	owm = OWM('4d9b5e79bfddd0b1bee5d376bbc02561')
	x = get_message_bot
	mgr  =  owm . weather_manager ()
	observation = mgr.weather_at_place(x)
	w = observation.weather
	temp=w.temperature('celsius')['temp']
	col = ( f'Температура: {temp} , {w.status} '  )
	bot.send_message(message.chat.id,col)

bot.polling(none_stop=True)
# @test99751_bot