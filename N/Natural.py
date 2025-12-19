class Natural:
    def __init__(self, n, A):
        self.A = A  # [] массив из int   123 -> [1, 2, 3]
        self.len = n  # int len(A)-1
        # Автоматически убираем ведущие нули при создании
        while len(self.A) > 1 and self.A[0] == 0:
            self.A.pop(0)
        # Корректируем длину после удаления нулей
        self.len = len(self.A) - 1

        # Если после удаления нулей массив пуст, создаем [0]
        if len(self.A) == 0:
            self.A = [0]
            self.len = 0

    def COM_NN_D(self, other):
        """
        Сделал: Соколовский Артём
        Сравнение двух натуральных чисел (self и other).
        """
        A = self.A[:]
        B = other.A[:]

        # Убираем ведущие нули
        while len(A) > 1 and A[0] == 0:
            A.pop(0)
        while len(B) > 1 and B[0] == 0:
            B.pop(0)

        # Сравнение по длине
        if len(A) > len(B):
            return 1
        elif len(A) < len(B):
            return -1

        # Поразрядное сравнение
        for da, db in zip(A, B):
            if da > db:
                return 1
            elif da < db:
                return -1

        return 0

    def NZER_N_B(self):
        """
        Богданов Никита Константинович
        Проверка на ноль натурального числа
        """
        return not (len(self.A) == 1 and self.A[0] == 0)

    def ADD_1N_N(self):
        """
        Выполнил: Сурин Максим
        Добавление 1 к натуральному числу
        """
        # Копируем и переворачиваем
        rev_num = self.A.copy()[::-1]

        # Добавляем 1 к младшему разряду
        rev_num[0] += 1

        # Обрабатываем переносы
        i = 0
        while i < len(rev_num) and rev_num[i] >= 10:
            rev_num[i] -= 10
            if i + 1 < len(rev_num):
                rev_num[i + 1] += 1
            else:
                rev_num.append(1)
            i += 1

        return Natural(len(rev_num) - 1, rev_num[::-1])

    def __add__(self, other):
        """
        Сделал: Соколовский Артём
        Сложение двух натуральных чисел: self + other.
        """
        A = self.A[::-1]
        B = other.A[::-1]
        res = []
        carry = 0

        for i in range(max(len(A), len(B))):
            da = A[i] if i < len(A) else 0
            db = B[i] if i < len(B) else 0
            s = da + db + carry
            res.append(s % 10)
            carry = s // 10

        if carry:
            res.append(carry)

        res.reverse()
        return Natural(len(res) - 1, res)

    def __sub__(self, other):
        """
        Сделал: Соколовский Артём
        Вычитание натуральных чисел: self - other (при self >= other).
        """
        if self.COM_NN_D(other) == -1:
            raise ValueError("SUB_NN_N: self < other")

        A = self.A[::-1]
        B = other.A[::-1]
        res = []
        borrow = 0

        for i in range(len(A)):
            da = A[i]
            db = B[i] if i < len(B) else 0
            diff = da - db - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            res.append(diff)

        # Убираем ведущие нули
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        res.reverse()
        return Natural(len(res) - 1, res)

    def MUL_ND_N(self, digit):
        """
        Выполнил: Сурин Максим
        Умножение натурального числа на цифру (0-9)
        """
        if digit < 0 or digit > 9:
            raise ValueError("Цифра должна быть от 0 до 9")

        if digit == 0:
            return Natural(0, [0])

        rev_num = self.A.copy()[::-1]
        carry = 0

        for i in range(len(rev_num)):
            product = rev_num[i] * digit + carry
            rev_num[i] = product % 10
            carry = product // 10

        if carry > 0:
            rev_num.append(carry)

        return Natural(len(rev_num) - 1, rev_num[::-1])

    def MUL_Nk_N(self, k):
        """
        Богданов Никита Константинович
        Умножение натурального числа на 10^k
        """
        if k == 0:
            return Natural(self.len, self.A[:])

        new_A = self.A + [0] * k
        return Natural(len(new_A) - 1, new_A)

    def __mul__(self, other):
        """
        Богданов Никита Константинович
        Умножение натуральных чисел
        """
        if not isinstance(other, Natural):
            raise TypeError("Множители должны быть типа Natural")

        # Если одно из чисел равно нулю, возвращаем ноль
        if not self.NZER_N_B() or not other.NZER_N_B():
            return Natural(0, [0])

        result = Natural(0, [0])

        # Умножаем self на каждую цифру other и складываем со сдвигом
        for i in range(len(other.A)):
            digit = other.A[len(other.A) - 1 - i]
            partial = self.MUL_ND_N(digit)
            shifted = partial.MUL_Nk_N(i)
            result = result + shifted

        return result

    def SUB_NDN_N(self, digit, other):
        """
        Выполнил: Сурин Максим
        Вычитание из натурального другого натурального, умноженного на цифру
        """
        if digit < 0 or digit > 9:
            raise ValueError("Цифра должна быть от 0 до 9")

        other_multiplied = other.MUL_ND_N(digit)

        if self.COM_NN_D(other_multiplied) == -1:
            return Natural(0, [0])

        return self - other_multiplied

    def DIV_NN_Dk(self, other):
        """
        Сделал: Захаренко Александр
        Вычисление первой цифры деления и её позиции
        """
        if self.COM_NN_D(other) == -1:
            return 0, 0

        k = self.len - other.len
        if k < 0:
            return 0, 0

        # Умножаем other на 10^k
        other_shifted = other.MUL_Nk_N(k)

        # Проверяем, что other_shifted не больше self
        if self.COM_NN_D(other_shifted) == -1:
            k -= 1
            if k < 0:
                return 0, 0
            other_shifted = other.MUL_Nk_N(k)

        # Находим максимальную цифру (1-9)
        for digit in range(9, 0, -1):
            temp = other_shifted.MUL_ND_N(digit)
            if self.COM_NN_D(temp) != -1:
                return digit, k

        return 0, 0

    def __floordiv__(self, other):
        """
        Сделал: Захаренко Александр
        Целочисленное деление натуральных чисел
        """
        # Проверка деления на ноль
        if not other.NZER_N_B():
            raise ZeroDivisionError("Деление на ноль")

        # Если делимое меньше делителя
        if self.COM_NN_D(other) == -1:
            return Natural(0, [0])

        # Если делитель равен 1
        if other.A == [1]:
            return Natural(self.len, self.A[:])

        result_digits = []
        current = Natural(self.len, self.A[:])

        while current.COM_NN_D(other) != -1:
            digit, k = current.DIV_NN_Dk(other)
            if digit == 0:
                break

            # Добавляем нули для позиции k
            while len(result_digits) <= k:
                result_digits.append(0)
            result_digits[k] = digit

            # Вычитаем digit * other * 10^k
            other_shifted = other.MUL_Nk_N(k)
            product = other_shifted.MUL_ND_N(digit)
            current = current - product

            # Если остаток стал нулевым
            if not current.NZER_N_B():
                break

        # Преобразуем result_digits в число
        if not result_digits:
            return Natural(0, [0])

        # Собираем число из цифр
        result_str = ""
        for i in range(len(result_digits) - 1, -1, -1):
            result_str += str(result_digits[i])

        digits = [int(d) for d in result_str]
        return Natural(len(digits) - 1, digits)

    def __mod__(self, other):
        """
        Сделал: Захаренко Александр
        Остаток от деления натуральных чисел
        """
        # Проверка деления на ноль
        if not other.NZER_N_B():
            raise ZeroDivisionError("Деление на ноль")

        # Если делимое меньше делителя
        if self.COM_NN_D(other) == -1:
            return Natural(self.len, self.A[:])

        quotient = self // other
        product = other * quotient
        remainder = self - product

        return remainder

    def GCF_NN_N(self, other):
        """
        Сделал: Чумаков Никита Ярославович
        НОД (наибольший общий делитель) двух натуральных чисел.
        """
        # Алгоритм Евклида с использованием целочисленной арифметики Python для безопасности
        a_int = int(self.show())
        b_int = int(other.show())

        while b_int != 0:
            a_int, b_int = b_int, a_int % b_int

        digits = [int(d) for d in str(a_int)]
        return Natural(len(digits) - 1, digits)

    def LCM_NN_N(self, other):
        """
        Сделала: Имховик Наталья
        Нахождение НОК натуральных чисел
        """
        gcd = self.GCF_NN_N(other)
        product = self * other
        return product // gcd

    def show(self):
        return "".join(list(map(str, self.A)))