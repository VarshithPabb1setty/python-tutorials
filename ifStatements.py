def main(a, b, c):
    if a >= b and a >= c:
        return "a is greater than b"
    elif b >= a and not(b <= c):
        return "b is greater than a"
    else:
        return "c is greater than a"

print(main(1, 2, 1))