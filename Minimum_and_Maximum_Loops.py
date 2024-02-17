
Max_Min_list = [70, 7, 90, 102, 40, 80, 55] #Using the same list for every function 

#FOR LOOP MAXIMUM:

def for_loop_max_min(Max_Min_list):

    max_value = Max_Min_list[0]

    for number in Max_Min_list:

        if number > max_value:

            max_value = number 

    return max_value

result = for_loop_max_min(Max_Min_list)

print(f"Using a 'for loop' the max value is {result}") #I found out how to make a sentence with a result on google

#FOR LOOP MINIMUM:

def for_loop_max_min(Max_Min_list):

    min_value = Max_Min_list[0]

    for number in Max_Min_list:

        if number < min_value:

            min_value = number

    return min_value 

result = for_loop_max_min(Max_Min_list)

print(f"Using a 'for loop' the min value is {result}")

#WHILE LOOP MAXIMUM:

def while_loop_max_min(Max_Min_List):

    max_value = Max_Min_List[0]

    i = 1 

    while i < len(Max_Min_List): #Had some help with this line 

        number = Max_Min_list[i] #This is just changing the variable i to number to match with the for loops

        if number > max_value:

            max_value = number 

        i += 1

    return max_value 

result = while_loop_max_min(Max_Min_list)

print(f"Using a 'while loop' the max value is {result}")

#WHILE LOOP MINIMUM:

def while_loop_max_min(Max_Min_list):
    
    min_value = Max_Min_list[0]

    i = 1

    while i < len(Max_Min_list):
        
        number = Max_Min_list[i]

        if number < min_value:

            min_value = number 

        i += 1

    return min_value

result = while_loop_max_min(Max_Min_list)

print(f"Using a 'while loop' the min value is {result}")
