from random import randint

dice_sides = input("Dice sides are: ")
dice_sides = int(dice_sides)

player1 = input("Player1 name: ")
player2 = input("Player2 name: ")

player1_dice = randint(1, dice_sides)
print(player1 + " rolls " + str(player1_dice))

player2_dice = randint(1, dice_sides)
print(player2 + " rolls " + str(player2_dice))

if player1_dice == player2_dice:
	print("No one win!")
elif player1_dice > player2_dice:
	print(player1 +" win!")
else:
	print(player2 +" win!")
	