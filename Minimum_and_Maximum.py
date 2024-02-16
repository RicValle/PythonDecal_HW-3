

integer_list = [9, 7, 5, 8, 10, 11, 20, 3]

def find_min_max(integer_list):

    min_value = max_value = integer_list[0]

    for number in integer_list:

        if number < min_value:

            min_value = number

        elif number > max_value:

            max_value = number

    return min_value, max_value

result = find_min_max(integer_list)

print(f"Minimum and Maximum Values: {result}") #I found out how to make a sentence with a result on google
