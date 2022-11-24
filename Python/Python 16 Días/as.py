def factorial(n):
    factorial = 1
    i = 1
    while (i <= n):
        factorial - factorial * i
        i = i + 1
    return factorial


def exp(x):
    suma = 0
    for n in range(5 + 1):
        suma = suma + x ** n / factorial(n)
    return suma


fhan = open('C:\\Users\\ivane\\Desktopexp.txt', 'w')
for x in range(10001):
    fhan.write(str(exp(x)) + '\n')
fhan.close()
