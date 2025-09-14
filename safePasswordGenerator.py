import random

#строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

#переменная, которая будет содержать все символы, которые могут быть в генерируемом пароле
chars = ''

amount_of_passwords = int(input('Введите количество паролей, которое надо сгенерировать: ')) #количество паролей для генерации
length = int(input('Введите длину одного пароля: ')) #длина одного пароля
numbers = input('Включать ли цифры 0123456789 (введите "д" - да, "н" - нет)? ') 
upper_case = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (введите "д" - да, "н" - нет)? ') 
lower_case = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (введите "д" - да, "н" - нет)? ') 
special_symbols = input('Включать ли символы !#$%&*+-=?@^_ (введите "д" - да, "н" - нет)? ') 
bad_symbols = input('Исключать ли неоднозначные символы il1Lo0O (введите "д" - да, "н" - нет)? ') 

if numbers.lower() == "д":
    chars += digits
if upper_case.lower() == "д":
    chars += uppercase_letters
if lower_case.lower() == "д":
    chars += lowercase_letters
if special_symbols.lower() == "д":
    chars += punctuation
if bad_symbols.lower() == "д":
    for el in chars:
        if el in 'il1Lo0O':
            chars = chars.replace(el, '')

#генерация пароля
def generate_password(length, chars, amount_of_passwords):
    
    #генерация нужного количества паролей
    while amount_of_passwords != 0:
        password = ''
        for _ in range(length):
            password += random.choice(chars)
        amount_of_passwords -= 1
        print(f'Пароль №{amount_of_passwords + 1}: {password}')


# старт программы
generate_password(length, chars, amount_of_passwords)