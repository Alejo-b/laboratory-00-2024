#include <stdio.h>

// Declaración de la función
float peso_ideal(float bmi);

float calcular_IMC(float height, float weight);

int main()
{
    float height;
    float weight;
    float bmi;
    float peso_nuevo;
    float peso_reducir;

    // Solicitar altura al usuario en cm
    printf("Ingrese su altura en cm:\n");
    scanf("%f", &height);

    // Solicitar peso al usuario en kg
    printf("Ingrese su peso en kg:\n");
    scanf("%f", &weight);

    bmi = calcular_IMC(height, weight);

    printf("Su índice de masa corporal es %f kg/m^2\n", bmi);

    if (bmi < 18.5)
    {
        printf("Su masa corporal es baja.\n");
    }
    else if (bmi < 24.5)
    {
        printf("Su masa corporal es normal ;)\n");
    }
    else if (bmi < 29.9)
    {
        printf("Su masa corporal indica sobrepeso ;)\n");
    }
    else if (bmi < 34.4)
    {
        printf("Su masa corporal indica obesidad grado 1 ;)\n");
    }
    else if (bmi < 39.9)
    {
        printf("Su masa corporal indica obesidad grado 2, ¡cuídese! ;)\n");
    }
    else
    {
        printf("Su masa corporal indica obesidad grado 3 ;)\n");
    }

    peso_nuevo = peso_ideal(bmi);

    if (bmi > 24.5)
    {
        peso_reducir = bmi - 24.5;
        printf("Debe reducir su peso en aproximadamente %f kilos para alcanzar un estado saludable.\n", peso_reducir);
    }
    else
    {
        peso_reducir = 0;
    }

    if (bmi < 24.5)
    {
        printf("Debe aumentar su peso en aproximadamente %f kilos para alcanzar un estado saludable.\n", peso_nuevo);
    }

    return 0;
}

// Implementación de la función
float peso_ideal(float bmi)
{
    float peso_nuevo = 0;

    if (bmi < 24.5)
    {
        peso_nuevo = 24.5 - bmi;
    }

    return peso_nuevo;
}
float calcular_IMC(float h, float w)
{
    float bmi;

    bmi = w / ((h / 100.0) * (h / 100.0));
    return bmi;
}