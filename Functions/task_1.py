from random import randint

def password_generation():
    password = ''
    for i in range(randint(8, 16)):

        for i in range(1):
            rand_char = randint(48, 122)
            if(rand_char>=48 and rand_char<=57) or (rand_char>=65 and rand_char<=90) or (rand_char>=97 and rand_char<=122): 
                password += chr(rand_char)
            else:
                continue    

    return password        

for i in range(1, 4):
    print(f'Пароль {i}: {password_generation()}')
