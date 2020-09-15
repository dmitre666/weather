import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('1c0e157087cb3d068e3d395128b25f37', config_dict)

bot = telebot.TeleBot("1340040245:AAEUcd701hhXHFB8c_i6JsuXE2_EIszJa0c")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']

	answer = "В городе " + message.text + " сейчас в районе " + str(temp) + " градусов цельсия." + "\n"
	answer += "За окном " + observation.weather.detailed_status + "." + "\n\n"

	if temp < 10:
		answer += "Сейчас очень холодно, одевайся потеплее." + "\n"
	elif temp < 20:
		answer += "Сейчас прохладно, одевайся потеплее."+ "\n"
	else:
		answer += "Тепло, одевайся как тебе угодно."+ "\n"

	if observation.weather.detailed_status == "небольшой дождь":
		answer += "Возьми зонт."
	elif observation.weather.detailed_status == "умеренный дождь":
		answer += "Возьми зонт."
	elif observation.weather.detailed_status == "дождь":
		answer += "Возьми зонт."
	elif observation.weather.detailed_status == "небольшой проливной дождь":
		answer += "Возьми зонт."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )