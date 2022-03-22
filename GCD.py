num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def compare(a, b):
    if a > b:
        return a, b
    else:
        return b, a


num1, num2 = compare(num1, num2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print("GCD is: " + str(gcd(num1, num2)))