# B. One Dimensional Array: Array of Characters
# PROBLEM #04: Create a program that will check if a given word is a palindrome or not a palindrome.

string = input("Enter a word:")

def isPalindrome(string):
    if (string == string[::-1]):
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"

print(isPalindrome(string))