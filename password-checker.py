MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

PASSWORDS = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage']

HAS_SPECIAL_CHAR = False
HAS_NUMBER = False
HAS_7_CHARS = False

# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL_CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions

for password in PASSWORDS:
    if len(password) >= MIN_CHARACTERS:
        HAS_7_CHARS = True
    for char in SPECIAL_CHARS:
        special_char_in_password = password.count(char)
        if special_char_in_password > 0:
            HAS_SPECIAL_CHAR = True
    for number in NUMBERS:
        numbers_in_password = password.count(str(number))
        if numbers_in_password > 0:
            HAS_NUMBER = True
    if HAS_7_CHARS and HAS_SPECIAL_CHAR and HAS_NUMBER:
        print(f"Great! This password is fully valid: {password}")
        print("")
    else:
        print(f"This password does not meet all the requirements: {password}")
        print("")