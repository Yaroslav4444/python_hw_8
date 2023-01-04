"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    """creating Matrix class"""

    def __init__(self, *args):
        self.matrix_numbers = list(args)

    def __str__(self):
        table = '\n'.join(map(str, self.matrix_numbers))
        table = table.replace(',', '').replace('[', '').replace(']', '')
        return table

    def __add__(self, other):
        my_sum = []
        my_line_sum = []
        for x in range(len(self.matrix_numbers)):
            for y in range(len(self.matrix_numbers[x])):
                my_line_sum.append(
                    self.matrix_numbers[x][y] + other.matrix_numbers[x][y])
            my_sum.append(my_line_sum)
            my_line_sum = []
        return Matrix('\n'.join(map(str, my_sum)))


Matrix_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(Matrix_1)
print()

Matrix_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(Matrix_2)
print()

print(f"Мартица,полученная в результате сложения двух верхних "
      f"матриц:\n{Matrix_1 + Matrix_2}")
