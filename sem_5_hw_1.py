# Задание 1
# Напишите функцию для транспонирования матрицы


def transpose_matrix(matrix):
    rows = len(matrix)                         # Определение числа строк и столбцов в исходной матрице
    cols = len(matrix[0]) if matrix else 0

    transposed = [[None] * rows for _ in range(cols)]    # Создание пустой матрицы с перевернутыми размерами
                                                         # (столбцы станут строками и наоборот)

    for i in range(rows):                                # Заполнение новой матрицы данными
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [                                                 # Пример использования функции
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = transpose_matrix(matrix)
for row in result:
    print(row)
