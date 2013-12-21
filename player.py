

class Player(object):
    name = ""
    country = ""
    average = 0.00
    matches = 0

    def __init__(self):
        self.name = "Cricket Player"
        self.country = "None"
        self.average = 0.00
        self.matches = 0

    def print_info(self):
        print "Name: {}, Country {}, Played {}, Average {}.".format(self.name, 
            self.country, self.matches, self.average);

class Bowler(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = "Bowler"


class Batsman(Player): 
    def __init__(self):
        Player.__init__(self)
        self.name = "Batsman"
        self.country = "EN"
        self.average = "51.59"

