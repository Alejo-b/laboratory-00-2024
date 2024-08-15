
#include <stdio.h>

float calcBmi(float h,float w);

// Main function - entry point
int main(){
    // Local variable declaration
    float height;
    float weight;
    float bmi;

    // Ask user for height in cms
    printf("Enter your height in cms: ");
    scanf("%f",&height);

    // Ask user for weight in kgs
    printf("Enter your weight in kgs: ");
    scanf("%f",&weight);

    // Call calcBmi function
    bmi=calcBmi(height,weight);

    if (bmi < 18.5)
    {
        printf("your body mass is low\n");
    }
    else if (18.5 < bmi < 24.9)
    {
        printf("your body mass is normal\n");
    }
    else if (24.9 < bmi < 29)
    {
        printf("your body mass is high\n");
    }
    else if (29 < bmi < 34.9)
    {
        printf("You are in obesity grade 1\n");
    }
    else if (35 < bmi < 39.9)
    {
        printf("You are in obesity grade 2\n");
    }
    else if (40 < bmi)
    {
        printf("You are in obesity grade 3\n");
    }
    
    // Print result
    printf("Your body mass index is %f kg/m^2",bmi);
}

// Implementation of calcBmi function
float calcBmi(float h,float w){
    float bmi;

    // Compute body mass index
    bmi= w/((h/100.0)*(h/100.0));
    return bmi;
}