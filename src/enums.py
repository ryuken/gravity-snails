class TurnStatus(object):
    """
    An enum to check the current turn status of TurnManager
    """
    BREAK = 1
    CURRENTTURN = 2

class Direction(object):
    """
    An enum used for setting gravity directions.
    """
    UP, DOWN, LEFT, RIGHT = range(4)
    #UP = 1
    #DOWN = 2
    #LEFT = 3
    #RIGHT = 4

class GameModes(object):
    """
    An enum for the various game modes
    """
    INIT = 1
    MENU_MAIN = 2
    MENU_SETTINGS = 3
    GAME_PLACING_SNAILS = 4
    GAME_PLAYING = 5
    GAME_WINNING = 6