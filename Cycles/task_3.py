text_1 = 'abcde123'
text_2 = 'bad_cat_23'
char = ''
check = True
for i in text_1:
    char = i
    for j in text_2:
        if char == j:
            check = True
            break
        else:
            check = False
            
    if check == False:
        print(f'Символ "{char}" нет в "{text_2}"')
    else:
        print(f'Символ "{char}" есть в "{text_2}"')    
            
            
