fruit = input().lower()
day = input().lower()
kg = float(input())
if kg > 0:
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
        if fruit == "banana":
            print("%.2f" % (kg * 2.50))
        elif fruit == "apple":
            print("%.2f" % (kg * 1.20))
        elif fruit == "orange":
            print("%.2f" % (kg * 0.85))
        elif fruit == "grapefruit":
            print("%.2f" % (kg * 1.45))
        elif fruit == "kiwi":
            print("%.2f" % (kg * 2.70))
        elif fruit == "pineapple":
            print("%.2f" % (kg * 5.50))
        elif fruit == "grapes":
            print("%.2f" % (kg * 3.85))
        else:
            print("invalid fruit")
    elif day == "sunday" or day == "saturday":
        if fruit == "banana":
            print("%.2f" % (kg * 2.70))
        elif fruit == "apple":
            print("%.2f" % (kg * 1.25))
        elif fruit == "orange":
            print("%.2f" % (kg * 0.90))
        elif fruit == "grapefruit":
            print("%.2f" % (kg * 1.60))
        elif fruit == "kiwi":
            print("%.2f" % (kg * 3.00))
        elif fruit == "pineapple":
            print("%.2f" % (kg * 5.60))
        elif fruit == "grapes":
            print("%.2f" % (kg * 4.20))
        else:
            print("invalid fruit")
    else:
        print("invalid day")
else:
    print("error")
