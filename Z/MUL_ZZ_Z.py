def __mul__(self, other):
    """
    Сделал: Соколовский Артём
    Умножение целых чисел: self * other.
    """
    sign = 1 if self.s != other.s else 0  # знак результата

    A = self.A[::-1]
    B = other.A[::-1]
    res = [0] * (len(A) + len(B))

    for i in range(len(A)):
        carry = 0
        for j in range(len(B)):
            prod = res[i + j] + A[i] * B[j] + carry
            res[i + j] = prod % 10
            carry = prod // 10
        if carry:
            res[i + len(B)] += carry

    # убираем ведущие нули
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    res.reverse()
    return Integer(sign, len(res) - 1, res)

