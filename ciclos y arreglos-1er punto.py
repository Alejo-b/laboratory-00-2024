def main():
    
    citizen = int(input("Enter de value of citizen that you will request: \n"))
    
    
    weight= [0.0] * citizen
    
    height = [0.0] * citizen
    

    for i in range (citizen):
        
        height [i] = float(input(f"Enter the height of the citizen number {i+1}: \n")) 
        weight [i] = float(input(f"Enter the weight of the citizen number {i+1}: \n"))     
        
    for j in range (citizen):
        
        bmi = weight[j] / ((height[j]/100)*(height[j]/100))
        
        if bmi < 18.5:
            print(f"the body mass of the citizen numeber {j+1} is low\n")
        elif  bmi < 24.9:
            print(f"the body mass of the citizen numeber {j+1} is normal\n")
        elif  bmi < 29.9:
            print(f"the body mass of the citizen numeber {j+1} is high\n")
        elif  bmi < 34.9:
            print(f"the body mass of the citizen numeber {j+1} is on obesity grade 1\n")
        elif  bmi < 39.9:
            print(f"the body mass of the citizen numeber {j+1} is on obesity grade 2\n")
        elif bmi >= 40:
            print(f"the body mass of the citizen numeber {j+1} is on obesity grade 3\n")
    
    
        print(f"Your body mass index is {bmi}\n")


if __name__ == "__main__":
    main()