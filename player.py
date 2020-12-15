import math
import random



class Player:
    def __init__(self,letter):
        self.letter = letter;


    def get_moves(self):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_moves(self,tictactoe):
        square  = random.choice(tictactoe.available_moves());
        return square;


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_moves(self,tictactoe):
        valid_square = False;
        val = None;
        while not valid_square:
            square  = input(self.letter+ '\'s turn. Input moves from (0-8): ')

            try:
                val = int(square);
                if val not in tictactoe.available_moves():
                    raise ValueError;
                valid_square = True;

            except ValueError:
                x = "!ERROR Already Filled {} Position".format(val);
                print(x);


        return val;

        
