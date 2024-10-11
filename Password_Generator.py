import random
import string
password=''
print('welcome to password generator')
lower=[random.choice(string.ascii_lowercase) for i in range(int(input('enter how many lowercase letters')))]
numbers=[random.choice(string.digits) for j in range(int(input('enter how many numbers')))]
symbol=[random.choice(string.punctuation) for k in range(int(input('enter how many symbols')))]
upper=[random.choice(string.ascii_uppercase) for l in range(int(input('Enter how many uppercase letters')))]
key=lower+numbers+symbol+upper
random.shuffle(key)
for i in key:
    password=password+i
print(f"The Random Password generated is {password}")