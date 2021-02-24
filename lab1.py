from datetime import datetime

print('HELLo World!')
username = input('Please, enter your name: ')
len_username = len(username)

print(f'Hello, {username}!')
print(f'Your name has {len_username} letters.')

dbd = input('Please, enter your birth date in format (DD.MM.YYYY): ')
dbd = datetime.strptime(dbd, '%d.%m.%Y')

d = datetime.now()
days = (d - dbd).days
years = int(days // 365.2425)

print(f"Today is {d.strftime('%d.%m.%Y')}, you are "\
        + f'{years} year '\
        + f'({days} day) old.')