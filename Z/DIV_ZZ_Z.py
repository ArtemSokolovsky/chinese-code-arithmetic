def __truediv__(self, other):
    """
    Сделал: Соколовский Артём
    Деление целых чисел (self / other).
    """

    # Проверка делителя на ноль
    if all(d == 0 for d in other.A):
        raise ZeroDivisionError("Деление на ноль в целых числах")

    # Определяем знак результата
    result_sign = 1 if self.s != other.s else 0

    # Берём модули чисел (натуральные части)
    abs_self = self.ABS_Z_N()
    abs_other = other.ABS_Z_N()

    # Если |self| < |other| → результат = 0
    if abs_self.COM_NN_D(abs_other) == -1:
        return Integer(0, 0, [0])

    # Используем целочисленное деление (без остатка)
    quotient = abs_self // abs_other  # базовый оператор для натуральных чисел

    # Формируем результат
    result = Integer(result_sign, quotient.len, quotient.A)

    return result
