# Write your solution here
def who_won(game_board: list):
    count1 = 0
    count2 = 0
    count0 = 0
    for row in game_board:
        for number in row:
            if number == 0:
                count0 +=1
            elif number == 1:
                count1 +=1
            elif number == 2:
                count2 +=1
    if count1 > count2:
        # print("Player 1 won")
        return 1
    elif count2 > count1:
        # print("Player 2 won")
        return 2
    elif count1 == count2:
        # print("Draw")
        return 0
    else:
        # print("Nothing")
        return 0

if __name__ == "__main__":
    game_board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    who_won(game_board)
