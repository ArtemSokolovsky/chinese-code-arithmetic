from N.Natural import Natural
from Z.Integer import Integer


class CRTInteger:
    """
    Класс для работы с китайской теоремой об остатках для ЦЕЛЫХ чисел
    """

    def __init__(self, moduli, residues=None, check_coprime=True):
        """
        Инициализация системы остаточных классов

        Args:
            moduli: список модулей (Natural)
            residues: список остатков (Natural)
            check_coprime: проверять ли взаимную простоту модулей
        """
        self.moduli = moduli

        if check_coprime:
            if not self._check_coprime():
                raise ValueError("Модули должны быть взаимно простыми")

        # Вычисляем M = произведение всех модулей
        self.M = Natural(0, [1])
        for m in moduli:
            self.M = self.M * m

        # Преобразуем M в целое для вычислений
        self.M_int = int(self.M.show())

        # Если переданы остатки, проверяем их
        if residues is not None:
            if len(residues) != len(moduli):
                raise ValueError("Количество остатков должно совпадать с количеством модулей")
            self.residues = residues
            self._precompute_constants()

    def _check_coprime(self):
        """Проверка взаимной простоты модулей"""
        for i in range(len(self.moduli)):
            for j in range(i + 1, len(self.moduli)):
                gcd = self.moduli[i].GCF_NN_N(self.moduli[j])
                if gcd.A != [1]:
                    return False
        return True

    def _precompute_constants(self):
        """Предвычисление констант для быстрого обратного преобразования"""
        self.M_i = []
        self.inv_M_i = []

        for i, m_i in enumerate(self.moduli):
            # M_i = M / m_i
            M_i_val = self.M // m_i
            self.M_i.append(M_i_val)

            # inv_i - мультипликативно обратный к M_i по модулю m_i
            inv_i = self._mod_inverse(M_i_val, m_i)
            self.inv_M_i.append(inv_i)

    def _mod_inverse(self, a, m):
        """
        Нахождение мультипликативно обратного элемента a^{-1} mod m
        Используем расширенный алгоритм Евклида на Python int для надежности
        """
        # Базовый случай
        if not a.NZER_N_B():
            raise ValueError("Нет обратного элемента")

        # Преобразуем в Python int для вычислений
        a_int = int(a.show())
        m_int = int(m.show())

        # Расширенный алгоритм Евклида
        def extended_gcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = extended_gcd(b % a, a)
                return (g, x - (b // a) * y, y)

        g, x, y = extended_gcd(a_int, m_int)
        if g != 1:
            raise ValueError("Элемент не обратим")

        # Приводим к положительному
        inv = x % m_int

        # Преобразуем обратно в Natural
        digits = [int(d) for d in str(inv)]
        return Natural(len(digits) - 1, digits)

    def _residue_to_int(self, residue, m):
        """Преобразование остатка в int с безопасным взятием модуля"""
        try:
            r_int = int(residue.show())
            m_int = int(m.show())
            return r_int % m_int
        except:
            # Если что-то пошло не так, возвращаем 0
            return 0

    @classmethod
    def from_integer(cls, n, moduli):
        """
        Преобразование целого числа в СОК

        Args:
            n: целое число (Integer)
            moduli: список модулей (Natural)
        """
        # Получаем абсолютное значение
        abs_n = n.ABS_Z_Z()
        abs_natural = Natural(abs_n.len, abs_n.A[:])

        # Вычисляем остатки
        residues = []
        for m in moduli:
            residue = abs_natural % m
            residues.append(residue)

        # Если число отрицательное, вычитаем остатки из модулей
        if n.s == 1 and not (len(n.A) == 1 and n.A[0] == 0):
            new_residues = []
            for i, m in enumerate(moduli):
                if residues[i].A == [0]:
                    new_residues.append(Natural(0, [0]))
                else:
                    # Вычисляем m - residue используя int для безопасности
                    m_int = int(m.show())
                    residue_int = int(residues[i].show())
                    diff_int = m_int - residue_int
                    diff_digits = [int(d) for d in str(diff_int)]
                    new_residues.append(Natural(len(diff_digits) - 1, diff_digits))
            residues = new_residues

        return cls(moduli, residues)

    def to_integer(self):
        """
        Обратное преобразование из СОК в целое число по формуле КТО
        """
        if not hasattr(self, 'residues'):
            raise ValueError("Нет остатков для преобразования")

        # Вычисляем X = Σ (x_i * M_i * inv_i) mod M
        result = Natural(0, [0])

        for i, residue in enumerate(self.residues):
            term1 = residue * self.inv_M_i[i]
            term2 = term1 * self.M_i[i]
            result = result + term2

        # Берем по модулю M
        X_natural = result % self.M

        # Преобразуем в целое
        X_int = int(X_natural.show())

        # Определяем знак (симметричный диапазон)
        half_M = self.M_int // 2
        if X_int > half_M:
            # Отрицательное число
            X_int = X_int - self.M_int
            sign = 1
        else:
            sign = 0

        # Преобразуем обратно в Integer
        if X_int == 0:
            return Integer(0, 0, [0])
        digits = [int(d) for d in str(abs(X_int))]
        return Integer(sign, len(digits) - 1, digits)

    def __add__(self, other):
        """Сложение в СОК"""
        if self.moduli != other.moduli:
            raise ValueError("Модули должны совпадать")

        new_residues = []
        for i, m in enumerate(self.moduli):
            # Складываем остатки и берем по модулю
            a_int = self._residue_to_int(self.residues[i], m)
            b_int = self._residue_to_int(other.residues[i], m)
            m_int = int(m.show())

            sum_int = (a_int + b_int) % m_int
            sum_digits = [int(d) for d in str(sum_int)]
            new_residues.append(Natural(len(sum_digits) - 1, sum_digits))

        return CRTInteger(self.moduli, new_residues, check_coprime=False)

    def __sub__(self, other):
        """Вычитание в СОК"""
        if self.moduli != other.moduli:
            raise ValueError("Модули должны совпадать")

        new_residues = []
        for i, m in enumerate(self.moduli):
            a_int = self._residue_to_int(self.residues[i], m)
            b_int = self._residue_to_int(other.residues[i], m)
            m_int = int(m.show())

            diff_int = (a_int - b_int) % m_int
            diff_digits = [int(d) for d in str(diff_int)]
            new_residues.append(Natural(len(diff_digits) - 1, diff_digits))

        return CRTInteger(self.moduli, new_residues, check_coprime=False)

    def __mul__(self, other):
        """Умножение в СОК"""
        if self.moduli != other.moduli:
            raise ValueError("Модули должны совпадать")

        new_residues = []
        for i, m in enumerate(self.moduli):
            a_int = self._residue_to_int(self.residues[i], m)
            b_int = self._residue_to_int(other.residues[i], m)
            m_int = int(m.show())

            prod_int = (a_int * b_int) % m_int
            prod_digits = [int(d) for d in str(prod_int)]
            new_residues.append(Natural(len(prod_digits) - 1, prod_digits))

        return CRTInteger(self.moduli, new_residues, check_coprime=False)

    def __floordiv__(self, other):
        """Деление в СОК (только если делитель обратим по всем модулям)"""
        if self.moduli != other.moduli:
            raise ValueError("Модули должны совпадать")

        new_residues = []
        for i, m in enumerate(self.moduli):
            a_int = self._residue_to_int(self.residues[i], m)
            b_int = self._residue_to_int(other.residues[i], m)
            m_int = int(m.show())

            # Проверяем, что делитель не 0 по модулю
            if b_int == 0:
                raise ZeroDivisionError(f"Делитель равен 0 по модулю {m_int}")

            # Находим обратный элемент
            try:
                # Используем Python int для вычисления обратного
                def modinv(a, m):
                    def egcd(a, b):
                        if a == 0:
                            return (b, 0, 1)
                        else:
                            g, y, x = egcd(b % a, a)
                            return (g, x - (b // a) * y, y)

                    g, x, y = egcd(a, m)
                    if g != 1:
                        raise ValueError(f"Элемент {a} не обратим по модулю {m}")
                    return x % m

                b_inv = modinv(b_int, m_int)
                div_int = (a_int * b_inv) % m_int
                div_digits = [int(d) for d in str(div_int)]
                new_residues.append(Natural(len(div_digits) - 1, div_digits))

            except ValueError as e:
                raise ValueError(f"Деление невозможно: {e}")

        return CRTInteger(self.moduli, new_residues, check_coprime=False)

    def compare_to(self, other):
        """
        Сравнение двух чисел
        Возвращает:
          1  если self > other
          0  если self == other
          -1 если self < other
        """
        if not isinstance(other, CRTInteger):
            raise TypeError("Можно сравнивать только с объектом CRTInteger")

        if self.moduli != other.moduli:
            raise ValueError("Для сравнения числа должны быть в одной системе модулей")

        # Преобразуем оба числа в целые и сравниваем
        int_self = self.to_integer()
        int_other = other.to_integer()

        # Используем сравнение целых чисел (если реализовано в Integer)
        # Или сравниваем через строки для простоты
        val_self = int(int_self.show())
        val_other = int(int_other.show())

        if val_self > val_other:
            return 1
        elif val_self < val_other:
            return -1
        else:
            return 0

    def __eq__(self, other):
        """Равенство чисел в СОК"""
        if not isinstance(other, CRTInteger):
            return False

        if self.moduli != other.moduli:
            return False

        return self.to_integer().show() == other.to_integer().show()

    def __lt__(self, other):
        """Меньше"""
        if not isinstance(other, CRTInteger):
            return NotImplemented

        if self.moduli != other.moduli:
            raise ValueError("Числа должны быть в одной системе модулей")

        return self.compare_to(other) == -1

    def __le__(self, other):
        """Меньше или равно"""
        if not isinstance(other, CRTInteger):
            return NotImplemented

        cmp = self.compare_to(other)
        return cmp == -1 or cmp == 0

    def __gt__(self, other):
        """Больше"""
        if not isinstance(other, CRTInteger):
            return NotImplemented

        return self.compare_to(other) == 1

    def __ge__(self, other):
        """Больше или равно"""
        if not isinstance(other, CRTInteger):
            return NotImplemented

        cmp = self.compare_to(other)
        return cmp == 1 or cmp == 0

    def __ne__(self, other):
        """Не равно"""
        return not self.__eq__(other)


    def show(self):
        """Строковое представление"""
        if not hasattr(self, 'residues'):
            return "CRTInteger(empty)"

        residues_str = ", ".join([f"{r.show()} mod {m.show()}"
                                  for r, m in zip(self.residues, self.moduli)])
        return f"CRTInteger({residues_str})"