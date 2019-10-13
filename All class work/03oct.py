'''1. Напишіть програму, яка пропонує користувачу ввести ціле число 
і визначає чи це число парне чи непарне, чи введені дані коректні.'''

# try:
#     a = int(input("Enter your number: "))
#         if x % 2 != 0:
# except ValueError: 
#     print("That is not correct number") 
# else: 
#     print("No exception")
     


'''task_2 Напишіть програму, яка пропонує користувачу ввести свій вік, 
після чого виводить повідомлення про те чи вік є парним чи непарним числом.
 Необхідно передбачити можливість введення від’ємного числа, в цьому випадку 
згенерувати власну виняткову ситуацію. Головний код має викликати функцію,
 яка обробляє введену інформацію.'''


# while True:
#     try:
#         a = int(input("Enter your age: "))
#         if a < 1:
#             raise ValueError("That is not a positive number!")
#         elif a % 2 == 0:
#             print("Even number")
#         else:
#             print("Not an even number")
#     except TypeError:
#         print("Caught TypeError Exception")
#     except ValueError:
#         print("Caught ValueError Exception")
#     else:
#         print("Nothing went wrong")
#     exit()

'''task_3 Напишіть програму для обчислення частки двох чисел, 
які вводяться користувачем послідовно через кому, передбачити 
випадок ділення на нуль, випадки синтаксичних помилок та випадки 
інших виняткових ситуацій. Використати блоки else та finaly.'''

# while True:
#     try:
#         a,b = int(input("Enter your 2 numbers: ").split(','))
#         sum = a/b
#         if b == 0:
#             raise ZeroDivisionError("You can not divise by null")  
#     except TypeError:
#         print("Caught TypeError Exception")
#     except ValueError:
#         print("Caught ValueError Exception")
#     else:
#         print("Result is: ", sum)

'''4.  Написати  програму, яка аналізує введене число та в залежності 
від числа видає день тижня, який відповідає цьому числу 
(1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення 
чисел від 8 і більше, а також випадки введення не числових даних.'''

try:
    num=int(input('Give a number from 1 to 7 '))
    if num==1:
        print ('Monday')
    elif num==2:
        print ('Tuesday')
    elif num==3:
        print ('Wednesday')
    elif num==4:
        print ('Thirsday')
    elif num==5:
        print ('Friday')
    elif num==6:
        print ('Saturday')
    elif num==7:
        print ('Sunday')
    elif num>7:
        raise ValueError
except ValueError:
    print ('False value.')
finally:
    print ('END')
