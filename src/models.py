

class Person:
    '''Base Class for person'''

    def __init__(self, x, y, symbol):
        '''Initialises The person at a location with the symbol'''
        self.x = x
        self.y = y
        self.symbol = symbol
    '''The below functions are for moving. 
    No checking is done to see if the move is permitted.'''

    def move_up(self):

        self.y += 1

    def move_down(self):

        self.y -= 1

    def move_right(self):

        self.x += 1

    def move_left(self):

        self.x -= 1


class Bomberman(Person):
    '''Bomberman class. Additional functions to drop bombs 
    and other features have to be added'''

    def __init__(self):
        Person.__init__(self, 1, 1, "B")


class Enemy(Person):
    '''Enemy class. Functions to move have to be created.'''

    def __init__(self, x, y):
        Person.__init__(self, x, y, "E")


class Cell:
    '''Class for cell which is the basic unit of the board'''

    def __init__(self, obj=None, name=None, symbol=" "):
        self.obj = obj
        self.name = name
        self.symbol = symbol


class Bomb:
    '''Class for Bombs'''

    def __init__(self, x, y, frame):
        self.x = x
        self.y = y
        self.frame = frame
        self.symbol = "B"


class Brick:
    '''Class for Brick'''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = "/"
