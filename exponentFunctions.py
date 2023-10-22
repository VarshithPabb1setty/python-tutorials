def raise_to_power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(raise_to_power(2, 3))