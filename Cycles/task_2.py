number_list = [1, '2', 3, 4, '5']

s = 0

for n in number_list:
    number = int(n)
    s += number

print(f'Сумма={s}')
