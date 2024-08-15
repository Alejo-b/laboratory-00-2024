# Función para calcular el índice de masa corporal (IMC)
def calc_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    return bmi

# Punto de entrada principal
def main():
    # Solicitar altura en cm
    height = float(input("Introduce tu altura en cm: "))
    
    # Solicitar peso en kg
    weight = float(input("Introduce tu peso en kg: "))
    
    # Calcular el IMC llamando a la función calc_bmi
    bmi = calc_bmi(height, weight)
    
    # Imprimir el resultado
    print(f"Tu índice de masa corporal es {bmi:.2f} kg/m^2")

# Llamada al método principal
if __name__ == "__main__":
    main()
