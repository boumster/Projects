
class Chess:
    
    board = [['bR','bN','bB','bQ','bK','bB','bN','bR'],
             ['bP','bP','bP','bP','bP','wQ','bP','bP',],
             ['**','**','**','**','**','**','**','**',],
             ['**','**','**','**','**','**','**','**',],
             ['**','**','**','**','**','**','**','**',],
             ['**','**','**','**','**','**','**','**',],
             ['wP','wP','wP','wP','wP','wP','wP','wP',],
             ['wR','wN','wB','wQ','wK','wB','wN','wR']]      #initializing board

    letter_position = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
    number_position = {'1' : 7, '2' : 6, '3' : 5, '4' : 4, '5' : 3, '6' : 2, '7' : 1, '8' : 0}## setting positions with white on the bottom

    number_to_letter = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}
    number_to_number = {7 : '1', 6 : '2', 5 : '3', 4 : '4', 3 : '5', 2 : '6', 1 : '7', 0 : '8'}

    turn = 1 #setting turn for white then multiplied for -1 to switch turns

    white = ['wR','wN','wB','wQ','wK','wB','wN','wR', 'wP']
    black = ['bR','bK','bB','bQ','bK','bB','bN','bR', 'bP']

    def set_move(starting_str, desired_str):
        move_list = Chess.process_move(starting_str, desired_str)
        legal_move = Chess.move_legal(move_list)

        if legal_move == 0:
            print('Please select one of your pieces')
            return 0

        elif legal_move == 1:

            Chess.board[move_list[1][0]][move_list[1][1]] = Chess.board[move_list[0][0]][move_list[0][1]]
            Chess.board[move_list[0][0]][move_list[0][1]] = '**'
            return 1

        elif legal_move == -1:

            print("Please choose a legal move")
            return -1

    def move_legal(move_list): #Return a integer value of 0, -1, 1. 0 meaning the starting position has no pieces, -1 not a legal move, 1 a legal move
        piece = Chess.board[move_list[0][0]][move_list[0][1]]
        desired_position = move_list[1]

        if piece == '**':
            return 0

        if piece == 'bN' or 'wN':
            if piece == 'bN' and Chess.turn == -1:
                if desired_position in Chess.knight_move(move_list[0], color = 'b'):
                    return 1
                else:
                    return -1
            elif piece == 'wN' and Chess.turn == 1:
                if desired_position in Chess.knight_move(move_list[0], color = 'w'):
                    return 1
                else:
                    return -1
            elif (piece == 'wN' and Chess.turn == -1) or (piece == 'bN' and Chess.turn == 1):
                return 0

        if piece == 'wP' or 'bP':
            if piece == 'wP' and Chess.turn == 1:
                if desired_position in Chess.pawn_move(move_list[0], color = 'w'):
                    return 1
                else: 
                    return -1
            if piece == 'bP' and Chess.turn == -1:
                if desired_position in Chess.pawn_move(move_list[0], color = 'b'):
                    return 1
                else:
                    return -1
            elif (piece == 'wP' and Chess.turn == -1) or (piece == 'bP' and Chess.turn == 1):
                return 0

        if piece == 'wB' or 'bB':
            if piece == 'wB' and Chess.turn == 1:
                if desired_position in Chess.bishop_move(move_list[0], color = 'w'):
                    return 1
                else: 
                    return -1
            if piece == 'bB' and Chess.turn == -1:
                if desired_position in Chess.bishop_move(move_list[0], color = 'b'):
                    return 1
                else:
                    return -1
            elif (piece == 'wB' and Chess.turn == -1) or (piece == 'bB' and Chess.turn == 1):
                return 0

        if piece == 'wR' or 'bR':
            if piece == 'wR' and Chess.turn == 1:
                if desired_position in Chess.rook_move(move_list[0], color = 'w'):
                    return 1
                else: 
                    return -1
            if piece == 'bR' and Chess.turn == -1:
                if desired_position in Chess.rook_move(move_list[0], color = 'b'):
                    return 1
                else:
                    return -1
            elif (piece == 'wR' and Chess.turn == -1) or (piece == 'bR' and Chess.turn == 1):
                return 0
        
        if piece == 'wQ' or 'bQ':
            if piece == 'wQ' and Chess.turn == 1:
                if desired_position in Chess.queen_move(move_list[0], color = 'w'):
                    return 1
                else: 
                    return -1
            if piece == 'bQ' and Chess.turn == -1:
                if desired_position in Chess.queen_move(move_list[0], color = 'b'):
                    return 1
                else:
                    return -1
            elif (piece == 'wQ' and Chess.turn == -1) or (piece == 'bQ' and Chess.turn == 1):
                return 0
            
            if piece == 'wK' or 'bK':
                if piece == 'wK' and Chess.turn == 1:
                    if desired_position in Chess.king_move(move_list[0], color = 'w'):
                        return 1
                    else: 
                        return -1
                if piece == 'bK' and Chess.turn == -1:
                    if desired_position in Chess.king_move(move_list[0], color = 'b'):
                        return 1
                    else:
                        return -1
                elif (piece == 'wK' and Chess.turn == -1) or (piece == 'bK' and Chess.turn == 1):
                    return 0

    # Next 6 functions will take in the position of a piece and returns list of their legal moves
    def king_move(start, color):
        x_position = start[1]
        y_position = start[0]
        legal_moves = []
        if color == 'w':
            if x_position + 1 < 8 and Chess.board[y_position][x_position+1] not in Chess.white and Chess.king_in_checkmate([y_position, x_position+1], color = 'w'):
                legal_moves.append([y_position,x_position+1])
            if x_position - 1 >= 0 and Chess.board[y_position][x_position-1] not in Chess.white and Chess.king_in_checkmate([y_position, x_position-1],color = 'w'):
                legal_moves.append([y_position,x_position-1])
            if y_position + 1 < 8 and Chess.board[y_position+1][x_position] not in Chess.white and Chess.king_in_checkmate([y_position+1, x_position],color = 'w'):
                legal_moves.append([y_position+1,x_position])
            if y_position - 1 >= 0 and Chess.board[y_position-1][x_position] not in Chess.white and Chess.king_in_checkmate([y_position-1, x_position],color = 'w'):
                legal_moves.append([y_position-1,x_position])
            if y_position + 1 < 8 and x_position + 1 < 8 and Chess.board[y_position+1][x_position+1] not in Chess.white and Chess.king_in_checkmate([y_position+1, x_position+1],color = 'w'):
                legal_moves.append([y_position+1,x_position+1])
            if y_position - 1 >= 0 and x_position + 1 < 8 and Chess.board[y_position-1][x_position+1] not in Chess.white and Chess.king_in_checkmate([y_position-1, x_position+1],color = 'w'):
                legal_moves.append([y_position+1,x_position+1])
            if y_position + 1 < 8 and x_position - 1 > 0 and Chess.board[y_position+1][x_position-1] not in Chess.white and Chess.king_in_checkmate([y_position+1, x_position-1],color = 'w'):
                legal_moves.append([y_position+1,x_position-1])
            if y_position - 1 > 0 and x_position - 1 > 0 and Chess.board[y_position-1][x_position-1] not in Chess.white and Chess.king_in_checkmate([y_position-1, x_position-1],color = 'w'):
                legal_moves.append([y_position-1,x_position-1])
        if color == 'b':
            if x_position + 1 < 8 and Chess.board[y_position][x_position+1] not in Chess.black and Chess.king_in_checkmate([y_position, x_position+1],color = 'b'):
                legal_moves.append([y_position,x_position+1])
            if x_position - 1 >= 0 and Chess.board[y_position][x_position-1] not in Chess.black and Chess.king_in_checkmate([y_position, x_position-1],color = 'b'):
                legal_moves.append([y_position,x_position-1])
            if y_position + 1 < 8 and Chess.board[y_position+1][x_position] not in Chess.black and Chess.king_in_checkmate([y_position+1, x_position],color = 'b'):
                legal_moves.append([y_position+1,x_position])
            if y_position - 1 >= 0 and Chess.board[y_position-1][x_position] not in Chess.black and Chess.king_in_checkmate([y_position-1, x_position],color = 'b'):
                legal_moves.append([y_position-1,x_position])
            if y_position + 1 < 8 and x_position + 1 < 8 and Chess.board[y_position+1][x_position+1] not in Chess.black and Chess.king_in_checkmate([y_position+1, x_position+1],color = 'b'):
                legal_moves.append([y_position+1,x_position+1])
            if y_position - 1 >= 0 and x_position + 1 < 8 and Chess.board[y_position-1][x_position+1] not in Chess.black and Chess.king_in_checkmate([y_position-1, x_position+1],color = 'b'):
                legal_moves.append([y_position+1,x_position+1])
            if y_position + 1 < 8 and x_position - 1 > 0 and Chess.board[y_position+1][x_position-1] not in Chess.black and Chess.king_in_checknmate([y_position+1, x_position-1],color = 'b'):
                legal_moves.append([y_position+1,x_position-1])
            if y_position - 1 > 0 and x_position - 1 > 0 and Chess.board[y_position-1][x_position-1] not in Chess.black and Chess.king_in_checkmate([y_position-1, x_position-1],color = 'b'):
                legal_moves.append([y_position-1,x_position-1])

    def queen_move(start, color): # super simple just call bishop and rook for moves
        legal_moves = Chess.rook_move(start,color) + Chess.bishop_move(start, color)
        return legal_moves

    def rook_move(start, color): # Simple for loops of looking side to side and up and down
        x_position = start[1]
        y_position = start[0]
        legal_moves = []

        for i in range(x_position+1, 8):# checks right
            if Chess.board[y_position][i] not in Chess.white and color == 'w':
                legal_moves.append([y_position, i])
            elif Chess.board[y_position][i] not in Chess.black and color == 'b':
                legal_moves.append([y_position, i])
            else:
                break

        for i in range(x_position-1, -1, -1):# checks left
            if Chess.board[y_position][i] not in Chess.white and color == 'w':
                legal_moves.append([y_position, i])
            elif Chess.board[y_position][i] not in Chess.black and color == 'b':
                legal_moves.append([y_position, i])
            else:
                break

        for j in range(y_position+1, 8): # checks down
            if Chess.board[j][x_position] not in Chess.white and color == 'w':
                legal_moves.append([j,x_position])
            elif Chess.board[j][x_position] not in Chess.black and color == 'b':
                legal_moves.append([j,x_position])
            else: break

        for j in range(y_position-1, -1, -1): # checks up
            if Chess.board[j][x_position] not in Chess.white and color == 'w':
                legal_moves.append([j,x_position])
            elif Chess.board[j][x_position] not in Chess.black and color == 'b':
                legal_moves.append([j,x_position])
            else: break
        return legal_moves

    def bishop_move(start, color): ## will look at diagonals using for loops
        x_position = start[1]
        y_position = start[0]
        legal_moves = []

        j = y_position
        for i in range(x_position+1, 8): #diagonal up to the right
            if j - 1 >= 0:
                if Chess.board[j-1][i] not in Chess.white and color == 'w':
                    legal_moves.append([j-1, i])
                elif Chess.board[j-1][i] not in Chess.black and color == 'b':
                    legal_moves.append([j-1,i])
                j -= 1
            else:
                break

        
        j = y_position
        for i in range(x_position-1, -1, -1): #diagonal up to the left
            if j - 1 >= 0:
                if Chess.board[j-1][i] not in Chess.white and color == 'w':
                    legal_moves.append([j-1, i])
                elif Chess.board[j-1][i] not in Chess.black and color == 'b':
                    legal_moves.append([j-1,i])
                j -= 1
            else:
                break
        
        j = y_position
        for i in range(x_position+1, 8): #diagonal down to the right
            if j + 1 < 8:
                if Chess.board[j+1][i] not in Chess.white and color == 'w':
                    legal_moves.append([j+1, i])
                elif Chess.board[j+1][i] not in Chess.black and color == 'b':
                    legal_moves.append([j+1,i])
                j += 1
            else:
                break

        j = y_position
        for i in range(x_position-1, -1, -1): #diagonal down to the right
            if j + 1 < 8:
                if Chess.board[j+1][i] not in Chess.white and color == 'w':
                    legal_moves.append([j+1, i])
                elif Chess.board[j+1][i] not in Chess.black and color == 'b':
                    legal_moves.append([j+1,i])
                j += 1
            else:
                break
        return legal_moves

    def pawn_move(start, color): # Checks if starting position then rest of positions
        x_position = start[1]
        y_position = start[0]
        legal_moves = []

        if color == 'b':

            if y_position == 1:
                if Chess.board[y_position+2][x_position] == '**':
                    legal_moves.append([y_position+2, x_position])

            if y_position + 1 < 8:

                if Chess.board[y_position+1][x_position] == '**':
                    legal_moves.append([y_position+1,x_position])
                
                if x_position + 1 < 8:
                    if Chess.board[y_position+1][x_position+1] not in Chess.black and Chess.board[y_position+1][x_position+1] != '**':
                        legal_moves.append([y_position+1,x_position+1])
                if x_position - 1 >= 0:
                    if Chess.board[y_position+1][x_position-1] not in Chess.black and Chess.board[y_position+1][x_position-1] != '**':
                        legal_moves.append([y_position+1,x_position-1])

        else:

            if y_position == 6:
                if Chess.board[y_position-2][x_position] == '**':
                    legal_moves.append([y_position-2, x_position])

            if y_position - 1 >= 0:

                if Chess.board[y_position-1][x_position] == '**':
                    legal_moves.append([y_position-1,x_position])
                
                if x_position + 1 < 8:
                    if Chess.board[y_position-1][x_position+1] not in Chess.white and Chess.board[y_position-1][x_position+1] != '**':
                        legal_moves.append([y_position-1,x_position+1])

                if x_position - 1 >= 0:        
                    if Chess.board[y_position-1][x_position-1] not in Chess.white and Chess.board[y_position-1][x_position-1] != '**':
                        legal_moves.append([y_position-1,x_position-1])

        return legal_moves

    def knight_move(start, color): # looks at L pattern for the night
        x_position = start[0]
        y_position = start[1]
        legal_moves = []

        if x_position + 2 < 8:

            if y_position + 1 < 8:
                if Chess.board[x_position+2][y_position+1] not in Chess.white and color == 'w':

                    legal_moves.append([x_position+2, y_position+1])

                elif Chess.board[x_position+2][y_position+1] not in Chess.black and color == 'b':

                    legal_moves.append([x_position+2, y_position+1])

            if y_position - 1 >= 0:
                if Chess.board[x_position+2][y_position-1] not in Chess.white and color == 'w':

                    legal_moves.append([x_position+2, y_position-1])

                elif Chess.board[x_position+2][y_position-1] not in Chess.black and color == 'b':

                    legal_moves.append([x_position+2, y_position-1])

        if x_position - 2 >= 0:
            if y_position + 1 < 8:
                if Chess.board[x_position-2][y_position+1] not in Chess.white and color == 'w':

                    legal_moves.append([x_position-2, y_position+1])

                elif Chess.board[x_position-2][y_position+1] not in Chess.black and color == 'b':

                    legal_moves.append([x_position-2, y_position+1])

            if y_position - 1 >= 0:
                if Chess.board[x_position-2][y_position-1] not in Chess.white and color == 'w':

                    legal_moves.append([x_position-2, y_position-1])

                elif Chess.board[x_position-2][y_position-1] not in Chess.black and color == 'b':

                    legal_moves.append([x_position-2, y_position-1])
        
        if y_position - 2 >= 0:
            if x_position + 1 < 8:
                if Chess.board[x_position+1][y_position-2] not in Chess.white and color == 'w':

                    legal_moves.append([x_position+1, y_position-2])

                elif Chess.board[x_position+1][y_position-2] not in Chess.black and color == 'b':

                    legal_moves.append([x_position+1, y_position-2])

            if x_position - 1 >= 0:
                if Chess.board[x_position-1][y_position-2] not in Chess.white and color == 'w':

                    legal_moves.append([x_position-1, y_position-2])

                elif Chess.board[x_position-1][y_position-2] not in Chess.black and color == 'b':

                    legal_moves.append([x_position-1, y_position-2])

        if y_position + 2 < 8:
            if x_position + 1 < 8:
                if Chess.board[x_position+1][y_position+2] not in Chess.white and color == 'w':

                    legal_moves.append([x_position+1, y_position+2])

                elif Chess.board[x_position+1][y_position+2] not in Chess.black and color == 'b':

                    legal_moves.append([x_position+1, y_position+2])

            if x_position - 1 >= 0:
                if Chess.board[x_position-1][y_position+2] not in Chess.white and color == 'w':

                    legal_moves.append([x_position-1, y_position+2])

                elif Chess.board[x_position-1][y_position+2] not in Chess.black and color == 'b':

                    legal_moves.append([x_position-1, y_position-+2])

        return legal_moves   

    def reset_board():
        Chess.board = [['bR','bN','bB','bQ','bK','bB','bN','bR'],['bP','bP','bP','bP','bP','bP','bP','bP',],
         ['**','**','**','**','**','**','**','**',],['**','**','**','**','**','**','**','**',],
    ['**','**','**','**','**','**','**','**',],['**','**','**','**','**','**','**','**',],['wP','wP','wP','wP','wP','wP','wP','wP',],
     ['wR','wN','wB','wQ','wK','wB','wN','wR']]
        Chess.turn = 1

    def print_board():
        print('')
        iteration = 8
        iteration_2 = 0
        for i in Chess.board:

            print(iteration, end = ' ')
            iteration -= 1
            iteration_2 += 1

            for j in i:
                print(j, end= ' ')
            print('') ## creates new line

            if iteration_2 == 8:
                print(' ', end=' ')
                for k in range(0,8):
                    print(chr(ord('a')+k), end='  ')
        print('\n')

    def process_move(starting_str, desired_str): ## returns a list of the move and desired position in numerical values
        for i in starting_str:  # gets position
            if i in Chess.letter_position:
                start_letter = Chess.letter_position[i]
            elif i in Chess.number_position:
                start_number = Chess.number_position[i]
        
        for i in desired_str: # gets position
            if i in Chess.letter_position:
                desired_letter = Chess.letter_position[i]
            elif i in Chess.number_position:
                desired_number = Chess.number_position[i]        
        move_list = [[start_number,start_letter], [desired_number, desired_letter]]

        return move_list

    
    def king_in_check(): ## Returns boolean value, This will be the hardest one with algorithms.
        ## An idea is to iterate through the list of positions of all the pieces and gather a list of all the moves and then check if the king of either king is within those moves
        ## A thought is this should be called every move to check making the pass through argument another function called king_move_in_check checking the next position
        ## Will basically be the same function but just comparing the future position
        white_moves = Chess.all_legal_moves_white()
        black_moves = Chess.all_legal_moves_black()
        white_king_position = Chess.king_positions()[0]
        black_king_position = Chess.king_positions()[1]
        
        for i in white_moves:
            if i != None:
                if black_king_position in i:
                    print('Black King in Check')
                    return True
        
        for i in black_moves:
            if i != None:
                if white_king_position in i:
                    print('White king in Check')
                    return True
        
        return False

    
    def king_positions():
        white_king = []
        black_king = []
        for i in range(0,8):
            for k in range(0,8):
                if Chess.board[i][k] == 'bK':
                    black_king = [i,k]
                elif Chess.board[i][k] == 'wK':
                    white_king = [i,k]
        return [white_king, black_king]
        
    
    def all_legal_moves_white(): ## Going to return all legal moves for white as an array used for comparison later
        white_moves = []
        for i in range(0, 8):
            for k in range(0, 8):
                position = [i,k]
                j = Chess.board[i][k]
                
                if j in Chess.white:
                    if j == 'wP':
                        white_moves.append(Chess.pawn_move(position, color='w'))
                    elif j == 'wN':
                        white_moves.append(Chess.knight_move(position, color='w'))
                    elif j == 'wB':
                        white_moves.append(Chess.bishop_move(position, color='w'))
                    elif j == 'wR':
                        white_moves.append(Chess.rook_move(position, color='w'))
                    elif j == 'wQ':
                        white_moves.append(Chess.queen_move(position, color='w'))
                    elif j == 'wK':
                        white_moves.append(Chess.king_move(position, color='w'))
        return white_moves

    def all_legal_moves_black():
        black_moves = []

        for i in range(0, 8):
            for k in range(0, 8):
                position = [i,k]
                j = Chess.board[i][k]

                if j in Chess.black:
                    if j == 'bP':
                        black_moves.append(Chess.pawn_move(position, color='b'))
                    elif j == 'bN':
                        black_moves.append(Chess.knight_move(position, color='b'))
                    elif j == 'bB':
                        black_moves.append(Chess.bishop_move(position, color='b'))
                    elif j == 'bR':
                        black_moves.append(Chess.rook_move(position, color='b'))
                    elif j == 'bQ':
                        black_moves.append(Chess.queen_move(position, color='b'))
                    elif j == 'bK':
                        black_moves.append(Chess.king_move(position, color='b'))

        return black_moves

    def moves_list_to_letters(move_list):## 2d list
        
        legal_moves = []
        for i in move_list:
            if i != None:
                for j in i:
                    string = Chess.number_to_letter[j[1]] + Chess.number_to_number[j[0]]
                    legal_moves.append(string)

        return legal_moves
                

    def king_in_checkmate(positon, color):
        pass

def main():
    game = Chess ## setting class instance to game

    game.print_board()
    game.set_move(starting_str = 'e2', desired_str='e4')
    game.print_board()
    print(game.king_in_check())
    

main()