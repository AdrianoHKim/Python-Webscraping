import re

# Creating a function to find the sum of numbers from a text
def extract_and_sum_num(text):
    # Regular expression to match numbers (one or more digits)
    pattern = r'[0-9]+'

    # Finding all matches of the pattern in the text
    num_as_str = re.findall(pattern, text)

    # Convert the matched numbers from strings to integers and sum them
    total_sum = sum(map(int, num_as_str))

    return total_sum

# Reading the data
with open('find_number.txt', 'r') as file:
    data = file.read()

# Calling the function to extract and sum numbers
result = extract_and_sum_num(data)

# Print the result
print("The sum of the numbers in the actual data is:", result)
