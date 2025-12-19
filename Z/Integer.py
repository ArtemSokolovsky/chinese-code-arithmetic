from N.Natural import Natural


class Integer:
    def __init__(self, s, n, A):
        self.s = s  # int знак числа (1 — минус, 0 — плюс)
        self.len = n  # int len(A)-1
        self.A = A  # [] массив из int   123 -> [1, 2, 3], -123 -> [1, 2, 3]
        # Убираем ведущие нули
        while len(self.A) > 1 and self.A[0] == 0:
            self.A.pop(0)
        self.len = len(self.A) - 1
        # Если после удаления нулей массив пуст, создаем [0]
        if len(self.A) == 0:
            self.A = [0]
            self.len = 0

    def ABS_Z_Z(self):
        """
        Сделала: Имховик Наталья
        Определение абсолютной величины числа
        Возвращает целое
        """
        # Устанавливаем знак +
        return Integer(0, self.len, self.A[:])

    def SGN_Z_D(self):
        """
        Сделал: Чумаков Никита Ярославович
        Определение знака целого числа:
        -1 — положительное
         0 — равно нулю
         1 — отрицательное
        """
        # Проверим, что число не ноль
        if all(d == 0 for d in self.A):  # Если массив нулей -> z = 0
            return 0
        # Если знак отрицательный (s == 1)
        elif self.s == 1:
            return 1
        # Иначе положительное
        else:
            return -1

    def MUL_ZM_Z(self):
        """
        Сделал: Захаренко Александр
        Умножение целого на (-1)
        """
        # Проверяем, не пытаемся ли заменить знак у нуля
        if all(d == 0 for d in self.A):
            return Integer(0, self.len, self.A[:])

        # Иначе, число не ноль
        new_s = 0 if self.s == 1 else 1  # меняем знак числа
        return Integer(new_s, self.len, self.A[:])

    def __sub__(self, other):
        """
        Выполнил: Сурин Максим
        Вычитание целых чисел: self - other
        """
        return self + other.MUL_ZM_Z()

    def __mul__(self, other):
        """
        Сделал: Соколовский Артём
        Умножение целых чисел: self * other.
        """
        sign = 1 if self.s != other.s else 0

        if self.SGN_Z_D() == 0 or other.SGN_Z_D() == 0:
            return Integer(0, 0, [0])

        # Используем ABS_Z_Z для получения модулей
        abs_self = self.ABS_Z_Z()
        abs_other = other.ABS_Z_Z()

        n1 = Natural(abs_self.len, abs_self.A[:])
        n2 = Natural(abs_other.len, abs_other.A[:])
        mul_result = n1 * n2

        return Integer(sign, mul_result.len, mul_result.A)

    def __floordiv__(self, other):
        """
        Сделал: Соколовский Артём
        Деление целых чисел (self // other).
        """
        if other.SGN_Z_D() == 0:
            raise ZeroDivisionError("Деление на ноль в целых числах")

        result_sign = 1 if self.s != other.s else 0

        # Используем ABS_Z_Z для получения модулей
        abs_self = self.ABS_Z_Z()
        abs_other = other.ABS_Z_Z()

        # Создаем натуральные числа из модулей
        n1 = Natural(abs_self.len, abs_self.A[:])
        n2 = Natural(abs_other.len, abs_other.A[:])

        if n1.COM_NN_D(n2) == -1:
            # Если |self| < |other|, результат 0
            return Integer(0, 0, [0])

        quotient = n1 // n2

        # Для целых чисел нужно учесть знак и округление
        if result_sign == 1 and self % other != Integer(0, 0, [0]):
            # Если результат отрицательный и есть остаток, нужно уменьшить результат на 1
            quotient_digits = [int(d) for d in str(int(quotient.show()) - 1)]
            return Integer(result_sign, len(quotient_digits) - 1, quotient_digits)

        return Integer(result_sign, quotient.len, quotient.A)

    def __mod__(self, other):
        """
        Богданов Никита Константинович
        Остаток от деления целого числа self на целое число other
        """
        if other.SGN_Z_D() == 0:
            raise ValueError('Нельзя делить на ноль.')

        # Вычисляем частное
        quotient = self // other

        # Вычисляем произведение делителя и частного
        product = other * quotient

        # Вычисляем остаток
        remainder = self - product

        return remainder

    def __add__(self, other):
        """
        Выполнил: Сурин Максим
        Сложение целых чисел
        """
        # Если первое число - ноль, возвращаем второе
        if self.SGN_Z_D() == 0:
            return other

        # Если второе число - ноль, возвращаем первое
        if other.SGN_Z_D() == 0:
            return self

        # Если числа одного знака
        if self.s == other.s:
            # Складываем абсолютные значения
            n1 = Natural(self.len, self.A[:])
            n2 = Natural(other.len, other.A[:])
            sum_nat = n1 + n2
            return Integer(self.s, sum_nat.len, sum_nat.A)

        # Если числа разных знаков
        # Сравниваем абсолютные значения
        n1 = Natural(self.len, self.A[:])
        n2 = Natural(other.len, other.A[:])

        cmp_result = n1.COM_NN_D(n2)

        if cmp_result == 0:  # Абсолютные значения равны
            return Integer(0, 0, [0])
        elif cmp_result > 0:  # |self| > |other|
            sub_nat = n1 - n2
            return Integer(self.s, sub_nat.len, sub_nat.A)
        else:  # |self| < |other|
            sub_nat = n2 - n1
            return Integer(other.s, sub_nat.len, sub_nat.A)

    def show(self):
        s = ""
        if self.s == 1 and not (len(self.A) == 1 and self.A[0] == 0):
            s = "-"
        s = s + "".join(list(map(str, self.A)))
        return s