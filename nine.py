a = int(input())
while not(-300 <= a <= 300 or 1000 <= a <= 1600):
    print("Invalid number")
    a = int(input())
print(f"The number is: {a}")
