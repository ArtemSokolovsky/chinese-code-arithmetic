    def MUL_Nk_N(self, other):
        """
        Богданов Никита Константинович
        Умножение натурального числа на 10^k
        """

        # Если число 0 или k = 0, возвращаем исходное число
        if self.NZER_N_B() or other.NZER_N_B():
            return Natural(self.len, self.A[:])

        # Получаем значение k как целое число (количество нулей)
        k_value = 0
        multiplier = 1
        for i in range(other.len, -1, -1):
            k_value += other.A[i] * multiplier
            multiplier *= 10

        # Копируем существующие цифры со сдвигом на k позиций
        new_A = self.A + [0] * k_value

        new_len = len(new_A) - 1
        return Natural(new_len, new_A)
