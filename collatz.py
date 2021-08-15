import sys

def collatz(number):
    if number%2 == 0:
        ans1 = number//2
        print(str(ans1))
    elif number%2 == 1:
        ans2 = 3*number + 1
        print(str(ans2))

tryagain = True
fnum = " "

while fnum != 1:
    fnum = int(input("Enter a number: "))
    collatz(fnum)
