
# 1. Роздрукувати всі парні числа менші 100 
# (написати два варіанти коду: один використовуючи цикл while, 
# а інший з використанням циклу for).
# (1)

#  i = 0
# while i < 100:
# if i % 2 == 0:    
#     print (i)
#     i = i + 2
# print (list(range(0, 100, 2)))

# (2)

# for i in range(0, 100):
#     if i % 2 == 0:
#         print (i)


# 2.  Роздрукувати всі непарні числа менші 100. 
# (написати два варіанти коду: один використовуючи
#  оператор continue, а інший без цього оператора).

# for i in range(0, 100):
#         if i % 2 == 0:
#             continue
#         print (i)

# test_list = [2,4,6,8,9,10]
# contains_odd = False
# for item in test_list:
#     if not item % 2 == 0:
#          contains_odd = True
#          break

# n = list(range(100)
#     for i in n:
#         print

# list_num = [2, 1, 4, 6, 1, 4, 8, 6]
# for i in range (len(list_num)):
#     list_num [i] = float (list_num[i])
# print(list_num)


#4. Створити список, який містить елементи цілочисельного типу, 
# потім за допомогою циклу перебору змінити тип даних елементів
#  на числа з плаваючою крапкою. 
# (Підказка: використати вбудовану функцію float ()).

#list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
#for n in list_of_numbers:
#   print(float(n), end=',')

#5. Вивести числа Фібоначі включно до введеного числа n,
#  використовуючи цикли. (Послідовність чисел
#  Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)  

# a1 = 0
# a2 = 1
# i = 0
# while i < 13:
#     print(a1)
#     a3 = a1 + a2
#     a1 = a2
#     a2 = a3
#     i += 1

#6.  Створити список, що складається з чотирьох елементів 
# типу string. Потім, за допомогою циклу for,
#  вивести елементи по черзі на екран.

# my_list=['one','two','three', 'four']
# for i in my_list:
#    print(i, end=' ')

# #7.  Змінити попередню програму так, щоб в кінці
#  кожної букви елементів при виводі додавався 
# певний символ, наприклад “#”. 
# (Підказка: цикл for може бути вкладений в 
# інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).

# some_list=['one','two','three', 'four']
# for i in some_list:
#    print(i, end=' #,')

# 8.  Юзер вводить число з клавіатури, 
# написати скріпт, який визначає чи це число просте чи складне.

number=int(input('Enter your number:' ))
if number>1 and number%2==0 and number!=2 or number%3==0 and number!=3:
    print('complex number')
else:
    print('Prime number')