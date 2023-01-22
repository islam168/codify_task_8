number = int(input('Введите целое цисло: '))
list_number = list(str(number))
list_number.reverse()
number_rev = ''
for i in list_number:
    number_rev += i
    
print(number_rev)