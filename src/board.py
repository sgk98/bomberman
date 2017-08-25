from models import *
import os
from inp import *
import time
import random
#board=[[Cell() for i in range(20)] for j in range(20)]


def convert(board):
    '''Converts boards with cells into a printable board'''
    nboard = [[" " for i in range(76)] for j in range(38)]
    for i in range(len(board)):
        for j in range(len(board)):
            try:
                nboard[2 * j][4 * i] = board[i][j].symbol
                nboard[2 * j][4 * i + 1] = board[i][j].symbol
                nboard[2 * j][4 * i + 2] = board[i][j].symbol
                nboard[2 * j][4 * i + 3] = board[i][j].symbol
                nboard[2 * j + 1][4 * i] = board[i][j].symbol
                nboard[2 * j + 1][4 * i + 1] = board[i][j].symbol
                nboard[2 * j + 1][4 * i + 2] = board[i][j].symbol
                nboard[2 * j + 1][4 * i + 3] = board[i][j].symbol
            except:
                print i, j
    return nboard


def print_board(board):
    '''Displays the board'''
    os.system('clear')
    for i in range(len(board)):
        print("".join(board[i]))


def check(board, x, y, mode=""):
    '''Checks if a sqaure is fine for bomberman to go'''
    try:

        if mode != "" and board[x][y].symbol != "X":
            return True
        if(board[x][y].symbol == "X" or board[x][y].symbol == "B" or board[x][y].symbol == "/"):
            return False

        elif(board[x][y].symbol == "E" and mode == ""):

            return "DEAD"

        else:
            return True
    except IndexError:
        return False


def check_if_dead(bomberman, enemies):
    for i in enemies:
        if i.x == bomberman.x and i.y == bomberman.y:
            return True
    return False


if __name__ == "__main__":

    board = [[Cell() for i in range(19)] for j in range(19)]
    level = raw_input("enter difficulty\n1:Easy\n2:Medium\n3:Hard")
    if level == '3':
        no_enemies = 20
        enemy_slow = 10
    elif level == '2':
        no_enemies = 10
        enemy_slow = 30
    else:
        no_enemies = 5
        enemy_slow = 50

    enemies = []

    for i in range(len(board)):
        for j in range(len(board)):
            if i == 0 or j == 0 or i == 18 or j == 18:
                board[i][j].name = "wall"
                board[i][j].symbol = "X"
            elif i % 2 == 0 and j % 2 == 0:
                if i < 18:
                    board[i][j].name = "wall"
                    board[i][j].symbol = "X"
            if random.random() > 0.95 and i != 1 and j != 1 and board[i][j].symbol == " ":
                board[i][j].symbol = "/"

    bomberman = Bomberman()
    board[bomberman.x][bomberman.y].symbol = bomberman.symbol
    board[bomberman.x][bomberman.y].name = "bomberman"
    bombs = []
    lives = 3
    frame_count = 0
    to_explode = False
    score = 0

    while 1:
        frame_count += 1
        time.sleep(0.1)

        while len(enemies) < no_enemies:
            choices = []
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j].symbol == " ":
                        choices.append((i, j))
            ind = random.choice(choices)
            enemies.append(Enemy(ind[0], ind[1]))
            board[ind[0]][ind[1]].symbol = "E"
            board[ind[0]][ind[1]].name = "enemy"

        if frame_count % enemy_slow == 0:
            for i in range(len(enemies)):
                curx = enemies[i].x
                cury = enemies[i].y
                possible = [[curx + 1, cury], [curx - 1, cury],
                            [curx, cury + 1], [curx, cury - 1]]
                possible_after = []
                for j in possible:
                    can_go = check(board, j[0], j[1])
                    if can_go:
                        possible_after.append(j)
                square_choice = random.choice(possible_after)
                board[curx][cury] = Cell()
                board[square_choice[0]][square_choice[1]].symbol = "E"
                board[square_choice[0]][square_choice[1]].name = "enemy"
                enemies[i].x = square_choice[0]
                enemies[i].y = square_choice[1]

        if len(bombs) != 0:

            timer = 3 - (frame_count - bombs[0].frame) / 10
            if frame_count - bombs[0].frame > 30:
                to_explode = True
                bombx = bombs[0].x
                bomby = bombs[0].y
                possible_loc = [[bombx, bomby], [
                    bombx + 1, bomby], [bombx - 1, bomby], [bombx, bomby + 1], [bombx, bomby - 1]]
                blow_up = []
                for i in possible_loc:
                    can_go = check(board, i[0], i[1], "bomb")
                    if can_go:
                        # print(i)
                        if board[i[0]][i[1]].symbol == "/":
                            score += 20
                        board[i[0]][i[1]].symbol = "e"
                        blow_up.append(i)
                        if i[0] == bomberman.x and i[1] == bomberman.y:
                            lives -= 1
                            if lives == 0:
                                dead = True
                            else:
                                dead = False
                                board[bomberman.x][bomberman.y].symbol = "e"
                                bomberman = Bomberman()
                                board[1][1].symbol = "B"
                                enemies = []
                                break
                try:
                    if dead:
                        break
                except:
                    pass
                nenemies = []
                for i in blow_up:
                    for j in enemies:
                        if i[0] == j.x and i[1] == j.y:
                            board[j.x][j.y].symbol = "e"
                            score += 100
                        else:
                            nenemies.append(j)
                enemies = list(enemies)

                bombs = []

                #rint("made to 0")
            else:
                board[bombs[0].x][bombs[0].y].symbol = str(timer)

        nboard = convert(board)
        print_board(nboard)
        print "Score is:", score
        print "Lives Left:", lives
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].symbol == "e":
                    board[i][j] = Cell()
        char = get_char_keyboard_nonblock()
        if char == "w":
            can_go = check(board, bomberman.x, bomberman.y - 1)
            if can_go:
                board[bomberman.x][bomberman.y] = Cell()
                bomberman.y -= 1
                board[bomberman.x][bomberman.y].symbol = bomberman.symbol
                board[bomberman.x][bomberman.y].name = "bomberman"
            elif can_go == False:
                pass

        elif char == "a":
            can_go = check(board, bomberman.x - 1, bomberman.y)
            if can_go:
                board[bomberman.x][bomberman.y] = Cell()
                bomberman.x -= 1
                board[bomberman.x][bomberman.y].symbol = bomberman.symbol
                board[bomberman.x][bomberman.y].name = "bomberman"
            elif can_go == False:
                pass

        elif char == "s":
            can_go = check(board, bomberman.x, bomberman.y + 1)
            if can_go:
                board[bomberman.x][bomberman.y] = Cell()
                bomberman.y += 1
                board[bomberman.x][bomberman.y].symbol = bomberman.symbol
                board[bomberman.x][bomberman.y].name = "bomberman"
            elif can_go == False:
                pass

        elif char == "d":
            can_go = check(board, bomberman.x + 1, bomberman.y)
            if can_go:
                board[bomberman.x][bomberman.y] = Cell()
                bomberman.x += 1
                board[bomberman.x][bomberman.y].symbol = bomberman.symbol
                board[bomberman.x][bomberman.y].name = "bomberman"
            elif can_go == False:
                pass

        elif char == "b":
            if bombs == []:
                bomb = Bomb(bomberman.x, bomberman.y, frame_count)
                bombs.append(bomb)
        elif char == "q":
            sys.exit(0)

        dead = check_if_dead(bomberman, enemies)
        if dead:
            lives -= 1
            if lives == 0:
                print("Game Over")
                break
            else:
                board[bomberman.x][bomberman.y] = Cell()

                bomberman = Bomberman()
                board[1][1].symbol = "B"
                enemies = []
                bombs = []
