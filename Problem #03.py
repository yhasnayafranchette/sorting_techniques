# A. ONE DIMENSIONAL ARRAY – Number Array
# PROBLEM #03: Create a program that will ask the user to enter 10 numbers and display the 1st and 2nd to highest number and 1st and 2nd to the lowest number.
# Don’t use array sorting

def find_highest(numbers):
    highest = second_highest = numbers[0]
    lowest = second_lowest = numbers[0]

    for num in numbers:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num
        
        if num < lowest:
            second_lowest = lowest
            lowest = num
        elif num < second_lowest and num != lowest:
            second_lowest = num

    return highest, second_highest, lowest, second_lowest

numbers = []

print("Enter ten numbers:")
for i in range(10):
    num = int(input()) 
    numbers.append(num)

highest, second_highest, lowest, second_lowest = find_highest(numbers)

print(f"1st highest number: {highest}")
print(f"2nd highest number: {second_highest}")
print(f"1st lowest number: {lowest}")
print(f"2nd lowest number: {second_lowest}")