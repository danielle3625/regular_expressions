# This is an attempt to accomplish the same end result as reg_ex_1 but with less code
import re

# In reg_ex_1, I prompted name from input and provided allowance if no input entered
# This time, I'm assigning the handle to the open file from start (shorter code)

num_list = []

with open('regex_sum_1625412.txt') as handle:
    num = re.findall('[0-9]+', handle.read())
    num_list.append(num)

# Shorten the code to flatten a nested list in one line of code
# Use a generator!
count_list = [num for sublist in num_list for num in sublist]

#Shorten the code to sum the list in one line
print(sum(int(num) for num in count_list))
