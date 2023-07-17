minimum_value = 1
maximum_value = 100

divisible_by_7_and_8 = []

integer_list = [i for i in range(minimum_value, maximum_value+1) if i>0]

for integer in integer_list:
    if integer % 7 == 0 and integer % 8 == 0:
        divisible_by_7_and_8.append(integer)

print("Numbers divisible by 7 and 8: ", divisible_by_7_and_8)


lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

integer_list = [i for i in range(lower_limit, upper_limit+1)]

divisible_by_7_8 = [num for num in integer_list if num % 7 == 0 and num % 8 == 0]

print("The numbers that are divisible by 7 and 8 are: ", divisible_by_7_8)




string = "emp"

new_list = [f"{string}{num}" for num in list]
print(new_list)




num = int(input("Enter a number: "))
reverse = 0
temp = num
while temp > 0:
   
    rem = temp % 10
    reverse = (reverse * 10) + rem
    temp = temp // 10

if num == reverse:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")


#Recursive Version:
def is_palindrome(num):
    if num < 10:
        return True
    else:
        num_str = str(num)
        return num_str[0] == num_str[-1] and is_palindrome(int(num_str[1:-1]))


num = int(input("Enter a number: "))

if is_palindrome(num):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")








string = input("Enter a string: ")
first_char = string[0]
found_first_char = False
new_string = ""

for char in string:
    if char == first_char and not found_first_char:
        found_first_char = True
        new_string += char
    elif char == first_char and found_first_char:
        new_string += "$"
    else:
        new_string += char

print("Resulting string:", new_string)


import string

password = input("Enter a password: ")
valid_chars = string.ascii_letters + string.digits + string.punctuation

if len(password) < 8 or len(password) > 16:
    print("Password should be between 8 to 16 characters long")
if not any(char.islower() for char in password):
    print("Password should contain at least one lowercase alphabet")
if not any(char.isupper() for char in password):
    print("Password should contain at least one uppercase alphabet")
if not any(char.isdigit() for char in password):
    print("Password should contain at least one digit")
if not any(char in string.punctuation for char in password):
    print("Password should contain at least one special character")
if any(char not in valid_chars for char in password):
    print("Password contains invalid characters")

strength = 0
if any(char.islower() for char in password):
        strength += 1
if any(char.isupper() for char in password):
        strength += 1
if any(char.isdigit() for char in password):
        strength += 1
if any(char in string.punctuation for char in password):
        strength += 1

if strength == 4:
        print("Password strength is strong")
elif strength == 2 or strength == 3:
        print("Password strength is medium")
else:
        print("Password strength is poor")