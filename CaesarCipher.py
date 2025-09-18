'''
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. 
Она должна запрашивать у пользователя следующие данные:
    - направление: шифрование или дешифрование;
    - язык алфавита: русский или английский;
    - шаг сдвига (со сдвигом вправо).

Шифр Цезаря (шифр сдвига) — один из самых простых и наиболее широко известных методов шифрования. 
Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, 
находящимся на некотором постоянном числе позиций левее или правее него в алфавите.

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. 
Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
'''

dir = input('Необходимо выполнить шифрование или дешифрование (введите "ш" или "д")? ').lower()
#lang = input('Введите язык (ру или англ)').lower()
stp = int(input('Шаг сдвига (число): '))
txt = input('Введите текст: ')



def caesar_cipher(direction, step, text):

    eng_alphabet_lower = [chr(j) for j in range(97,123)]
    eng_alphabet_upper = [chr(i) for i in range(65,91)]
    rus_alphabet_lower = [chr(i) for i in range(1072,1104)]
    rus_alphabet_upper = [chr(i) for i in range(1040,1072)]

    for i in range(len(text)):
        #определяем язык
        if text[1].lower() in eng_alphabet_lower:
            low_alphabet = eng_alphabet_lower
            upp_alphabet = eng_alphabet_upper
        else:
            low_alphabet = rus_alphabet_lower
            upp_alphabet = rus_alphabet_upper
        
        
        
        letter = text[i]
        if letter.isalpha():
            if letter == letter.lower():
                index_of_i = low_alphabet.index(letter)
            elif letter == letter.upper():
                index_of_i = upp_alphabet.index(letter)

            if direction == "д":
                cipher_index = (index_of_i - step) % len(low_alphabet)
            elif direction == "ш":
                cipher_index = (index_of_i + step) % len(low_alphabet)
            
            if text[i] == text[i].lower():
                print(low_alphabet[cipher_index], end='')
            elif text[i] == text[i].upper():
                print(upp_alphabet[cipher_index], end='')


        else:
            print(text[i], end='') 

    
#caesar_cipher("д", 25, 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.')   
#caesar_cipher("д", 22, 'Hawnj pk swhg xabkna ukq nqj.')  
#caesar_cipher("ш", 10, 'Блажен, кто верует, тепло ему на свете!')  
caesar_cipher(dir, stp, txt)  