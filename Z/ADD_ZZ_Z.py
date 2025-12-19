def __add__(self, other):
    """ 
    Выполнил: Сурин Максим 
    Сложение целых чисел
    """

    """ Если первое число - ноль, возвращаем второе """
    if self.SGN_Z_D() == 0:
        return other
    
    """ Если второе число - ноль, возвращаем первое """
    if other.SGN_Z_D() == 0:
        return self

    """ Если числа одного знака - складываем модули и устанавливаем общий знак """
    if self.SGN_Z_D() == other.SGN_Z_D():
        sum_of_mods = Natural(self.len, self.ABS_Z_Z().A) + Natural(other.len, other.ABS_Z_Z().A)
        return Integer(self.s, sum_of_mods.len, sum_of_mods.A)
    
    """ Если числа разных знаков - вычитаем из большего меньшее, берём знак большего """
    if self.SGN_Z_D() != other.SGN_Z_D():
        n1 = Natural(self.len, self.A)
        n2 = Natural(other.len, other.A)

        if n1.COM_NN_D(n2) != -1:
            sub_of_mods = n1 - n2
            return Integer(n1.s, sub_of_mods.len, sub_of_mods.A)
        else:
            sub_of_mods = n2 - n1
            return Integer(n2.s, sub_of_mods.len, sub_of_mods.A) 