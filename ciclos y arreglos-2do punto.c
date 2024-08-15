int main() {
   
    float height;
    float weight;
    float bmi;
    float personas;
    float bajo_peso = 0;
    float peso_normal = 0;
    float sobrepeso = 0;
    float obesidad = 0;


    printf("Enter the number of citizen that you will enter their data:\n");
    scanf("%f", &personas);

    while (personas <= 0) {
        printf("Please enter a value greater than zero:\n");
        scanf("%f", &personas);
    }

    
    for (int i = 0; i < personas; i++) {
        
        printf("Enter your height in cms:\n");
        scanf("%f2", &height);

        
        printf("Enter your weight in kgs:\n");
        scanf("%f", &weight);

        
        bmi = weight / ((height / 100.0) * (height / 100.0));


        
        if (bmi < 18.5) {
            bajo_peso++;
        } else if (bmi < 24.9) {
            peso_normal++;
        } else if (bmi < 29.9) {
            sobrepeso++;
        } else if (bmi < 34.9) {
            obesidad++;
        } else if (bmi < 39.9) {
            obesidad++;
        } else {
            obesidad++;
        }
     }
    printf("Underweight: %.2f%%\n", (bajo_peso / personas) * 100);
    printf("Normal weight: %.2f%%\n", (peso_normal / personas) * 100);
    printf("Overweight: %.2f%%\n", (sobrepeso / personas) * 100);
    printf("Obesity: %.2f%%\n", (obesidad / personas) * 100);

return 0;
}