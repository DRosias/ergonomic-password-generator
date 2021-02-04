import secrets
import os

# digit lists
digits = ['!', '@', '#', '$', '%', '+', '=', '*', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
          '6', '7', '8', '9']
cap_digits = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
lower_digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
num_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
left_digits = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', '1', '2', '3', '4', '5', '!',
               '@', '#', '$', '%', 'Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V', 'B']
right_digits = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'n', 'm', '6', '7', '8', '9', '0', '+', '=', '*', '?', 'Y', 'U', 'O', 'P', 'H', 'J', 'K', 'L', 'N', 'M']
left_cap_digits = ['Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V', 'B']
right_cap_digits = ['Y', 'U', 'O', 'P', 'H', 'J', 'K', 'L', 'N', 'M']
left_lower_digits = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
right_lower_digits = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'n', 'm']
left_num_digits = ['1', '2', '3', '4', '5']
right_num_digits = ['6', '7', '8', '9', '0']
left_sym_digits = ['!', '@', '#', '$', '%']
right_sym_digits = ['+', '=', '*', '?']
left_digits_nosymbol = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', '1', '2', '3', '4',
                        '5',
                        'Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V', 'B']
right_digits_nosymbol = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'n', 'm', '6', '7', '8', '9', '0', 'Y', 'U',
                         'O', 'P', 'H', 'J', 'K', 'L', 'N', 'M']
left_lower_digits_nosymbol = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', '1', '2', '3',
                              '4', '5']
right_lower_digits_nosymbol = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'n', 'm', '6', '7', '8', '9', '0']


def generate_digit(digits_generated, digits_left, digits_right):
    if digits_generated % 2 == 0:  # check hand
        return secrets.choice(digits_left)
    else:
        return secrets.choice(digits_right)

# loop setup
loop_variable = 1
while loop_variable == 1:

    # starting constants
    length = 8  # can be changed without breaking anything
    digits_generated = 0
    password_final = ''
    starting_hand = ['l', 'r']

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # choose starting hand
    starting_hand = secrets.choice(starting_hand)

    # first letter
    if starting_hand == 'l':
        password_final += secrets.choice(left_cap_digits)
    else:
        digits_generated += 1  # offset for rest of digits to use correct hand
        length += 1  # offset for rest of digits to use correct hand
        password_final += secrets.choice(right_cap_digits)

    digits_generated += 1  # counting first letter as generated

    # middle letters
    length = length - 3  # offset for last 3

    while digits_generated < length: 
        if password_final.isupper(): # after first lowercase, all lowercase thereafter
            password_final += generate_digit(digits_generated, left_digits_nosymbol, right_digits_nosymbol)
        else:
            password_final += generate_digit(digits_generated, left_lower_digits_nosymbol, right_lower_digits_nosymbol)
        digits_generated += 1

    # third to last letter is a guaranteed lowercase
    password_final += generate_digit(digits_generated, left_lower_digits, right_lower_digits)
    digits_generated += 1

    # second to last digit is a number
    password_final += generate_digit(digits_generated, left_num_digits, right_num_digits)
    digits_generated += 1

    # last digit is a symbol
    password_final += generate_digit(digits_generated, left_sym_digits, right_sym_digits)
    digits_generated += 1
    
    "".join(password_final)
    
    print(password_final)

    print("")

    input("Press Enter for a new password")