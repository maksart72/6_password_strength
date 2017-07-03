import re
password = input('Please enter your password:')

def get_password_strength(password):
    strength = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    
    passlen = len(password) // 3
    if passlen > 5:
        p6 = 5
    else: 
        p6 = passlen

    strength = p1+p2+p3+p4+p5+p6
    return(str(strength))

if __name__ == '__main__':
    if re.search('[a-z]', password) = None:
        print('None')
            
        print('Your password strength is '+ get_password_strength(password))
