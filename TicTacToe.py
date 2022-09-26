import random
import sys, pygame
import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = []
        self.create_board()
        self.player = 'X' if self.get_random_first_player() == 1 else 'O'
        self.playerPC = "O" if self.player == "X" else 'X'

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
            return True
        else:
           return False

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

        # Intentar coger el centro
        if board[1][1] == "-":
            return 2, 2
        #Tratar de jugar en las esquinas
        jugadasGood=[[1,1], [1,3], [3,1], [3,3]]
        jugada=self.elegir_jugada_azar(board, jugadasGood)
        if jugada != None:
            return jugada
        else:
            return None, None
        # Jugar a los lados
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
            return None

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


class TicTacToeGame:

    def __init__(self):
        # Inicializamos pygame
        pygame.init()
        # Muestro una ventana de 800x600
        self.size = 360, 360
        self.screen = pygame.display.set_mode(self.size)
        # Cambio el título de la ventana
        pygame.display.set_caption("Juego Tic-Tac-Toe")
        # Inicializamos variables
        self.width, self.height = 360, 360
        # Crea un objeto imagen tablero y obtengo su rectángulo
        self.tablero = pygame.image.load("tablero.png")
        self.tablerorect = self.tablero.get_rect()
        # Pongo el tablero en la pantalla
        self.tablerorect.move_ip(0, 0)
        # Crea un objeto imagen juador X y obtengo su rectángulo
        self.xPlayer = pygame.image.load("X.png")
        self.xrect = self.xPlayer.get_rect()
        # Crea un objeto imagen juador O y obtengo su rectángulo
        self.oPlayer = pygame.image.load("O.png")
        self.orect = self.oPlayer.get_rect()
        self.run=True
        self.diclic = False
        self.juegaPC = False
        self.termino=False
        #inicializo TicTacToe
        self.tic_tac_toe = TicTacToe()



    def startGame(self):
        while self.run:
            # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
            pygame.time.delay(1)
            # Capturamos los eventos que se han producido
            for event in pygame.event.get():
                # Si el evento es salir de la ventana, terminamos
                if event.type == pygame.QUIT: self.run = False

            row, col =0, 0
            if event.type == pygame.MOUSEBUTTONDOWN and not self.termino and not self.juegaPC:
                xPos, yPos = pygame.mouse.get_pos()
                if (0 <= xPos <= 120) and (0 <= yPos <= 120):
                    xPos, yPos = 0, 0
                    row, col = 1, 1
                elif (120+1 <= xPos <= 240) and (0 <= yPos <= 120):
                    xPos, yPos = 120, 0
                    row, col = 1, 2
                elif (240+1 <= xPos <= 360) and (0 <= yPos <= 120):
                    xPos, yPos = 240, 0
                    row, col = 1, 3
                elif (0 <= xPos <= 120) and (120+1 <= yPos <= 240):
                    xPos, yPos = 0, 120
                    row, col = 2, 1
                elif (120+1 <= xPos <= 240) and (121 <= yPos <= 240):
                    xPos, yPos = 120, 120
                    row, col = 2, 2
                elif (240+1 <= xPos <= 360) and (121 <= yPos <= 240):
                    xPos, yPos = 240, 120
                    row, col = 2, 3
                elif (0 <= xPos <= 120) and (241 <= yPos <= 360):
                    xPos, yPos = 0, 240
                    row, col = 3, 1
                elif (120+1 <= xPos <= 240) and (241 <= yPos <= 360):
                    xPos, yPos = 120, 240
                    row, col = 3, 2
                elif (240+1 <= xPos <= 360) and (241 <= yPos <= 360):
                    xPos, yPos = 240, 240
                    row, col = 3, 3
                # Pinto la X o O y actualizo la pantalla
                if self.tic_tac_toe.player == "X":
                    self.xrect.update(self.xPlayer.get_rect())
                    self.xrect.move_ip(xPos, yPos)
                else:
                    self.orect.update(self.oPlayer.get_rect())
                    self.orect.move_ip(xPos, yPos)
                # Hago la logica para jugar
                self.juegaPC = self.tic_tac_toe.fix_spot(row - 1, col - 1, self.tic_tac_toe.player)
                if self.tic_tac_toe.is_player_win(self.tic_tac_toe.player):
                    print(f"Player {self.tic_tac_toe.player} wins the game!")
                    self.termino=True
                # checking whether the game is draw or not
                if self.tic_tac_toe.is_board_filled():
                    print("Match Draw!")
                    self.termino=True

                # Poner la PC a Jugar
                if self.juegaPC and not self.termino:
                    print(f"Ya jugo Player {self.tic_tac_toe.player}!")
                    print(f"Ahora juega PlayerPC {self.tic_tac_toe.playerPC}!")
                    fila, columna = self.tic_tac_toe.estado_favorable(self.tic_tac_toe.board,self.tic_tac_toe.playerPC)
                    if fila != None and columna != None:
                        print(f"La PC jugo {fila} {columna}")
                        self.tic_tac_toe.board[fila - 1][columna - 1] = self.tic_tac_toe.playerPC
                        # checking whether playerPC is won or not
                        if self.tic_tac_toe.is_player_win(self.tic_tac_toe.playerPC):
                            print(f"Player {self.tic_tac_toe.playerPC} wins the game!")
                            self.termino = True
                    else:
                        print("Match Draw!")
                        self.termino=True

                self.juegaPC = False
            self.diclic = True




            # Pinto el fondo, dibujo lo que hay en el tablero y actualizo la pantalla
            self.screen.blit(self.tablero, self.tablerorect)
            for i in range(3):
                for j in range(3):
                    xPos, yPos = self.damePosTablero(i, j)
                    if self.tic_tac_toe.board[i][j] == "X":
                        self.xPlayer = pygame.image.load("X.png")
                        self.xrect.update(self.xPlayer.get_rect())
                        self.xrect.move_ip(xPos, yPos)
                        self.screen.blit(self.xPlayer, self.xrect)
                    if self.tic_tac_toe.board[i][j] == "O":
                        self.oPlayer = pygame.image.load("O.png")
                        self.orect.update(self.oPlayer.get_rect())
                        self.orect.move_ip(xPos, yPos)
                        self.screen.blit(self.oPlayer, self.orect)


            pygame.display.flip()
        # Salgo de pygame
        pygame.quit()


    def damePosTablero(self, i, j):
        xPos, yPos = None, None
        if (i == 0) and (j == 0):
           xPos , yPos = 0, 0
        elif (i == 0) and (j == 1):
            xPos, yPos = 120, 0
        elif (i == 0) and (j == 2):
            xPos, yPos = 240, 0
        elif (i == 1) and (j == 0):
            xPos, yPos = 0, 120
        elif (i == 1) and (j == 1):
            xPos, yPos = 120, 120
        elif (i == 1) and (j == 2):
            xPos, yPos = 240, 120
        elif (i == 2) and (j == 0):
            xPos, yPos = 0, 240
        elif (i == 2) and (j == 1):
            xPos, yPos = 120, 240
        elif (i == 2) and (j == 2):
            xPos, yPos = 240, 240
        return xPos, yPos



# starting the game
ticTacToe_Game = TicTacToeGame()
ticTacToe_Game.startGame()
#tic_tac_toe = TicTacToe()
#tic_tac_toe.start()
