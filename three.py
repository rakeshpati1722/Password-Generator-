import random
def generateStrongPassword():
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsLow = "abcdefghijklmnopqrstuvwxyz"
    charsNumber = "0123456789"
    charsSpecial = "!@#$%&*()[]{}"
    password = ''
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    return password

#function to create a weak password from a default list
def generateWeakPassword():
    defaultPass = ['0123456','123456','abcdef','qawseedrf']
    return random.choice(defaultPass)

print('Generating password 1',generateStrongPassword())
print('Generating password 2',generateStrongPassword())
print('Generating password 3',generateStrongPassword())
print('Generating password 4',generateStrongPassword())


answer = input('Do you want strong or weak password?')
if answer == 'strong':
    print('Your strong password is ',generateStrongPassword())
elif answer == 'weak':
    print('Your weak password is ',generateWeakPassword())
else:
    print('ERROR, you have typed a wrong word, please try again typing "strong" or "weak"')
    
    
    
#2nd type
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)
