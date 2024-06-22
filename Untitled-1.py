nums_str = input("Please input a list of numbers separated by commas: ")
nums_list = nums_str.split(',')
unique_numbers = []
for num in nums_list:
    if nums_list.count(num) == 1:
        unique_numbers.append(num)
if unique_numbers:
    print("Numbers that occur only once:", unique_numbers)
else:
    print("No numbers repeated only once")
