
integer = 28756

def Rotated_digits(integer):
    
    last_digit = integer % 10 

    integer = integer // 10 

    rotation = last_digit * (10 ** (len(str(integer)))) + integer #I was able to figure out this equation with the help of the internet 

    return rotation 

result = Rotated_digits(integer)

print(f"The rotated digits are {result}") #I found out how to make a sentence with a result on google