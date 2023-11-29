n = int(input())
if n > 0:
    max = int(input())
    for i in range(n-1):
        a = int(input())
        if a > max:
            max = a
    print(max)
else:
    print("error")
