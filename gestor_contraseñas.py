import random

from string import digits
from string import punctuation
from string import ascii_letters

len = int(input("Enter the password lenght: "))

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols) for i in range(len))

print(password)