def int2roman(num: int) -> str:
    # keep order
    symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    roman = []
    for v, symbol in symbols:
        while num >= v:
            roman.append(symbol)
            num -= v
        if num == 0:
            break
    return "".join(roman)


