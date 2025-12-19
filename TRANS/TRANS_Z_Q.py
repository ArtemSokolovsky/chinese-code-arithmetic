def TRANS_Z_Q(Integer: Z) -> Rational:
    """
    Богданов Никита Константинович
    Преобразование целого в дробное
    """
    # Создаем натуральное 1 для знаменателя
    one_natural = Natural(0, [1])

    return Rational(Z, one_natural)
