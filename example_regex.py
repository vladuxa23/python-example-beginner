import pyperclip, re
li = ['aSWe4ew1', 'aaaaaaaa', '11111111', 'Qwertyui870']

for val in li:
    if re.match(r'([a-z][A-Z]\w{1,})', val) and len(val)>= 7:

        print ('yes')
    else:
        print ('no')


#Напишите функцию, которая использует регулярные выражения для
#проверки того, что переданная ей строка представляет собой сильный пароль.
#Сильными считаются пароли, которые состоят по крайней мере
#из 8 символов, содержат символы в ВЕРХНИХ и нижних регистрах и
#и включают по меньшей мер одну цифру.
def strongPassword():

    testPassword = str(input())
    testRegex = re.compile(r'([A-Za-z0-9@#$%^&+=]{8,})')
    test = testRegex.search(password)
    if (test):
        print('Идеальный пароль')
    else:
        print('Плохой пароль')

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

text = str(pyperclip.paste())

def checkPhone(text):

    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(groups[0])


    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер офмена:')
        print('\n'.join(matches))
    else:
        print('Ничего не обнаружено')

#text = str(pyperclip.paste())


def checkEmail(text):

    matches = []
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4}){1,2}
        )''', re.VERBOSE)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер офмена:')
        print('\n'.join(matches))
    else:
        print('Ничего не обнаружено')
        #! python3
        # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.


def checkPhone(text):

    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(groups[0])


    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер офмена:')
        print('\n'.join(matches))
    else:
        print('Ничего не обнаружено')

def checkEmail(text):

    matches = []
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4}){1,2}
        )''', re.VERBOSE)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер офмена:')
        print('\n'.join(matches))
    else:
        print('Ничего не обнаружено')





