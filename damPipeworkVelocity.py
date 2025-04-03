print("Solve for...")
goal = input().lower()


if goal == "vel":
    loss = 1

    print("Calculate diff?")
    calcDiff = input().lower()
    if calcDiff == "yes":
        print("Input distOne and distTwo")
        distOne = float(input())
        distTwo = float(input())
        diff = distOne - distTwo
        print(diff)
    else:
        print("Input diff...")
        diff = float(input())

    print("Number of losses...")
    noLosses = int(input())

    print("State loss values")
    for x in range (noLosses):
        loss += float(input())

    vel = ((diff * 19.6) /loss) ** 0.5
    print(vel)


if goal == "diff":
    loss = 1
    
    print("Enter flow velocity")
    vel = float(input())

    print("Number of losses...")
    noLosses = int(input())

    print("State loss values")
    for x in range (noLosses):
        loss += float(input())

    diff = ((vel ** 2) / 19.6) * loss
    print(diff)

    print()
    print("Is there a known distOne?")
    yesOr = input().lower()
    print(yesOr)

    if yesOr == "yes":
        print("Enter value")
        distOne = float(input())
        distTwo = distOne - diff
        print(distTwo)


if goal == "loss":
    print("Input velocity...")
    vel = float(input())

    print("Calculate diff?")
    calcDiff = input().lower()
    if calcDiff == "yes":
        print("Input distOne and distTwo")
        distOne = float(input())
        distTwo = float(input())
        diff = distOne - distTwo
        print(diff)
    else:
        print("Input diff...")
        diff = float(input())
    
    loss = (diff * (19.6 / (vel ** 2))) - 1
    print("loss =" + str(loss))

