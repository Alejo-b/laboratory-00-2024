
def calc_bmi(height, weight):
    
    bmi = weight / ((height / 100) ** 2)
    return bmi


def main():
    
    height = float(input("Enter your height in cms: "))
    
    
    weight = float(input("Enter your weight in kgs: "))
    
    
    bmi = calc_bmi(height, weight)

    
    if bmi < 18.5:
        print("Your body mass is low")
    elif  bmi < 24.9:
        print("Your body mass is normal")
    elif  bmi < 29.9:
        print("Your body mass is high")
    elif  bmi < 34.9:
        print("You are in obesity grade 1")
    elif  bmi < 39.9:
        print("You are in obesity grade 2")
    elif bmi >= 40:
        print("You are in obesity grade 3")
    
    
    print(f"Your body mass index is {bmi}")


if __name__ == "__main__":
    main()