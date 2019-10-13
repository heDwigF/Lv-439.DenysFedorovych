# # task_1  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 

# def found_middle(*args)
#     """This function founds middle value of your digits """
#     return sum(args)/len(args)


# task_2 Написати функцію, яка повертає абсолютне значення числа

# def total_mean (number):
#     """" This function returns absolute mean """
#     return abs(number)
# print (total_mean(-9))



# task_3 Написати функцію, яка знаходить максимальне число з двох чисел,
#  а також в функції використати рядки документації DocStrings.


# def max_numbers(a,b):
#     """This function returns maximum of 2 numbers"""
#     if a>b:
#         print(a)
#     if a==b:
#         print("The values ​​are equal")
#     else:
#         return b
# print(max_numbers(5,9))



# task_4  Написати програму, яка обчислює площу прямокутника, трикутника та кола

# def rectangel(a,b):
#     """This function calculate area of rectangel"""
#     s_rectangel=a*b
#     return s_rectangel

# def triangle(a,b,c):
#     """This function calculate area of triangle"""
#     p=(a+b+c)/2
#     return ((p*(p-a)*(p-b)*(p-c))** 0.5)

# def circle(r):
#     """This function calculate area of circle"""
#     return(3.14*(r**2))



# task_5 Написати функцію, яка обчислює суму цифр введеного числа.

def sum_of_digits():
    '''Find sum of entered number'''
    number = input('Enter a number ')
    sum_1 = 0
    for i in number:
        i=int(i)
        sum_1+=i
    return sum_1
print(sum_of_digits())


# task_6 Написати програму калькулятор, яка складається з наступних функцій ...


# def adding(a, b):
#     return a + b

# def subtraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     return a / b

# def calculator():
#  """ Calculator program """
# action = input('Please, enter your action: ')
# while True:
#     if action == 'adding':
#         a = float(input('Please, enter your first number:  '))
#         b = float(input('Please, enter your second number:  '))
#         print(adding(a, b))
#         break
#     elif action == 'subtraction':
#         a = float(input('Please, enter your first number:  '))
#         b = float(input('Please, enter your second number:  '))
#         print(subtraction(a, b))
#         break
#     elif action == 'multiplication':
#         a = float(input('Please, enter your first number:  '))
#         b = float(input('Please, enter your second number:  '))
#         print(multiplication(a, b))
#         break
#     elif action == 'division':
#         a = float(input('Please, enter your first number:  '))
#         b = float(input('Please, enter your second number:  '))
#         print(division(a, b))
#         break
#     else:
#         print('False action')
# calculator()

