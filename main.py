board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
taken = []
game_over = False
player = "X"


def draw_board():
    global player
    row1 = board[0]+"|"+board[1]+"|"+board[2]
    row2 = board[3]+"|"+board[4]+"|"+board[5]
    row3 = board[6]+"|"+board[7]+"|"+board[8]
    print(row1+"\n"+row2+"\n"+row3)
    pos = input(f"[player: {player}] - Select a position 1-9: ")
    total_pos = check_if_valid(pos)
    board[total_pos] = player


def check_if_valid(pos):
    while int(pos) > 9 or int(pos) < 1 or int(pos)-1 in taken:
        pos = input("Select a defferent position 1-9: ")
    else:
        total_pos = int(pos) - 1
        taken.append(total_pos)
        return total_pos


def swich_players():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"


def check_rows():
    global game_over
    global player
    row1 = board[0] == player and board[1] == player and board[2] == player
    row2 = board[3] == player and board[4] == player and board[5] == player
    row3 = board[6] == player and board[7] == player and board[8] == player
    if row1 or row2 or row3:
        print(f"PLAYER [{player}]  WON")
        game_over = True


def check_columns():
    global game_over
    global player
    col1 = board[0] == player and board[3] == player and board[6] == player
    col2 = board[1] == player and board[4] == player and board[7] == player
    col3 = board[2] == player and board[5] == player and board[8] == player
    if col1 or col2 or col3:
        print(f"PLAYER [{player}]  WON")
        game_over = True


def check_diagonals():
    global game_over
    global player
    dia1 = board[0] == player and board[4] == player and board[8] == player
    dia2 = board[2] == player and board[4] == player and board[6] == player

    if dia1 or dia2:
        print(f"PLAYER [{player}]  WON")
        game_over = True


while not game_over:
    draw_board()
    check_rows()
    check_columns()
    check_diagonals()
    swich_players()
