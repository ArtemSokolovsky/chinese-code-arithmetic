# вместо MOD_NN_N (переопределяем Остаток от деления %)
def __mod__(self, other):
    """
    Сделал: Захаренко Александр
    Остаток от деления первого натурального числа
    на второе натуральное (делитель отличен от нуля)
    """

    q = self // other  # Целая часть от деления self на other, Natural
    digit = int("".join(map(str, q.A)))  # Перевели Natural q в int digit, чтобы воспользоваться SUB_NDN_N

    return self.SUB_NDN_N(digit, other)  # self - other * digit