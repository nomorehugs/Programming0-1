from random import randint

dice_sides = input("Dice sides are: ")
dice_sides = int(dice_sides)

dice = randint(1, dice_sides)

print("The dice rolled:")
print(dice)
