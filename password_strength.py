import re
password = input('Введите пароль:')
strength = 0
p1 = 1 #прописные
p2 = 1 #заглавные
p3 = 1 #цифры
p4 = 1 #символы
p5 = 0 #количество символов

if re.search('[a-zа-я]', password) == None:
    p1 = 0
    
if re.search('[A-ZА-Я]', password) == None:
        p2 = 0

if re.search('[0-9]', password) == None:
        p3 = 0

if re.search('[^A-zА-я0-9]', password) == None:
        p4 = 0
    
if re.search(' ',password) != None:
    raise ValueError('Пробел запрещен!')
 
passlen = len(password) // 3
if passlen > 5:
    p5 = 6
else: 
    p5 = passlen

def get_password_strength(p1,p2,p3,p4,p5):
    strength = p1+p2+p3+p4+p5
    return(str(strength))

if __name__ == '__main__':
             
    print('Оценка Вашего пароля: '+ get_password_strength(p1,p2,p3,p4,p5))
    print('1 – очень слабый пароль, 10 – очень крутой')