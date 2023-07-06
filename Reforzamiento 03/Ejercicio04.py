def mostrar_cuadrados(num1, num2):
    for num in range(num1, num2 + 1):
        print(num, ":", num ** 2)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))
mostrar_cuadrados(num1, num2)
