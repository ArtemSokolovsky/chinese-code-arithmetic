def __sub__(self, other):
    """
    Сделал: Соколовский Артём
    Вычитание натуральных чисел: self - other (при self >= other).
    """
    if self.COM_NN_D(other) == -1:
        raise ValueError("SUB_NN_N: self < other")

    A = self.A[::-1]
    B = other.A[::-1]
    res = []
    borrow = 0

    for i in range(len(A)):
        da = A[i]
        db = B[i] if i < len(B) else 0
        diff = da - db - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        res.append(diff)

    while len(res) > 1 and res[-1] == 0:
        res.pop()

    res.reverse()
    return Natural(len(res) - 1, res)
