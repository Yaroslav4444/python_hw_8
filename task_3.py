"""
Задание 3.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
 нуля в качестве делителя программа должна корректно обработать эту ситуацию и
 не завершиться с ошибкой.
"""


class OwnError(Exception):
    """creating Exception class"""
    def __init__(self, txt):
        self.txt = txt


user_number = input("Введите число: ")

try:
    user_number = int(user_number)
    if user_number == 0:
        raise OwnError("На ноль делить нельзя,введите другое число!")
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    print(f"Вы ввели число {user_number}")
