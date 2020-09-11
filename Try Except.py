try:
    num = int(input("Enter your  no: "))
    print(num)
except:
    print("invalid Input")

print("//////////// but problem //////////")

try:
    n = int(input("Enter your no "))
    print(n)


# print(10/0)
except ZeroDivisionError:
    print("Division by zero is not possible ")
except ValueError:
    print("Invalid input")

try:
   # print(10 / 0)
    n = int(input("Enter your no "))
    print(n)
except ZeroDivisionError:
    print("zero division is not possible ")
except ValueError as err:
    print(err)

