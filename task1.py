# Напишите функцию для транспонирования матрицы


def home_task1_zip(input_matrix: list[list[int]]) -> list[list[int]]:
    """С помощью zip:"""
    result_matrix = list(zip(*input_matrix))
    return result_matrix


def home_task1_cicle(input_matrix: list[list[int]]) -> list[list[int]]:
    """С помощью циклов"""
    result_matrix = []
    for i in range(len(input_matrix[0])):
        result_matrix.append(list())
        for row in input_matrix:
            result_matrix[i].append(row[i])
    return result_matrix


source_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"{source_matrix = }")
print(home_task1_zip(source_matrix))
print(home_task1_cicle(source_matrix))
