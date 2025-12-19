def GCF_PP_P(self, other):
    """
    Сделала: Имховик Наталья
    Нахождение НОД многочленов
    Используется алгоритм Евклида,
    полученный многочлен нормализуется
    Возвращает многочлен
    """
    # Копируем исходные многочлены
    A = Polynomial(self.m, self.C[:])
    B = Polynomial(other.m, other.C[:])

    # Алгоритм Евклида нахождения НОД
    while B.C != []:
        # B - многочлен с меньшей степенью
        if A.DEG_P_N() < B.DEG_P_N():
            A, B = B, A
        R = A % B
        A, B = B, R

    # Нормализация: свободный член равен 1
    if A.C != []:
        # normalizer = 1 / (свободный член)
        normalizer = Rational(Integer(0, 0, [1]), Natural(0, [1])) / A.LED_P_Q()
        A = A * normalizer

    return A