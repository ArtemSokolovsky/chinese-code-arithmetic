def NMR_P_P(p: Polynomial) -> Polynomial:
    """Сделал: Соколовский Артём"""
    dp=DER_P_P(p)
    g=GCF_PP_P(p,dp)
    return DIV_PP_P(p,g)
