n = int(input("Ingrese cuántos términos de la serie Fibonacci desea: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b