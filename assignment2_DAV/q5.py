
def is_valid_password(password):
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    
    if len(password) < 8 or len(password) > 16:
         
        print("Password must be between 8 and 16 characters. Hence, your password is invalid, try again!")
        return False
        
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if not has_lowercase:
        print("Password must contain at least one lowercase alphabet.")
        return False
    if not has_uppercase:
        print("Password must contain at least one uppercase alphabet.")
        return False
    if not has_digit:
        print("Password must contain at least one digit.")
        return False
    if not has_special:
        print("Password must contain at least one special character.")
        return False
    
    return True


def evaluate_password_strength(password):
    strength = 0
    
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    if has_lowercase:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1



    
    if strength == 4:
        print("Password strength is strong.")
    elif strength == 2 or strength == 3:
        print("Password strength is medium.")
    elif strength == 0:
        print("Password doesn't satisfy any conditions")
    else:
        print("Password strength is weak.")


def try_again():
    while True:
        response = input("Do you want to try again? (y/n): ")
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' or 'n'.")
            continue


while True:
    password = input("Enter your password: ")
    evaluate_password_strength(password)
    if not is_valid_password(password):
        if not try_again():
            break
        continue

    password_strength = evaluate_password_strength(password)
    if password_strength == "weak":
        if not try_again():
            break
        continue
    break
