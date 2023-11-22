budget = int(input())
season = input().lower()
fishmanCounter = int(input())
if season == "spring" or season == "summer":
    if 4 <= fishmanCounter <= 6:
        if fishmanCounter % 2 == 0:
            if budget - (3000 * 0.9 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.9 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.9 * 0.95))))
        else:
            if budget - (3000 * 0.9) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.9)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.9))))
    if 7 <= fishmanCounter <= 11:
        if fishmanCounter % 2 == 0:
            if budget - (3000 * 0.85 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.85 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.85 * 0.95))))
        else:
            if budget - (3000 * 0.85) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.85)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.85))))
    if 12 <= fishmanCounter <= 18:
        if fishmanCounter % 2 == 0:
            if budget - (3000 * 0.75 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.75 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.75 * 0.95))))
        else:
            if budget - (3000 * 0.75) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (3000 * 0.75)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (3000 * 0.75))))
elif season == "autumn":
    if 4 <= fishmanCounter <= 6:
        if fishmanCounter % 2 == 0:
            if budget - (4200 * 0.9 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.9 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.9 * 0.95))))
        else:
            if budget - (4200 * 0.9) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.9)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.9))))
    if 7 <= fishmanCounter <= 11:
        if fishmanCounter % 2 == 0:
            if budget - (4200 * 0.85 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.85 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.85 * 0.95))))
        else:
            if budget - (4200 * 0.85) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.85)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.85))))
    if 12 <= fishmanCounter <= 18:
        if fishmanCounter % 2 == 0:
            if budget - (4200 * 0.75 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.75 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.75 * 0.95))))
        else:
            if budget - (4200 * 0.75) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (4200 * 0.75)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (4200 * 0.75))))
elif season == "winter":
    if 4 <= fishmanCounter <= 6:
        if fishmanCounter % 2 == 0:
            if budget - (2600 * 0.9 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.9 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.9 * 0.95))))
        else:
            if budget - (2600 * 0.9) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.9)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.9))))
    if 7 <= fishmanCounter <= 11:
        if fishmanCounter % 2 == 0:
            if budget - (2600 * 0.85 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.85 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.85 * 0.95))))
        else:
            if budget - (2600 * 0.85) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.85)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.85))))
    if 12 <= fishmanCounter <= 18:
        if fishmanCounter % 2 == 0:
            if budget - (2600 * 0.75 * 0.95) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.75 * 0.95)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.75 * 0.95))))
        else:
            if budget - (2600 * 0.75) >= 0:
                print("Yes! You have %.2f rubles left." % (budget - (2600 * 0.75)))
            else:
                print("Not enough money! You need %.2f rubles" % (abs(budget - (2600 * 0.75))))
else:
    print("error")
