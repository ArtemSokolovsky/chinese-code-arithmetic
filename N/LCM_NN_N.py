def LCM_NN_N(self, other):
    """
    Сделала: Имховик Наталья
    Нахождение НОК натуральных чисел
    Используем НОК(a, b) = (a * b) / НОД(a, b)
    Возвращает натуральное
    """
    gcd = self.GCF_NN_N(other)
    return self * other // gcd