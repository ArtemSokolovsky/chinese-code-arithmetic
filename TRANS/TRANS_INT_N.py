from N.Natural import Natural


def TRANS_INT_N(I:int):
    arr_numbers = [int(char) for char in str(I) if char.isdigit()]
    return Natural(len(arr_numbers)-1,arr_numbers)