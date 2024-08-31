def calculate():
    print("Calculadora en línea de comandos")

    while True:
        operacion = input("Escribe la operación (por ejemplo, '2 + 2') o 'c' para borrar: ")
        if operacion.lower() == 'c':
            continue

        try:
            partes = operacion.split()
            if len(partes) != 3:
                print("Error: Entrada inválida. Usa el formato: número operación número")
                continue

            a = float(partes[0])
            operador = partes[1]
            b = float(partes[2])

            if operador == '+':
                resultado = a + b
            elif operador == '-':
                resultado = a - b
            elif operador == '*':
                resultado = a * b
            elif operador == '/':
                if b == 0:
                    resultado = "Error: No se puede dividir por cero"
                else:
                    resultado = a / b
            else:
                resultado = "Error: Operador inválido. Usa +, -, * o /"
            
            print("Resultado:", resultado)
        except ValueError:
            print("Error: Entrada inválida. Asegúrate de que los números sean válidos.")

if __name__ == "__main__":
    calculate()
