n = int(input())
if n > 0:
    min = int(input())
    for i in range(n-1):
        a = int(input())
        if a < min:
            min = a
        print(min)
else:
    print("error")
