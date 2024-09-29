# A. ONE DIMENSIONAL ARRAY – Number Array
# PROBLEM #01: Create a program that will ask the user to enter 10 numbers and display it in ascending order.

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    num = int(input())
    numbers.append(num)

numbers.sort()

print("\nElement value of array in ascending order")
for number in numbers:
    print(number, end=" ") 


