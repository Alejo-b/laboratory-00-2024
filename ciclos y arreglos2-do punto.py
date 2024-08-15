def main():
    personas = int(input("Enter the number of citizen that you will enter their data:\n"))
    
    bajo_peso = 0
    peso_medio = 0
    sobre_peso = 0
    
    while personas <= 0:
        personas = int(input("Enter a valid value of people\n"))
    
    for i in range(personas):
        weight = float(input("Enter your weight in kgs:\n"))
        height = float(input("Enter your height in cms:\n"))
        bmi = weight / ((height / 100.0) * (height / 100.0))
        
        if bmi < 18.5:
            bajo_peso += 1
        elif bmi < 24.9:
            peso_medio += 1
        else:
            sobre_peso += 1

    print(f"Underweight: {bajo_peso / personas * 100} %")
    print(f"Normal weight: {peso_medio / personas * 100} %")
    print(f"Overweight: {sobre_peso / personas * 100} %") 

if __name__ == "__main__":
    main()
    
    