def __mul__(self, other):
    """ 
    Выполнил: Сурин Максим 
    Умножение многочленов
    """

    """ Инициализация нулевого полинома """
    product = Polynomial(0, Rational(Integer(0, 0, [0]), Natural(0, [1])))
    
    """ 
    Умножение первого полинома на каждый член второго полинома:
    1) умножение на коэффициент каждого члена 
    2) домножение на x^(степень текущего члена), если его коэффициент не ноль
    """
    for i in range(other.m + 1):
        temp_poly = self.MUL_PQ_Q(other.C[i])
        if other.C[i].numerator.A != [0]:
            temp_poly = temp_poly.MUL_Pxk_P(other.m - i)

        product = product + temp_poly

    return product
