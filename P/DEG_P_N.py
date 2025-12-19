def DEG_P_N(self):
    """
    Сделал: Чумаков Никита Ярославович
    DEG_P_N: Polynomial → Natural
    Возвращает степень многочлена как натуральное число.
    """
    # Получаем степень многочлена (int)
    m = self.m

    # Преобразуем в массив цифр
    A = [int(d) for d in str(m)]

    # Создаём объект Natural
    N = Natural(len(A) - 1, A)

    return N