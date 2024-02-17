
integer = 56786

def Digital_Root(integer):

    Sum = 0 

    while integer > 0:

        Sum += integer % 10 

        integer //= 10

    return Sum

result = Digital_Root(integer)

print(f"The digit root of {integer} is {result}") #I found out how to make a sentence with a result on google