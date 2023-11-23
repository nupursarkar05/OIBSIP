def bmi_calculate(weight,height):
    bmi = weight/(height**2)
    return bmi


def bmi_category( bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Please enter valid positive values for weight and height.")
        else:
            calculated_bmi = bmi_calculate(weight, height)
            category = bmi_category(calculated_bmi)
            
        print(f"Your BMI is: {calculated_bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")


if __name__ == "__main__":
    main()    