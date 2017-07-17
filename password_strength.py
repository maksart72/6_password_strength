import re
import getpass


def get_password_strength(password):
    strength = 0
    if re.search('[a-zа-я]', password) is not None:
        strength = strength + 1
    if re.search('[A-ZА-Я]', password) is not None:
        strength = strength + 1
    if re.search('[0-9]', password) is not None:
        strength = strength + 1
    if re.search('[^A-zА-я0-9]', password) is not None:
        strength = strength + 1
    pass_length = len(password) // 3
    if pass_length > 5:
        strength = strength + 6
    else:
        strength = strength + pass_length
    return str(strength)

if __name__ == '__main__':
    print('')
    userpassword = getpass.getpass('Enter your password:')
    print('The strength of your password is: ' + get_password_strength(userpassword))
    print('1 – Password is very weak..., 10 – Password is very strong! ')
