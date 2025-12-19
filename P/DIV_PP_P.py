def __floordiv__(self, other):
    """
    делал: Чумаков Никита Ярославович
    Частное от деления многочлена P1 на P2 при делении с остатком.
    !!! Работает как деление столбиком !!!
    сначала делите старшие коэф -> factor - коэф в частном
    после формируете многочлен = factor * делитель * степень (степень = разность степеней делимого и делителя)
    и из делимого вычитаете этот многочлен и так продолжаете дальше пока степень делимого больше степени делителя или делимое не ноль
    """
    # Проверка делителя на нуль
    if all(d.numerator.A == [0] for d in other.C):
        raise ZeroDivisionError("Деление на нулевой многочлен невозможно")

    # Копии делимого и делителя
    A = Polynomial(self.m, self.C[:])
    B = Polynomial(other.m, other.C[:])

    # Частное Q = 0
    zero_rat = Rational(Integer(0, 0, [0]), Natural(0, [1]))
    Q = Polynomial(0, [zero_rat])

    # Основной цикл деления
    while True:
        # Вычисляем степени через DEG_P_N
        degA_nat = A.DEG_P_N()
        degB_nat = B.DEG_P_N()

        # Переводим Natural → int
        degA = int(''.join(str(x) for x in degA_nat.A))
        degB = int(''.join(str(x) for x in degB_nat.A))

        # Если степень делимого меньше или делимое == 0 — заканчиваем
        if degA < degB or all(c.numerator.A == [0] for c in A.C):
            break

        # Разность степеней
        k = degA - degB

        # Старшие коэффициенты (предполагаем C[0] — старший)
        a_lead = A.C[0]
        b_lead = B.C[0]

        # Делим коэффициенты (Rational)
        factor = a_lead / b_lead

        # Создаём одночлен factor * x^k
        term = Polynomial(0, [factor])
        term_shifted = term.MUL_Pxk_P(k)

        # Прибавляем одночлен к частному (будущий ответ)
        Q = Q + term_shifted

        # Умножаем делитель на factor и x^k
        B_shifted = B.MUL_Pxk_P(k)  # умножаем на x^k
        B_scaled = Polynomial(
            B_shifted.m,
            [c * factor for c in B_shifted.C]  # умножаем все коэф. делителя на factor
        )

        # Вычитаем (A = A - B_scaled)
        A = A - B_scaled

        # Удаляем ведущие нули, если появились
        while len(A.C) > 1 and A.C[0].numerator.A == [0]:
            A.C.pop(0)
            A.m -= 1

    # Корректируем степень частного (удаляем ведущие нули)
    while len(Q.C) > 1 and Q.C[0].numerator.A == [0]:
        Q.C.pop(0)
    Q.m = len(Q.C) - 1

    return Q