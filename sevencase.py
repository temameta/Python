degrees = int(input())
time = input().lower()
if time == "morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 25 <= degrees <= 42:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    else:
        print("invalid degrees")
elif time == "afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 25 <= degrees <= 42:
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    else:
        print("invalid degrees")
elif time == "evening":
    if 10 <= degrees <= 18:
        outfit = "Shirtt"
        shoes = "Moccasins"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    elif 25 <= degrees <= 42:
        outfit = "Shirt"
        shoes = "Moccasins"
        print("It's %d degrees, get your %s and %s" %(degrees, outfit, shoes))
    else:
        print("invalid degrees")
else:
    print("invalid time")
