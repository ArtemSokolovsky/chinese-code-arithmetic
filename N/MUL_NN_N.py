def __mul__(self, other):
    """
    Богданов Никита Константинович
    Умножение натуральных чисел
    """
    if not isinstance(other, Natural):
        raise TypeError("The multipliers must be Natural")

    # Если одно из чисел равно нулю, возвращаем ноль
    if self.NZER_N_B() or other.NZER_N_B():
        return Natural(0, [0])

    # Инициализируем результат как 0
    result = Natural(0, [0])

    # Умножаем каждую цифру N2 на N1 и складываем со сдвигом
    for i in range(other.len, -1, -1):
        digit = other.A[i]

        temp_product = self.MUL_ND_N(digit)

        # Создаем сдвиг (умножение на 10^i), если i не самая младшая цифра
        if i < other.len:
            # Аналогия как умножение столбиком
            shift_value = other.len - i  # На сколько разрядов сдвигать
            shift_digits = [shift_value] if shift_value < 10 else [int(d) for d in str(shift_value)]
            shift_natural = Natural(len(shift_digits) - 1, shift_digits)

            # Сдвигаем
            shifted_product = temp_product.MUL_Nk_N(shift_natural)
        else:
            shifted_product = temp_product

        # Складываем с результатом
        result = result + shifted_product

    return result