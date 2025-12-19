def SUB_QQ_Q(self, other):
    """
    Сделала: Имховик Наталья
    Находит разность дробей
    Возвращает дробь
    """
    # Находим НОК знаменателей
    lcm = self.denominator.LCM_NN_N(other.denominator)

    # Находим дополнительные множители
    multiplyerA = lcm // self.denominator
    multiplyerB = lcm // other.denominator

    # Умножаем числители на дополнительные множители и вычитаем
    newNumerator = self.numerator * multiplyerA - other.numerator * multiplyerB

    # Создаем результирующую дробь
    return Rational(newNumerator, lcm)