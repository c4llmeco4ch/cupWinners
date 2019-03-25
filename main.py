import random
chelseaPoints = 0
pointsForCup = 80

for game in range(38):
    chelseaScore = random.randint(0,5)
    oppScore = random.randint(0,5)

    if chelseaPoints > oppScore:
        chelseaPoints += 3
    elif chelseaScore == oppScore:
        chelseaPoints += 1

if chelseaPoints >= pointsForCup:
    print("Chelsea has won the cup!")

else:
    print("Better luck next year, Chelsea...")