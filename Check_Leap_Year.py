 
year = 2023

def leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        
        return True

    else:
        
        return False

result = leap_year(year)

print(f"{year} is a leap year: {result}") #I found out how to make a sentence with a result on google
