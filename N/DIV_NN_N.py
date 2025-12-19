def __floordiv__(self, other):
    """
    Сделал: Захаренко Александр
    Неполное частное от деления первого натурального числа
    на второе с остатком (делитель отличен от нуля)
    """

    # Проверка деления на ноль
    if all(x == 0 for x in other.A):
        raise ZeroDivisionError("Division by zero")

    # Если делимое меньше делителя, возвращаем 0
    if self.COM_NN_D(other) == -1:
        return Natural(1, [0])

    # Определяем максимальную длину результата
    max_length = self.len - other.len + 1
    result_digits = [0] * max_length            # массив для цифр результата

    current = Natural(self.len, self.A.copy())  # текущий остаток

    # Пока текущий остаток >= other
    while current.COM_NN_D(other) != -1:
        # Получаем очередную цифру и её позицию
        digit, k = current.DIV_NN_Dk(other)

        # Если цифра 0, значит деление завершено
        if digit == 0:
            break

        # Записываем цифру в результат на соответствующую позицию
        result_digits[k] = digit

        # Вычитаем: current = current - digit * other * 10^k
        other_shifted = other.MUL_Nk_N(k)  # other * 10^k
        current = current.SUB_NDN_N(other_shifted, digit)

        # Если остаток стал нулевым, завершаем
        if all(x == 0 for x in current.A):
            break

    # Убираем ведущие нули
    while len(result_digits) > 1 and result_digits[-1] == 0:
        result_digits.pop()

    # Разворачиваем массив (т.к. у нас старшие разряды в конце)
    result_digits.reverse()

    return Natural(len(result_digits), result_digits)