pokaz = input().lower()
r = int(input())
c = int(input())
if r > 0 and c > 0:
    if pokaz == "premiere":
        print("%.2f" % (r*c*12.00))
    elif pokaz == "normal":
        print("%.2f" % (r*c*7.50))
    elif pokaz == "discount":
        print("%.2f" % (r*c*5.00))
    else:
        print("error")
else:
    print("error")
