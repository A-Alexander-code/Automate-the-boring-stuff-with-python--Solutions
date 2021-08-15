digits = []
positiveDigits = 0
negativeDigits = 0

for i in range(1,11):
    print('Enter the digit ',i,'of 10')
    number = int(input())
    digits.append(number)
    if number >= 0:
        positiveDigits += 1
    else:
        negativeDigits += 1

#print(digits)
tryAgain = True
while tryAgain == True:
    question = input('Do you want know how many positive (p) or negative (n) are? \n')
    if question == 'p':
        print('There are ',str(positiveDigits),'positive numbers')
        tryAgain = False
    elif question == 'n':
        print('There are ',str(negativeDigits),'negative numbers')
        tryAgain = False
    else:
        tryAgain = True