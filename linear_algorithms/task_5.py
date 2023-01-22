from datetime import date
current_date = date.today()
converted_current_date = current_date.strftime('%d.%m.%Y')

print(f'год-месяц-день: {current_date}')
print(f'день.месяц.год: {converted_current_date}')

