from Z.Integer import Integer


def TRANS_INT_Z(I: int):
    """
    Преобразование Python int в целое число Integer
    """
    # Получаем абсолютное значение
    abs_val = abs(I)
    arr_numbers = [int(char) for char in str(abs_val)]

    # Определяем знак: 1 для отрицательных, 0 для неотрицательных
    sign = 1 if I < 0 else 0

    # Ноль всегда положительный
    if abs_val == 0:
        sign = 0

    return Integer(sign, len(arr_numbers) - 1, arr_numbers)