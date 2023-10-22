try:
    # value = 10/0

    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)