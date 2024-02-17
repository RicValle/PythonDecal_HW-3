
word_input = "PythonDecal"

def number_of_vowels(word_input):

    original_vowels = "AEIOUaeiou"

    count = 0 

    for number_of_vowels in word_input:

        if number_of_vowels in original_vowels:

            count += 1 

    return count 

result = number_of_vowels(word_input)

print(f"The amount of vowels in {word_input} is {result}") #I found out how to make a sentence with a result on google