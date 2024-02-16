
#BMI formula is wieght in kilograms divided by hiehg in metters squared 

Wieght_and_Height = [80, 1.8]

def Calculate_BMI(Wieght_and_Height):

    BMI = Wieght_and_Height[0] / (Wieght_and_Height[1] ** 2)

    if BMI <= 18.5:

        print("You are underwieght.")
    
    elif BMI <= 25:

        print("You have normal wieght.") 

    elif BMI >= 25:

        print("You are overwieght.")

    return BMI

result = Calculate_BMI(Wieght_and_Height)

print(f"Your BMI is: {result}") #I found out how to make a sentence with a result on google