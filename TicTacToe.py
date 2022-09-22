import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        if self.board[row][col] == '-':
            self.board[row][col] = player
        else:
            print(f"Player {player} esa casilla está ocupada.")
            print(f"Player {player} turn")
            self.show_board()
            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
            self.fix_spot(row-1, col-1, player)

    def estado_favorable(self, board, playerPC):
        #Ver si la PC gana en su proxima Jugada
        for i in range(3):
            for j in range(3):
                copia=self.duplicar_Tableto(board)
                if self.hacer_jugadaPC(copia, i, j, playerPC):
                    if self.is_player_winPC(copia, playerPC):
                        return i+1, j+1
        #Ver si el jugador le podra ganar a la PC en su proxima jugada para que la PC juegue ahi
        player = "O" if playerPC == "X" else 'X'
        for i in range(3):
            for j in range(3):
                copia=self.duplicar_Tableto(board)
                if self.hacer_jugadaPC(copia, i, j, player):
                    if self.is_player_winPC(copia, player):
                        return i+1, j+1
        #Tratar de jugar en las esquinas
        jugadasGood=[[1,1], [1,3], [3,1], [3,3]]
        jugada=self.elegir_jugada_azar(board, jugadasGood)
        if jugada != None:
            return jugada
        #Intentar coger el centro
        if board[2][2] == "-":
            return 2, 2
        #Jugar a los lados
        lados = [[1, 2], [2, 1], [2, 3], [3, 2]]
        return self.elegir_jugada_azar(board, lados)


    def duplicar_Tableto(self, boardOrig):
        boardDup=[]
        for i in range(3):
            row = []
            for j in range(3):
                row.append(boardOrig[i][j])
            boardDup.append(row)
        return boardDup

    def elegir_jugada_azar(self, board, listaJugada):
        jugadas=[]
        for row, col in listaJugada:
            if board[row-1][col-1] == '-':
                jugadas.append((row,col))
        if len(jugadas) != 0:
            return random.choice(jugadas)
        else:
            None

    def is_player_winPC(self, board, player):
        win = None

        n = len(board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filledPC(self, board):
        for row in board:
            for item in row:
                if item == '-':
                    return False
        return True

    def hacer_jugadaPC(self, board, row, col, player):
        if board[row][col] == '-':
            board[row][col] = player
            return True
        else:
            return False

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def show_boardPC(self, board):
        for row in board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        playerPC = "O" if player == "X" else 'X'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            #poner a la PC a Jugar
            print(f"Ya jugo Player {player}!")
            print(f"Ahora juega PlayerPC {playerPC}!")
            fila, columna = self.estado_favorable(self.board, playerPC)
            print(f"La PC jugo {fila} {columna}")
            self.board[fila-1][columna-1] = playerPC

            # checking whether playerPC is won or not
            if self.is_player_win(playerPC):
                print(f"Player {playerPC} wins the game!")
                break

            # swapping the turn
            #player = self.swap_player_turn(playerPC)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
