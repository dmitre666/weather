# Погода

from pyowm import OWM
from pyowm.utils.config import get_default_config
from colorama import init
from colorama import Fore, Back, Style

init()

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('1c0e157087cb3d068e3d395128b25f37', config_dict)

print (Back.RED)

print ("Тебя приветствует дебильный прогноз погоды v3.0.")

print (Back.GREEN)

place = input("В каком городе узнать прогноз погоды?: ")

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print (Back.BLUE)

print("В городе " + place + " сейчас в районе " + str(temp) + " градусов цельсия.")

print( "За окном " + observation.weather.detailed_status + ".")

print (Back.MAGENTA)

if temp < 10:
	print ("Сейчас очень холодно, одевайся потеплее.")
elif temp < 20:
	print ("Сейчас прохладно, одевайся потеплее.")
else:
	print ("Тепло, одевайся как тебе угодно.")

if observation.weather.detailed_status == "небольшой дождь":
	print ("Возьми зонт.")
elif observation.weather.detailed_status == "умеренный дождь":
	print ("Возьми зонт.")
elif observation.weather.detailed_status == "дождь":
	print ("Возьми зонт.")

input()