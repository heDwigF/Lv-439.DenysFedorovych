number=input('Enter your number that consist of 4 digits: ')
print('The result of multiplication:', int(number[0])*int(number[1])*int(number[2])*int(number[3]))
print('The reverse number:', number[3],number[2],number[1],number[0])
ordering_number=[int(number[0]),int(number[1]),int(number[2]),int(number[3])]
ordering_number.sort()
print('Sorted number:',ordering_number)