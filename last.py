inputString = input()
sumOfPrime = 0
sumOfNonPrime = 0
while inputString.lower() != "stop":
    try:
        num = int(inputString)
        d=0
        if num >= 0:
            prime = True
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    d+=1
            if d<=0:
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
