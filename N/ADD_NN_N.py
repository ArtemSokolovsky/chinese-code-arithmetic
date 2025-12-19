def __add__(self, other):
    """
    Сделал: Соколовский Артём
    Сложение двух натуральных чисел: self + other.
    """
    A = self.A[::-1]
    B = other.A[::-1]
    res = []
    carry = 0

    for i in range(max(len(A), len(B))):
        da = A[i] if i < len(A) else 0
        db = B[i] if i < len(B) else 0
        s = da + db + carry
        res.append(s % 10)
        carry = s // 10

    if carry:
        res.append(carry)

    res.reverse()
    return Natural(len(res) - 1, res)
