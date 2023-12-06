dlina = int(input())
shirina = int(input())


if 1 <= dlina <= 1000 and 1 <= shirina <= 1000:
    size = dlina * shirina

    while True:
        inputs = input()
        try:
            int(inputs)
        except ValueError:
            if inputs.lower() == "stop":
                break
            continue
        if int(inputs) < 0:
            print("Invalid number")
            continue
        size -= int(inputs)
        if size - int(inputs) < 0:
            break
    if size > 0:
        print(f'{size} pieces are left.')
    else:
        print(f'No more cake left! You need {abs(size)} pieces more.')
else:
    print("error")
