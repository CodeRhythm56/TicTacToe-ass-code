bd = ["-"] * 9  # board data
board = ""
player = ""
gameover = 0

def refreshBoard():
    global board
    board = "     |     |     \n" \
            "  {a}  |  {b}  |  {c}  \n".format(a=bd[0], b=bd[1], c=bd[2]) + "_____|_____|_____\n" \
            "     |     |     \n" \
            "  {d}  |  {e}  |  {f}  \n".format(d=bd[3],e=bd[4],f=bd[5]) + "_____|_____|_____\n" \
            "     |     |     \n" \
            "  {g}  |  {h}  |  {i}  \n".format(g=bd[6], h=bd[7], i=bd[8]) + "     |     |     \n"

def CheckForWin(player):
    #horizontal
    a=0
    for x in range(3):
        if player == bd[a] and player == bd[a+1] and player == bd[a+2]:
            print("player ", player, " won")
            gameover = 1
        a += 3
    #vertical
    a=0
    for x in range(3):
        if player == bd[a] and player == bd[a+3] and player == bd[a+6]:
            print("player ", player, " won")
            gameover = 1
        a += 1
    #diagonal
    if player == bd[1] and player == bd[5] and player == bd[9]:
        print("player ", player, " won")
        gameover = 1
    if player == bd[3] and player == bd[5] and player == bd[7]:
        print("player ", player, " won")
        gameover = 1
turn = 0
while gameover == 0:
    if turn == 0:
        val = int(input("Enter the box, X turn"))
        if bd[val -1 ] != "-":
            bd[val - 1] = "X"
            turn = turn + 1
            refreshBoard()
            print(board)
            CheckForWin("X")
        else:
            print("Space occupied. Try again")
    if turn == 1:
        val = int(input("Enter the box, O turn"))
        if bd[val -1 ] != "-":
            bd[val - 1] = "O"
            turn = turn - 1
            refreshBoard()
            print(board)
            CheckForWin("O")
        else:
            print("Space occupied. Try again")
