class Player:
    def __init__(self, name):
        self.location = 0
        self.name = name
        
    def __str__(self):
        return 'Player {} is on square {}'.format(self.name, self.location)

class SnakesLadders():

    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.current = 0
        self.stop_game = False
        
    @staticmethod
    def calculate_new_location(expected_location):
        ladders = [[2,38], [7,14], [8,31], [15,26], [21,42], [28,84], [36,44], [51,67], [71,91], [78,98], [87,94]]
        snakes = [[16,6], [46,25], [49,11], [62,19], [64,60], [74,53], [89,68], [92,88], [95,75], [99,80]]
        if expected_location > 100:
            expected_location = 100 - (expected_location - 100)
        for i in ladders:
            if expected_location == i[0]:
                return i[1]
        for i in snakes:
            if expected_location == i[0]:
                return i[1]
        return expected_location

    def play(self, die1, die2):
        if self.stop_game:
            return 'Game over!'
        pl = self.players[self.current]
        pl.location = self.calculate_new_location(pl.location + die1 + die2)
        if pl.location == 100:
            self.stop_game = True
            return 'Player %i Wins!' %pl.name
        if not die1 == die2:
            self.current = 0 if self.current else 1
        return str(pl)
         