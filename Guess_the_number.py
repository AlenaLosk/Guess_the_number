from random import *
from math import *
from time import *


# проверка, что введенная строка string является натуральным числом от border_1 до border_2 включительно
def is_valid(string, border_1, border_2):
    return string.isdigit() and border_1 <= int(string) <= border_2


# запрос числа в пределах [border_1, border_2] с предварительным выводом сообщения text
def get_number(text, border_1, border_2):
    while True:
        string = input(text)
        if is_valid(string, border_1, border_2):
            return int(string)
        else:
            print('Некорректный ввод! ', end='')


# загадываем число (1 элемент) и устанавливаем число попыток (2 элемент)
# с учетом нижней границы border_1 и верхней границы border_2 включительно
def set_goal_number_and_attempt(border_1, border_2):
    return randint(border_1, border_2), ceil(log2(border_2 - border_1))


# игровая логика, где attempts - число попыток, desired_number - загаданное число,
# border_1, border_2 - нижняя и верхняя границы, включительно которые может находиться загаданное число
def is_game_win(attempts, desired_number, border_1, border_2):
    temp = 0
    while attempts > 0:
        attempts -= 1
        temp += 1
        user_number = get_number(f'\nПопытка №{temp}: ', border_1, border_2)
        if desired_number < user_number:
            print('Слишком много! ', end='')
        elif desired_number > user_number:
            print('Слишком мало! ', end='')
        else:
            print('Ура, угадано! ')
            return True
        if attempts > 0:
            print('Попробуй еще раз: ', end='')
    return False


# Основная программа
flag = True
print('Добро пожаловать в числовую угадайку!\nДанная игра существует благодаря курсу "Поколение Python" '
      'https://stepik.org/course/58852\n')
while flag:
    upper_border = get_number('Введи любое число от 2 до 100\n(внутри диапазона [0; данное число]'
                              ' компьютер загадает случайное значение): ', 2, 100)
    goal_number, attempt = set_goal_number_and_attempt(0, upper_border)
    print(f'Угадай, какое число было загадано?\nТы можешь {attempt} раз(а) ввести свой/и вариант(ы) ответа.', end='')
    flag = is_game_win(attempt, goal_number, 0, upper_border)
print('Игра окончена!')
sleep(6)
