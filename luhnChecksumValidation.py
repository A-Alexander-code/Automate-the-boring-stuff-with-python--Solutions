digit = input("Enter a new password equal or less than 10 numbers: ")

def doubleDigitValue(number):
    doubleDigit = number*2
    if doubleDigit > 10:
        sum = 1 + (doubleDigit%10)
    else:
        sum = doubleDigit
    return sum

if len(digit) > 10:
    print("Error. The password is too long")
    digit = input("Enter a new password equal or less than 10 numbers: ")

oddnumber = []
evennumber = []

for i in range(len(digit)):
    if i % 2 == 0:
        evennumber.append(i)
    else:
        oddnumber.append(i)

#print('Odd numbers are: ',oddnumber)
#print('Even numbers are:',evennumber)

holeDigit = []
for i in digit:
    holeDigit.append(int(i))
#print(holeDigit)

checksum1 = 0
for i in evennumber:
    elem1 = holeDigit[i]
    checksum1 += elem1

#print(checksum1)

checksum2 = 0
for i in oddnumber:
    checksum2 +=  doubleDigitValue(holeDigit[i])

#print(checksum2)

Checksum = checksum1 + checksum2
errDigit = Checksum%10
#print(str(errDigit))
print('Checksum = ',Checksum)

if Checksum % 10 == 0:
    print('Checksum is divisible by 10. Valid')
else:
    print('Checksum is not divisible by 10. Invalid')