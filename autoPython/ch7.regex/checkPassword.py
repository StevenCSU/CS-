# checkPassword.py - Use regex to ensure that the password is safe


import re


def checkPassword(password):
    # check digits
    if len(password) < 8:
        print('Your password must longer than 8.')
        return False
    # check Upper case
    upperRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    digitRegex = re.compile(r'\d+')
    if upperRegex.search(password) is None:
        print('Your password must have uppercase letter.')
        return False

    # check Lower case
    if lowerRegex.search(password) is None:
        print('Your password must have lowercase letter.')
        return False

    # check if there is number
    if lowerRegex.search(password) is None:
        print('Your password must have digit.')
        return False

    print('Great! Your password is safe enough!')

# test
s = ['Woailajsfl1854', 'woailajsfl1854',
     'jgjgla', 'waolaslghlaj', 'WOGHLG199']
for i in range(len(s)):
    print('The safety of ' + s[i] + ' is ')
    checkPassword(s[i])
# s = 'Woailajsfl1854'
# checkPassword(s)

# s1 = 'woailajsfl1854'
# checkPassword(s1)

# s2 = 'jgjgla'
# checkPassword(s2)

# s3 = 'waolaslghlaj'
# checkPassword(s3)

# s4 = 'WOGHLG199'
# checkPassword(s4)
