def peso_ideal (bmi):
    peso_nuevo=0

    if bmi< 24.5:
        peso_nuevo= 24.5 - bmi
        print("Usted debe aumentar su masa corporal para estar en un estado normal.")

    elif bmi > 24.5:
        peso_nuevo= bmi-24.5
        print ("Usted debe reducir su masa corporal para mantenerse sano.")
    else:
        print ("usted se encuentra sano")

def main () :

    height = float(input("ingrese su altura (cm) :\n"))
    weight = float(input("ingrese su peso (en gramos): \n"))

    bmi= weight / ((height / 100.0) ** 2)

    print(f"Su índice de masa corporal es {bmi:.2f} kg/m^2")

   
    if bmi < 18.5:
        print("Su masa corporal es baja.")
    elif bmi < 24.5:
        print("Su masa corporal es normal ;)")
    elif bmi < 29.9:
        print("Su masa corporal indica sobrepeso ;)")
    elif bmi < 34.4:
        print("Su masa corporal indica obesidad grado 1 ;)")
    elif bmi < 39.9:
        print("Su masa corporal indica obesidad grado 2, ¡cuídese! ;)")
    else:
        print("Su masa corporal indica obesidad grado 3 ;)")
    
    
    peso_nuevo = peso_ideal(bmi)

   
    if bmi > 24.5:
        peso_reducir = bmi - 24.5
        print(f"Debe reducir su peso en aproximadamente {peso_reducir:.2f} kilos para alcanzar un estado saludable.")
    else:
        peso_reducir = 0 

    if bmi < 24.5:
        print(f"Debe aumentar su peso en aproximadamente {peso_nuevo:.2f} kilos para alcanzar un estado saludable.")

if __name__ == "__main__":
    main()
    