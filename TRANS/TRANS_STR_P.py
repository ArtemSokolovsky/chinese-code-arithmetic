from P.Polynomial import Polynomial
from TRANS.TRANS_INT_Q import TRANS_INT_Q
'''
def TRANS_STR_P(s:str):
    l=0
    if s[0] == '-':
        q = TRANS_INT_Q(-1)
        l = len(s)-1
    else:
        q = TRANS_INT_Q(1)
        l = len(s)
    q_arr = [q]
    if l==1 or s[-1]=='1':
        q_arr.append(TRANS_INT_Q(0))
        return Polynomial(1, q_arr)
    for i in range((int(s[-1]))):
        q_arr.append(TRANS_INT_Q(0))
    return Polynomial(int(s[-1]), q_arr)

'''


def TRANS_STR_P(s: str):
    # Определяем знак
    power = 1
    if s[0] == '-':
        positive = False
        q = TRANS_INT_Q(-1)
        s = s[1:]
    else:
        positive = True
        q = TRANS_INT_Q(1)
        s = s[1:]
    q_arr = [q]
    # Обрабатываем степень
    if '^' in s:
        # Формат x^n
        power = int(s.split('^')[1])
        for i in range(power):
            q_arr.append(TRANS_INT_Q(0))

    else:
        q_arr.append(TRANS_INT_Q(0))
        power = 1

    return Polynomial(power, q_arr)