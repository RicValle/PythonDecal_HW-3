
x = 2
y = 3

def raised_to_a_power(x, y):

    sum = 1

    for _ in range(y): #The underline allowing for a throwaway variable was something I found online when I was stuck 
        
        sum *= x 
    
    return sum

result = raised_to_a_power(x, y)

print(f"{x} raised to the power of {y} is equal to {result}") #I looked up how to print my variables into a worded statement



