def DER_P_P(p: Polynomial) -> Polynomial:
    """Сделал: Соколовский Артём"""
    if p.m==0:
        zero=Rational(Integer(0,0,[0]),Natural(0,[1]))
        return Polynomial(0,[zero])
    def _nat_from_small(k:int)->Natural:
        if k==0:return Natural(0,[0])
        d=[]
        while k>0:
            d.append(k%10)
            k//=10
        d.reverse()
        return Natural(len(d)-1,d)
    coeffs=[]
    for power in range(1,p.m+1):
        r=p.C[power]
        k_nat=_nat_from_small(power)
        k_int=TRANS_N_Z(k_nat)
        new_num=r.numerator*k_int
        coeffs.append(Rational(new_num,Natural(r.denominator.len,r.denominator.A[:])))
    return Polynomial(p.m-1,coeffs)
