# 1 create a list: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9

# 2 convert a list to a set to delete duplicates

# 3 calculate the sum of the numbers using a list

# 4 calculate the sum of the numbers using a set

# 5 create a dictionary to store the statistics
# only numbers, total sum list, total sum set, identify the maximum value and minimum value

# 8 print the statistics


# 1
numbersList = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]
print("This is my list: ", numbersList)

# 2
numberSet = set(numbersList)
print("This is my set: ", numberSet)

# 3
sum_of_numbersList = sum(numbersList)
print("The sum of numbers in the list is:", sum_of_numbersList)

# 4
sum_of_numberSet = sum(numberSet)
print("The sum of numbers in the set is:", sum_of_numberSet)

# 5
maximum_value = max(numberSet)
minimum_value = min(numberSet)
dictionary = {"unique numbers": len(numberSet),
              "sum of list": sum_of_numbersList,
              "sum of set": sum_of_numberSet,
              "maximum value": maximum_value,
              "minimum value": minimum_value}

print("This is my dictionary:", dictionary)


