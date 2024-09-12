def print_board(board):
    """طباعة لوحة اللعبة"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """التحقق من فوز اللاعب"""
    win_conditions = [
        # تحقق من الصفوف
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # تحقق من الأعمدة
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # تحقق من الأقطار
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    """التحقق مما إذا كانت اللوحة ممتلئة"""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """التحكم في لعبة تيك تاك تو"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"دور اللاعب {current_player}")

        # طلب الإدخال من اللاعب
        while True:
            try:
                row = int(input("أدخل رقم الصف (0، 1، 2): "))
                col = int(input("أدخل رقم العمود (0، 1، 2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("الخانة مشغولة، حاول مرة أخرى.")
            except (IndexError, ValueError):
                print("إدخال غير صحيح، حاول مرة أخرى.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"مبروك! اللاعب {current_player} فاز!")
            break

        if is_board_full(board):
            print_board(board)
            print("التعادل!")
            break

        # التبديل بين اللاعبين
        current_player = "O" if current_player == "X" else "X"

# تشغيل اللعبة
if __name__ == "__main__":
    tic_tac_toe()
