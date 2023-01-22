text = 'Python - это Питон!'

count = 0
for t in text:
    count += 1

print(f'Количестов символов в тексте, подсчитаных через for: {count}') 

count_2 = 0
t = 0

while t < len(text):
    count_2 += 1
    t += 1

print(f'Количестов символов в тексте, подсчитаных через while: {count_2}') 
