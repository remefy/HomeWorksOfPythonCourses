def func_se(a: int, b: int, c: int) -> int:
    var2 = a - (b + c)
    var3 = a - b * c

    expression = min(var2, var3)
    return expression
