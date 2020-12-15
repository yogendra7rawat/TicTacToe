from player import RandomComputerPlayer,HumanPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)];
        self.current_winner = None;



    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| "+" | ".join(row) + ' |')



    def print_numbers(self):
        number = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number:
            print("| "+" | ".join(row) + ' |')



    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == " "];


    def empty_squares(self):
        return ' ' in self.board;

    def num_empty_squares(self):
        empty  = len(self.available_moves());

        return 'empty squares are: {}'.format(empty);

    def make_moves(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter;
            if self.winner(square,letter):
                self.current_winner = letter;
            return True;
        return False;


    def winner(self,square,letter):
        row_ind = square//3;
        row = self.board[row_ind*3:(row_ind+1)*3];
        if(all([spot == letter for spot in row])):
            return True;

        #column
        col_ind = square%3;
        col = [self.board[col_ind+i*3] for i in range(3)]
        if(all([spot == letter for spot in col])):
            return True;

        #diag
        if(square%2==0):
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if(all([spot == letter for spot in diagonal1])):
                return True;



            diagonal2 = [self.board[i] for i in [2,4,6]]
            if(all([spot == letter for spot in diagonal2])):
                return True;

        return False;
        



def play(tictactoe,x_player,o_player,print_game = True):
    if print_game:
        tictactoe.print_numbers();

    letter = 'x';

    while tictactoe.empty_squares():
        if letter == 'o':
            square = o_player.get_moves(tictactoe);

        else:
            square = x_player.get_moves(tictactoe);




        if tictactoe.make_moves(square,letter):
            if(print_game):
                print(letter + f' make a move to a square {square}');
                tictactoe.print_board();


            if(tictactoe.current_winner):
                if(print_game):
                    print(letter+" Wins");
                return letter;

                    
            letter = 'o' if letter == 'x' else 'x'
            
    print("TIE");




if __name__ == '__main__':
    
    t = TicTacToe();
    x_player = HumanPlayer('x');
    o_player = RandomComputerPlayer('o');


    play(t,x_player,o_player,print_game = True);



