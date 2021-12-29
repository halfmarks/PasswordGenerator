import random

password = []
uppercaseLetter1 = chr(random.randint(65, 90)) # number in ranfint function correlate with an ASCII key
uppercaseLetter2 = chr(random.randint(65, 90))
password.append(uppercaseLetter1)
password.append(uppercaseLetter2)

lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
password.append(lowercaseLetter1)
password.append(lowercaseLetter2)

number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))
password.append(number1)
password.append(number2)

punctuation1 = chr(random.randint(33, 47))
punctuation2 = chr(random.randint(58, 64))
password.append(punctuation1)
password.append(punctuation2)

# password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + number2 + punctuation1 + punctuation2


random.shuffle(password)
for digit in password:
    print(digit, end="")

