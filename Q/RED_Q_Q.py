def RED_Q_Q(self):
    """ 
    Выполнил: Сурин Максим 
    Сокращение дроби
    """

    """ 
    Приведение числителя к натуральному числу;
    вычисление НОД числителя и знаменателя;
    приведение НОД к виду целого числа
    """
    gcf = Natural(self.numerator.len, self.numerator.A).GCF_NN_N(self.denominator)
    gcf = Integer(0, gcf.len, gcf.A)

    new_ratio = self.deepcopy()
    """ Если НОД не равен 1, сокращаем на него числитель и знаменатель """
    if gcf != 1:
        new_ratio.numerator = new_ratio.numerator // gcf
        new_ratio.denominator = new_ratio.denominator // gcf

    return new_ratio
