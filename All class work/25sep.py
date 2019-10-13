# import pyowm

# city=input("Enter your city: ")
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')      # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('Lviv')
# w = observation.get_weather()
# print('Rigth now time is: ', w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)




# task_1

''' Напишіть скрипт-гру, яка генерує випадковим чином число 
з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число.
Програма зчитує числа, які вводить користувач і видає користувачу підказки про 
те чи загадане число більше чи менше за введене користувачем. Гра має тривати
 до моменту поки користувач не введе число, яке загадане програмою, тоді друкує
 повідомлення привітання. (для виконання завдання необхідно імпортувати 
  модуль random, а з нього функцію randint())'''


# import random
# number = random.randint(1,100)
# def Guess_game():
#     while True:
#         my_number = int(input('Please enter a number '))
#         if my_number>number:
#             print('Your number is larger than secret number')
#         elif my_number<number:
#             print('Your number is smaller than secret number')
#         else:
#             print('You win!!!')
#             break
# Guess_game()



'''2.  Напишіть скрипт, який обчислює площу прямокутника a*b, 
площу трикутника 0.5*h*a, площу кола pi*r**2. 
(для виконання завдання необхідно імпортувати 
 модуль math, а з нього функцію pow() та значення змінної пі).'''

# import math
# def calculation_area():
#     """Calculation area"""
#     while True:
#         try:
#             figure = input("Enter your figure: ")
#             if figure == "rectangle":
#                 a = int(input("Enter first side "))
#                 b = int(input("Enter second side "))
#                 rectangle_area = (b * a)
#                 print('Your area is ', rectangle_area)
#                 break
#             elif figure == "triangle":
#                 c = int(input("Enter first side "))
#                 d = int(input("Enter height "))
#                 triangle_area = c * d * 0.5
#                 print('Your area is ', triangle_area)
#                 break
#             elif figure == "circle":
#                 r = int(input("Enter radius "))
#                 pi = math.pi
#                 circle_area = pi * r **2
#                 print('Your area is ', circle_area)
#                 break
#         except:
#             break
# calculation_area()