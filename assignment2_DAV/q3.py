# Iterative Version
num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)

is_palindrome = True
start = 0
end = length - 1

if length == 1:
    print("The number is a palindrome.")
else:
    while start < end and is_palindrome:
        if num_str[start] != num_str[end]:
            is_palindrome = False
        start += 1
        end -= 1

    if is_palindrome:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

#------------------------------------------------------------------------------------------------
# Recursive Version

def is_palindrome(num_str, start, end):
    if start >= end:
        return True
    if num_str[start] != num_str[end]:
        return False
    return is_palindrome(num_str, start+1, end-1)

num = int(input("Enter a number: "))
num_str = str(num)
length = len(num_str)

if length == 1:
    print("The number is a palindrome.")
else:
    if is_palindrome(num_str, 0, length-1):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
        
#------------------------------------------------------------------------------------------------

