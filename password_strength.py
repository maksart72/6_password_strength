import re


def get_password_strength(password):
    strength = 0
    is_small = 1
    is_caps = 1
    is_number = 1
    is_symbol = 1
    is_length = 0
    if re.search('[a-zа-я]', password) is None:
        is_small = 0

    if re.search('[A-ZА-Я]', password) is None:
        is_caps = 0

    if re.search('[0-9]', password) is None:
        is_number = 0

    if re.search('[^A-zА-я0-9]', password) is None:
        is_symbol = 0

    pass_length = len(password) // 3
    if pass_length > 5:
        is_length = 6
    else:
        is_length = pass_length

    strength = is_caps + is_length + is_small + is_number + is_symbol
    return str(strength)


if __name__ == '__main__':
    print('')
    PASSWORD_IS = input('Enter your password:')
    if re.search(' ', PASSWORD_IS) is None:
        print('The strength of your password is: ' +
              get_password_strength(PASSWORD_IS))
        print('1 – Password is very weak..., 10 – Password is very strong! ')
    else:
        raise ValueError('Error! Space is permitted')
