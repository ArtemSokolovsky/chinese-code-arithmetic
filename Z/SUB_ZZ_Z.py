def __sub__(self, other):
    """ 
    Выполнил: Сурин Максим 
    Вычитание целых чисел
    """

    """ Если первое число - ноль, возвращаем второе с противоположным знаком """
    if self.SGN_Z_D() == 0:
        return other.MUL_ZM_Z()
    
    """ Если второе число - ноль, возвращаем первое """
    if other.SGN_Z_D() == 0:
        return self

    """ 
    Если числа одного знака - вычитаем из большего меньшее;
    если большее - вычитаемое, знак минус, иначе плюс
    """
    if self.SGN_Z_D() == other.SGN_Z_D():
        n1 = Natural(self.len, self.A)
        n2 = Natural(other.len, other.A)

        if n1.COM_NN_D(n2) != -1:
            sub_of_mods = n1 - n2
            if self.SGN_Z_D == -1:
                sign = 1
            else:
                sign = 0

            return Integer(sign, sub_of_mods.len, sub_of_mods.A)
        else:
            sub_of_mods = n1 - n2
            if self.SGN_Z_D == -1:
                sign = 0
            else:
                sign = 1

            return Integer(sign, sub_of_mods.len, sub_of_mods.A) 
    
    """ Если числа разных знаков - складываем модули и устанавливаем общий знак """
    if self.SGN_Z_D() != other.SGN_Z_D():
        sum_of_mods = Natural(self.len, self.ABS_Z_Z().A) + Natural(other.len, other.ABS_Z_Z().A)
        return Integer(self.s, sum_of_mods.len, sum_of_mods.A)