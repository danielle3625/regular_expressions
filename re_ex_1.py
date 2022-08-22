import re

#Assign opened file to variable
#Don't want to keep typing file name
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1625412.txt"
hand = open(name)

num_list = []

#Iterate through file, find digits
for line in hand:
    line = line.strip()
    num = re.findall('[0-9]+', line)
    if len(num) >= 1:
        num_list.append(num)

count_list = []

#Remove embedded lists, for one master list
#Could not sum list type
for num in num_list:
    for item in num:
        count_list.append(int(item))

sum = 0

#Totals the combined items in the list
for num in count_list:
    sum += num

print(sum)
print(len(count_list))