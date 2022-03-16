def BMI (weight, height):
    return weight/(height * height)

def compare (bmi1, bmi2):
    if (bmi1 > 25):
        print("Person 1 is overweight")
    else:
        print("Person 1 has a good BMI")

    if (bmi2 > 25):
        print("Person 2 is not overweight")
    else:
        print("Person 2 has a good BMI")



kofi = BMI(65, 130)
kwaku = BMI(76, 140)

compare(kofi, kwaku)


