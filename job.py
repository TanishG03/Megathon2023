conscientiousness = float(input())
neuroticism = float(input())
agreeableness = float(input())
extroversion = float(input())
openness = float(input())

def agree():
    if agreeableness >= 2 and agreeableness <= 4:
        return 0
    elif agreeableness > 4 and agreeableness <= 5:  # too high
        return 2
    else:
        return 1

def extro():
    if extroversion >= 3 and extroversion <= 5:
        return 0
    else:
        return 1

def open():
    if openness >= 3 and openness <= 5:
        return 0
    else:
        return 1

if conscientiousness <= 5 and conscientiousness >= 2:  # very high/ med C
    if neuroticism <= 3 and neuroticism >= 0:  # very low/med
        if (agree() == 0 and extro() == 0):
            print("ideal salesperson")
        elif (agree() != 0 and extro() == 0 and open() == 0):
            print("salesperson")
        elif (agree() == 1 and open() == 1):
            print("not suitable")
        elif (agree() == 2 and extro() == 1):
            print("not suitable")
        elif (agree() == 2 and extro() == 0 and open() == 1):
            print("sales")
        elif (agree() == 0 and extro() == 1):
            print("tech person")
        elif (agree() == 1 and extro() == 1 and open() == 0):
            print("ideal tech person")
    else:  # very high
        if (agree() == 0 and extro() == 0):
            print("salesperson")
        elif (agree() == 1 and extro() == 1 and open() == 0):
            print("tech person")
        else:
            print("not suitable")
else:  # very low C
    if neuroticism <= 3 and neuroticism >= 0:  # very low/med
        if (agree() == 0 and extro() == 0):
            print("ideal salesperson")
        elif (agree() != 0 and extro() == 0 and open() == 0):
            print("salesperson")
        elif (agree() == 1 and open() == 1):
            print("not suitable")
        elif (agree() == 2 and extro() == 1):
            print("not suitable")
        elif (agree() == 2 and extro() == 0 and open() == 1):
            print("sales")
        # elif (agree() == 0 and extro() == 1):
        #     print("tech person")
        # elif (agree() == 1 and extro() == 1 and open() == 0):
        #     print("ideal tech person")
    else:  # very high
        # if (agree() == 0 and extro() == 0):
        #     print("ideal salesperson")
        # else:
            # print("not suitable")
        print("not suitable")