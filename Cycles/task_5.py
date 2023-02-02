lines = '----+----------------------------'
p = '  '
print('Таблица умножения')
print(lines)
print('| x |', end=' ')
for i in range(1, 10):
    if i == 9:
        p = ' |'
    print(i, end=p)
print(f'\n{lines}')
for n in range(1, 10):
    print(f'| {n} |', end=' ')
    for m in range(1, 10):
        s = n*m
        if n < 5 and s < 8:
            p = '  '
        elif n == 1 and s == 8:
            pass      
        else:
            p = ' '    
        print(s, end=p)
    print('|')
   
print(lines)