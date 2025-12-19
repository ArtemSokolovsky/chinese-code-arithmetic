    def __add__(self, other):
        """
        Богданов Никита Константинович
        Сложение многочленов
        """

        max_degree = max(self.m, other.m)

        # Создаем массив для коэффициентов результата (от старшей степени к младшей)
        result_coeffs = []

        for i in range(max_degree + 1):

            degree = max_degree - i # Текущая степень (от старшей к младшей)

            # Находим соответствующие коэффициенты
            self_index = self.m - degree if degree <= self.m else -1
            other_index = other.m - degree if degree <= other.m else -1

            if self_index >= 0 and self_index <= self.m:
                coeff1 = self.C[self_index]
            else:
                coeff1 = Rational(Integer(0,0,[0]), Natural(0, [1]))

            if other_index >= 0 and other_index <= other.m:
                coeff2 = other.C[other_index]
            else:
                coeff2 = Rational(Integer(0,0,[0]), Natural(0, [1]))

            # Складываем коэффициенты
            sum_coeff = coeff1 + coeff2
            result_coeffs.append(sum_coeff)

        # Убираем ведущие нули (в начале массива)
        while len(result_coeffs) > 1 and result_coeffs[0].numerator.A == [0]:
            result_coeffs.pop(0)
            max_degree -= 1

        result_degree = len(result_coeffs) - 1

        return Polynomial(result_degree, result_coeffs)

