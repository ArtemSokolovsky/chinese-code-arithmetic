    def __mod__(self, other):
        """
        Богданов Никита Константинович
        Остаток от деления целого числа self на целое число other
        """
        # Проверяем что делитель не ноль
        if other.A == [0] and other.len == 0:
            raise ValueError('You cant divide by zero.')

        # Вычисляем частное
        quotient = self // other

        # Вычисляем произведение делителя и частного
        product = other * quotient

        # Вычисляем остаток
        remainder = self - product

        return remainder
