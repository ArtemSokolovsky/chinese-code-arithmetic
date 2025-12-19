def DIV_NN_Dk(self, other) -> (int, int):
    """
    Сделал: Захаренко Александр
    Вычисление первой цифры деления большего натурального
    на меньшее, домноженное на 10^k,
    где k - номер позиции этой цифры (номер считается с нуля)
    """

    # Проверяем, что self >= other
    if self.COM_NN_D(other) == -1:
        return 0, 0

    # Определяем позицию k
    k = self.len - other.len

    # Если после сдвига other становится больше self, уменьшаем k
    if k > 0:
        other_shifted = other.MUL_Nk_N(k)
        if self.COM_NN_D(other_shifted) == -1:
            k -= 1

    # Если k стал отрицательным, возвращаем 0
    if k < 0:
        return 0, 0

    # Ищем цифру от 9 до 1
    for digit in range(9, 0, -1):
        other_shifted = other.MUL_Nk_N(k)

        # Преобразуем в числа для проверки
        other_shifted_num = int("".join(map(str, other_shifted.A)))
        self_num = int("".join(map(str, self.A)))

        if digit * other_shifted_num <= self_num:
            return digit, k

    return 1, k
