def procesar_entrada(entrada):
    try:
        partes = entrada.split()
        if len(partes) != 3:
            return "Error: Entrada inválida. Usa el formato: número operación número"

        a = float(partes[0])
        operador = partes[1]
        b = float(partes[2])

        if operador == '+':
            return suma(a, b)
        elif operador == '-':
            return resta(a, b)
        elif operador == '*':
            return multiplicacion(a, b)
        elif operador == '/':
            return division(a, b)
        else:
            return "Error: Operador inválido. Usa +, -, * o /"
    except ValueError:
        return "Error: Entrada inválida. Asegúrate de que los números sean válidos."

def calculate():
    print("Calculadora en línea de comandos")
    while True:
        operacion = input("Escribe la operación (por ejemplo, '2 + 2') o 'c' para borrar: ")
        if operacion.lower() == 'c':
            continue

        resultado = procesar_entrada(operacion)
        print("Resultado:", resultado)

if __name__ == "_main_":
    calculate()