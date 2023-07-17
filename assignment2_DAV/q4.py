# string = input("Enter a string: ")

# if len(string) <= 1:
#     print(string)
# else:
#     freq = {}
#     for char in string:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     if freq[string[0]] > 1:
#         new_string = string[0]
#         for i in range(1, len(string)):
#             if string[i] == string[0]:
#                 new_string += '$'
#             else:
#                 new_string += string[i]
#         print(new_string)
#     else:
#         print(string)
 
string= (input('ENTER'))
ns= string[0]

for char in string[1:] :
    if char == string[0]:
     ns= ns+'$'
else :
     ns= ns+ char

print( 'og' , ns)