from random import randint
number = 4 #randint(1, 101)
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    if num.isdigit():
        return 1 <= int(num) <= 100
    else:
        return False

def guess_num():
    
    attempts_counter = 0

    while True:
        response = input('Введите число число от 1 до 100: ')
        attempts_counter += 1
        
        if not is_valid(response):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        response = int(response)

        if response < number:
            print('Ваше число меньше загаданного, попробуйте еще раз')
            attempts_counter += 1
        elif response > number:
            print('Ваше число больше загаданного, попробуйте еще раз')
            attempts_counter += 1
        else:
            print(f'Вы угадали, поздравляем! Загаданное число: {number}. Количество попыток: {attempts_counter}')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


guess_num()