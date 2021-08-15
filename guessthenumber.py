import random
num = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")
#print(str(num))
cont = 1
while cont < 7:
    print("You have "+str(7-cont)+" chances")
    print("Take a guess")
    guess = int(input())
    if guess < num:
        print("Your guess is too low")
    elif guess > num:
        print("Your guess is too high")
    else:
        print("Good job! You guessed my number in "+str(cont)+" guesses!")
        break
    
    cont += 1
    
    if cont == 7:
        print("Nope. The number I was thinking of was "+str(num))
