from random import randint

player1 = input("Player1 name: ")
player2 = input("Player2 name: ")

player1_result = 101
player2_result = 101

while True:
    
    player1_rolls = 0
    player2_rolls = 0
    player1_roll_sum = 0
    player2_roll_sum = 0

    while player1_rolls < 5:
        player1_dice = randint(1, 6)
        print(player1 + " is rolling(" + str(player1_rolls+1) + "): " + str(player1_dice))
        player1_roll_sum += player1_dice
        player1_rolls += 1
    print("The sum of that turn is: " + str(player1_roll_sum))
    if player1_result > 0:
        player1_result -= player1_roll_sum
    elif player1_result < 0:
        player1_result += player1_roll_sum
    print("The result after that turn is: " + str(player1_result) + " for " + player1)
	
    if player1_result == 0:
        break	
		
    while player2_rolls < 5:
        player2_dice = randint(1, 6)
        print(player2 + " is rolling(" + str(player2_rolls+1) + "): " + str(player2_dice))
        player2_roll_sum += player2_dice
        player2_rolls += 1
    print("The sum of that turn is: " + str(player2_roll_sum))
    if player2_result > 0:
        player2_result -= player2_roll_sum
    elif player2_result < 0:
        player2_result += player2_roll_sum
    print("The result after that turn is: " + str(player2_result) + " for " + player2)

    if player2_result == 0:
        break
		
if player1_result == 0:
    print(player1 + " wins!")
elif player2_result == 0:
    print(player2 + " wins!")
