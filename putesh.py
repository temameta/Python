wallet = 0
value = 0
place = ""
state = "idle"
inputString = str(input())
while inputString.lower() != "end":
    if state == "idle":
        if not(inputString.isdigit()):
            place = inputString
        elif inputString.isdigit() and place == "":
            print("Страна не введена")
        elif inputString.isdigit() and place != "":
            value = int(inputString)
            state = "going"
            inputString = 0
    if state == "going":
        if str(inputString).isdigit():
            wallet += int(inputString)
        else:
            print("error")
        if wallet - value >= 0:
            print(f'Going to {place}!')
            value = 0
            state = "idle"
    inputString = str(input())
