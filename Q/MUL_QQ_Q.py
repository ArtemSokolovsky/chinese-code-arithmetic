def __mul__(self, other):
    """
    Сделал: Чумаков Никита Ярославович
    Умножение двух рациональных чисел.
    Результат — новый Rational.
    """
    new_numerator = self.numerator * other.numerator
    new_denominator = self.denominator * other.denominator

    # Формируем новую дробь
    result = Rational(new_numerator, new_denominator)

    return result