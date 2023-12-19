inputString = input()
sumOfPrime = 0
sumOfNonPrime = 0
while inputString.lower() != "stop":
    try:
        num = int(inputString)
        flag = False
    
        if num >= 0:
            for i in range(2, num):
                if num % i == 0:
                    flag == True
                    break
            if not(flag):
                sumOfPrime += num
            else:
                sumOfNonPrime += num
        else:
            print("Number is negative.")
    except ValueError:
        print("ERROR")
    inputString = input()
print(f'Sum of all prime numbers is: {sumOfPrime}')
print(f'Sum of all non prime numbers is: {sumOfNonPrime}')
