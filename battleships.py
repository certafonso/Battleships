import random

def game_setup(carrier_n,battleship_n,cruiser_n,destroyer_n,submarine_n):
    board = [["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]]
    aiboardshow = [["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]]
    aiboard = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

    for i in range(0,carrier_n): #player places the Aircraft Carrier
        board = placement(board,5,"Aircraft Carrier")
        aiboard = aiplacement(aiboard,5)
    for i in range(0,battleship_n): #player places the battleship
        board = placement(board,4,"Battleship")
        aiboard = aiplacement(aiboard,4)
    for i in range(0,cruiser_n): #player places the cruiser
        board = placement(board,3,"Cruiser")
        aiboard = aiplacement(aiboard,3)
    for i in range(0,destroyer_n): #player places the destroyer
        board = placement(board,2,"Destroyer")
        aiboard = aiplacement(aiboard,2)
    for i in range(0,submarine_n): #player places the submarine
        board = placement(board,1,"Submarine")
        aiboard = aiplacement(aiboard,1)

    print2board(board,aiboardshow)
    winner = "None"
    ailast_cell = []
    ailast_hit = 0
    while True:
        print2board(board,aiboardshow)
        aiboard, aiboardshow = playerturn(aiboard,aiboardshow)
        if checkwin(carrier_n,battleship_n,cruiser_n,destroyer_n,submarine_n,aiboardshow):
            winner = "Player"
            break
        board, ailast_cell, ailast_hit = aiturn(board,ailast_cell,ailast_hit)
        if checkwin(carrier_n,battleship_n,cruiser_n,destroyer_n,submarine_n,board):
            winner = "AI"
            break

    print(winner, "won")

def printboard(board): #prints the current board
    print("")
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters = []
    for i in range(0,len(board[0])):
        letters.append(alphabet[i])
    print("   ","   ".join(letters))
    for i in range(0,len(board)):
        if i+1 >= 10:
            print(i+1, " ".join(board[i]))
        else:
            print(i+1, "", " ".join(board[i]))

def print2board(board,aiboard): #prints the player's board and the AI's board
    print("")
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters = []
    print("                     You                                           Com")
    for i in range(0,len(board[0])):
        letters.append(alphabet[i])
    print("   ","   ".join(letters),"       ","   ".join(letters))
    for i in range(0,len(board)):
        if i+1 >= 10:
            print(i+1, " ".join(board[i]),"     ", " ".join(aiboard[i]),i+1)
        else:
            print(i+1, "", " ".join(board[i]),"     ", " ".join(aiboard[i]),"",i+1)

def placement(board,size,name): #puts ships
    upperalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    loweralphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    possibledirections = ["Cancel"]
    validdirections = ["Cancel", "cancel"]
    printboard(board)
    print("Where do you want to place the", name, "( Size", size,")")
    answer = input("")
    cell = answer.split()
    if len(cell) == 2: #if player puts coordinates will store them as numbers
        if cell[0] in upperalphabet:
            cell[0] = upperalphabet.index(cell[0])
            cell[1] = int(cell[1])-1

        elif cell[0] in loweralphabet:
            cell[0] = loweralphabet.index(cell[0])
            cell[1] = int(cell[1])-1

        else:
            print("Invalid Cell")
            return placement(board,size,name)
        if cell[0] > 10 or cell[1] > 10 or cell[1] < 0 or (board[cell[1]])[cell[0]] == "[■]": #checks if coordinates are inside the board
            print("Invalid Cell")
            return placement(board,size,name)

        if size > 1:
            if cell[0] - (size-1) >= 0: #checks if ship can be placed to the left
                valid = True
                for i in range(cell[0],cell[0]-size,-1):
                    if (board[cell[1]])[i] == "[■]":
                        valid = False
                if valid:
                    possibledirections.append("Left")
                    validdirections.append("Left")
                    validdirections.append("left")

            if cell[0] + (size-1) <= 9: #checks if ship can be placed to the right
                valid = True
                for i in range(cell[0],cell[0]+size):
                    if (board[cell[1]])[i] == "[■]":
                        valid = False
                if valid:
                    possibledirections.append("Right")
                    validdirections.append("Right")
                    validdirections.append("right")

            if cell[1] - (size-1) >= 0: #checks if ship can be placed to up
                valid = True
                for i in range(cell[1],cell[1]-size,-1):
                    if (board[i])[cell[0]] == "[■]":
                        valid = False
                if valid:
                    possibledirections.append("Up")
                    validdirections.append("Up")
                    validdirections.append("up")

            if cell[1] + (size-1) <= 9: #checks if ship can be placed to down
                valid = True
                for i in range(cell[1],cell[1]+size):
                    if (board[i])[cell[0]] == "[■]":
                        valid = False
                if valid:
                    possibledirections.append("Down")
                    validdirections.append("Down")
                    validdirections.append("down")

            while True: #asks direction
                print("In which direction do you want to place it ( Size", size,") \n( Possible directions:",", ".join(possibledirections),")")
                direction = input()
                if direction not in validdirections: #checks if direction is valid
                    print("Invalid Direction")
                elif direction == "Left" or direction == "left": #places ship to the left
                    for i in range(cell[0],cell[0]-size,-1):
                        (board[cell[1]])[i] = "[■]"
                    return board
                elif direction == "Right" or direction == "right": #places ship to the left
                    for i in range(cell[0],cell[0]+size):
                        (board[cell[1]])[i] = "[■]"
                    return board
                elif direction == "Up" or direction == "up": #places ship to up
                    for i in range(cell[1],cell[1]-size,-1):
                        (board[i])[cell[0]] = "[■]"
                    return board
                elif direction == "Down" or direction == "down": #places ship to down
                    for i in range(cell[1],cell[1]+size):
                        (board[i])[cell[0]] = "[■]"
                    return board
                elif direction == "Cancel" or direction == "cancel":
                    return placement(board,size,name)

        elif size == 1:
            (board[cell[1]])[cell[0]] = "[■]"
            return board

        else:
            raise ValueError("Size has to be greater than 0")
    else:
        print("Invalid Cell")
        return placement(board,size,name)

def aiplacement(board,size): #puts ships
    possibledirections = []
    cell = [random.randint(0,9),random.randint(0,9)]
    #print(cell)
    #print(size)

    if (board[cell[1]])[cell[0]] == -1: #checks if the cell has a ship
        return aiplacement(board,size)

    if size > 1:
        if cell[0] - (size-1) >= 0: #checks if ship can be placed to the left
            valid = True
            for i in range(cell[0],cell[0]-size,-1):
                if (board[cell[1]])[i] == -1:
                    valid = False
            if valid:
                possibledirections.append("Left")

        if cell[0] + (size-1) <= 9: #checks if ship can be placed to the right
            valid = True
            for i in range(cell[0],cell[0]+size):
                if (board[cell[1]])[i] == -1:
                    valid = False
            if valid:
                possibledirections.append("Right")

        if cell[1] - (size-1) >= 0: #checks if ship can be placed to up
            valid = True
            for i in range(cell[1],cell[1]-size,-1):
                if (board[i])[cell[0]] == -1:
                    valid = False
            if valid:
                possibledirections.append("Up")

        if cell[1] + (size-1) <= 9: #checks if ship can be placed to down
            valid = True
            for i in range(cell[1],cell[1]+size):
                if (board[i])[cell[0]] == -1:
                    valid = False
            if valid:
                possibledirections.append("Down")

        try: #asks direction
            direction = possibledirections[random.randint(0,len(possibledirections)-1)]
            #print(direction)
            if direction == "Left" or direction == "left": #places ship to the left
                for i in range(cell[0],cell[0]-size,-1):
                    (board[cell[1]])[i] = -1
                return board
            elif direction == "Right" or direction == "right": #places ship to the left
                for i in range(cell[0],cell[0]+size):
                    (board[cell[1]])[i] = -1
                return board
            elif direction == "Up" or direction == "up": #places ship to up
                for i in range(cell[1],cell[1]-size,-1):
                    (board[i])[cell[0]] = -1
                return board
            elif direction == "Down" or direction == "down": #places ship to down
                for i in range(cell[1],cell[1]+size):
                    (board[i])[cell[0]] = -1
                return board
        except:
                return aiplacement(board,size)

    elif size == 1:
        (board[cell[1]])[cell[0]] = -1
        return board

    else:
        raise ValueError("Size has to be greater than 0")

def playerturn(aiboard,aiboardshow):
    upperalphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    loweralphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    answer = input("Where do you want to fire?\n")
    cell = answer.split()

    if len(cell) == 2: #if player puts coordinates will store them as numbers
        if cell[0] in upperalphabet:
            cell[0] = upperalphabet.index(cell[0])
            cell[1] = int(cell[1])-1

        elif cell[0] in loweralphabet:
            cell[0] = loweralphabet.index(cell[0])
            cell[1] = int(cell[1])-1

        else:
            print("Invalid Cell")
            return playerturn(aiboard,aiboardshow)

        if cell[0] > 10 or cell[1] > 10 or cell[1] < 0 or (aiboard[cell[1]])[cell[0]] == 0 or (aiboard[cell[1]])[cell[0]] == 2: #checks if coordinates are inside the board
            print("Invalid Cell")
            return playerturn(aiboard,aiboardshow)

        (aiboard[cell[1]])[cell[0]] = (aiboard[cell[1]])[cell[0]] + 1

        if (aiboard[cell[1]])[cell[0]] == 0: #if cell has boat marks with "[X]"
            (aiboardshow[cell[1]])[cell[0]] = "[X]"

        elif (aiboard[cell[1]])[cell[0]] == 2: #if cell doesn't have a boat marks with "[/]"
            (aiboardshow[cell[1]])[cell[0]] = "[/]"

        return aiboard, aiboardshow
    else:
        print("Invalid Cell")
        return playerturn(aiboard,aiboardshow)

def aiturn(board,ailast_cell,ailast_hit):
    cell = []
    try:
        ailast_direction = ailast_cell[2]
    except:
        ailast_direction = 0

    if ailast_hit == 1:
        while True:
            if ailast_direction == 0:
                cell = [ailast_cell[0]+1,ailast_cell[1]]
                print("1")
                ailast_direction = 1
                break

            elif ailast_direction == 1:
                cell = [ailast_cell[0],ailast_cell[1]+1]
                print("2")
                ailast_direction = 2
                break

            elif ailast_direction == 2:
                cell = [ailast_cell[0]-1,ailast_cell[1]]
                print("3")
                ailast_direction = 3
                break

            elif ailast_direction == 3:
                cell = [ailast_cell[0],ailast_cell[1]-1]
                print("4")
                ailast_direction = 4
                break

            else:
                ailast_hit = 0
                while True:
                    if random.randint(0,1):
                        cell = [random.randint(0,4)*2,random.randint(0,4)*2]
                    else:
                        cell = [(random.randint(0,4)*2)+1,(random.randint(0,4)*2)+1]

                    if board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]":
                        break
                break

    elif ailast_hit > 1:
        if ailast_direction == 1:
            while True:
                cell = [ailast_cell[0]+1,ailast_cell[1]]
                if cell[0] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                    break

                cell = [ailast_cell[0]-1,ailast_cell[1]]
                if cell[0] >= 0 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                    break

                ailast_direction == -1
                break

        elif ailast_direction == 2:
            while True:
                cell = [ailast_cell[0],ailast_cell[1]+1]
                if cell[1] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                    break

                cell = [ailast_cell[0],ailast_cell[1]-1]
                if cell[1] >= 0 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                    break

                ailast_direction == -2
                break

        elif ailast_direction == -1:
            print("4")
            while True:
                print("3")
                if ailast_cell[0]-ailast_hit >= 0 and board[ailast_cell[0]-ailast_hit][ailast_cell[1]] == "[X]":
                    print("1")
                    cell = [ailast_cell[0]-ailast_hit,ailast_cell[1]]
                    if cell[0] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                        break
                elif ailast_cell[0]+ailast_hit < 10 and board[ailast_cell[0]+ailast_hit][ailast_cell[1]] == "[X]":
                    print("2")
                    cell = [ailast_cell[0]+ailast_hit,ailast_cell[1]]
                    if cell[0] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                        break
                else:
                    ailast_hit = 0
                    while True:
                        if random.randint(0,1):
                            cell = [random.randint(0,4)*2,random.randint(0,4)*2]
                        else:
                            cell = [(random.randint(0,4)*2)+1,(random.randint(0,4)*2)+1]

                        if board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]":
                            break
                break

        elif ailast_direction == -2:
            print("5")
            while True:
                print("6")
                if ailast_cell[1]-ailast_hit >= 0 and board[ailast_cell[0]][ailast_cell[1]-ailast_hit] == "[X]":
                    print("7")
                    cell = [ailast_cell[0],ailast_cell[1]-ailast_hit]
                    if cell[0] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                        break
                elif ailast_cell[1]+ailast_hit < 10 and board[ailast_cell[0]][ailast_cell[1]+ailast_hit] == "[X]":
                    print("8")
                    cell = [ailast_cell[0],ailast_cell[1]+ailast_hit]
                    if cell[0] < 10 and (board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]"):
                        break
                else:
                    ailast_hit = 0
                    while True:
                        if random.randint(0,1):
                            cell = [random.randint(0,4)*2,random.randint(0,4)*2]
                        else:
                            cell = [(random.randint(0,4)*2)+1,(random.randint(0,4)*2)+1]

                        if board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]":
                            break
                break

    else:
        while True:
            if random.randint(0,1):
                cell = [random.randint(0,4)*2,random.randint(0,4)*2]
            else:
                cell = [(random.randint(0,4)*2)+1,(random.randint(0,4)*2)+1]

            if board[cell[0]][cell[1]] == "[ ]" or board[cell[0]][cell[1]] == "[■]":
                break

    if (board[cell[1]])[cell[0]] == "[■]": #if cell has boat marks with "[X]"
        print("Ai acertou")
        (board[cell[1]])[cell[0]] = "[X]"
        ailast_hit = ailast_hit + 1
        ailast_cell = cell

    elif (board[cell[1]])[cell[0]] == "[ ]": #if cell doesn't have a boat marks with "[/]"
        print("Ai nao acertou")
        (board[cell[1]])[cell[0]] = "[/]"
        if ailast_direction == 0:
            ailast_hit = 0
    else:
        return aiturn(board,ailast_cell,ailast_hit)


    try:
        ailast_cell[2] = ailast_direction
    except:
        ailast_cell.append(ailast_direction)
    print(cell, board, ailast_cell, ailast_hit)
    return board, ailast_cell, ailast_hit

def checkwin(carrier_n,battleship_n,cruiser_n,destroyer_n,submarine_n,board):
    sink_max = carrier_n * 5 + battleship_n * 4 + cruiser_n * 3 + destroyer_n * 2 + submarine_n * 1
    sink_n = 0

    for i in range(0,len(board)):
        for x in range(0,len(board[i])):
            if board[i][x] == "[X]":
                sink_n = sink_n + 1

    if sink_n < sink_max:
        return False
    else:
        return True

#game_setup(1,1,1,2,2)
game_setup(4,0,0,0,0)
