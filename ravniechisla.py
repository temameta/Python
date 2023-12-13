def isInteger(userInput):
    try:
        userInput = int(userInput)
    except ValueError:
        return False
    return True
    
n = input()
flag = True 
if isInteger(n): 
    n = int(n)
    couples = []
    a = input()
    b = input()
    for i in range(n*2):
        while not(isInteger(a)):
            print("Неверный ввод")
            a = int(input())
        while not(isInteger(b)):
            print("Неверный ввод")
            b = int(input())
        
        couples[i] = a
    for i in range(1, n):
        if a[i] < 
        
            
