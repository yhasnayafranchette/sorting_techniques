# A. ONE DIMENSIONAL ARRAY – Number Array
# PROBLEM #02: Create a program that will convert a decimal number (positive value) to its equivalent binary number.
# Use array for binary values

def decimal_to_binary(decimal_number):
    binary_values_array = []  

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_values_array.append(remainder)  
        decimal_number = decimal_number // 2  

    binary_values_array.reverse()

    return binary_values_array 

decimal_number = int(input("Enter a decimal number: ")) 
binary_values_array = decimal_to_binary(decimal_number)  

print("Binary equivalent:", end=" ")
for bit in binary_values_array:
    print(bit, end="")