from random import randint

dice_sides = input("Dice sides are: ")
dice_sides = int(dice_sides)

dice1 = randint(1, dice_sides)
print("The dice rolled(first):")
print(dice1)

dice2 = randint(1, dice_sides)
print("The dice rolled(second):")
print(dice2)

dice3 = randint(1, dice_sides)
print("The dice rolled(third):")
print(dice3)

dice4 = randint(1, dice_sides)
print("The dice rolled(fourth):")
print(dice4)

sum = dice1 + dice2 + dice3 + dice4
print("The sum is:")
print(sum)