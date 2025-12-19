def GCF_NN_N(self, other):
    """
    Сделал: Чумаков Никита Ярославович
    НОД (наибольший общий делитель) двух натуральных чисел.
    """
    # Создаём копии, чтобы не испортить исходные
    A = Natural(self.len, self.A[:])
    B = Natural(other.len, other.A[:])

    while B.NZER_N_B():  # пока B != 0
        # Проверяем, какое больше
        cmp = A.COM_NN_D(B)

        if cmp == 1:  # A < B -> поменяем их местами
            A, B = B, A

        # Теперь A >= B, можно брать остаток
        R = A % B
        A, B = B, R

    return A