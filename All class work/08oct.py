'''1.  Спробуйте переписати наступний код через map. 
Він приймає список реальних імен і замінює їх хеш-прізвищами,
 використовуючи  більш надійний метод-хешування.'''


names = ['Sam', 'Don', 'Daniel'] 
print (list(map(hash, names)))

'''2.  Вивести список кольору “red”, який найчастіше зустрічається
 в даному списку  [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ] 
 використовуючи функцію filter.'''

# def colours (col):
#     if col == "red":
#         return "red"
# col = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
# print (list(filter(colours,col)))

'''3. Всі ці числа в списку мають стрічковий тип даних, наприклад  
[‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, 
всі числа якого мають тип даних integer:'''

# a= ['1','2','3','4','5','6','7']

'''new_a = a.append(str)
print(list(new_a)) '''

# new_b = list(map(int, a))
# print (new_b)

'''4 Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)'''
  
# miles = [5, 4, 3, 2, 3, 1]
# mm = map(lambda n: round(1.6 * n, 2), miles)
# print(list(mm))


'''5. Знайти найбільший елемент в списку  використовуючи функцію reduce'''

# from functools import reduce
# mylist1 = [1, 2, 3, 4, 5, 7]
# count1 = reduce(lambda a, x: a + x.count('tt'), mylist1, 0)
# print(count1)

