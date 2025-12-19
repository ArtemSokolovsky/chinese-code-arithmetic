def TRANS_Q_Z(q: Rational) -> Integer:
    """Сделал: Соколовский Артём"""
    one=Natural(0,[1])
    if COM_NN_D(q.denominator,one)!=0:
        raise ValueError("den!=1")
    return Integer(q.numerator.s,q.numerator.len,q.numerator.A[:])
