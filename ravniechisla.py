def isInteger(userInput):
    try:
        int(userInput)
    except ValueError:
        return False
    return True
    
n = input()
flag = False 
if isInteger(n): 
    n = int(n)
    couplesSum = []
    for i in range(n):
        a = input()
        while not(isInteger(a)):
            print("Неверный ввод")
            a = input()
        b = input()
        while not(isInteger(b)):
            print("Неверный ввод")
            b = input()
        couplesSum.append(int(a)+int(b))
    maxValue = []
    for i in range(1, n):
        if couplesSum[i] != couplesSum[i-1]:
            maxValue.append(couplesSum[i-1] - couplesSum[i])
    if len(maxValue) == 0:
        print(f'Yes, value = {couplesSum[0]}')
    else:
        print(f'No, maxdiff = {max(maxValue)}')
else:
    print("ERROR")
            
