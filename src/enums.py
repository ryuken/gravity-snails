class TurnStatus(object):
    BREAK = 1
    CURRENTTURN = 2
    
class Direction(object):
    UP, DOWN, LEFT, RIGHT = range(4)
    #UP = 1
    #DOWN = 2
    #LEFT = 3
    #RIGHT = 4
    
class GameModes(object):
    INIT = 1
    MENU_MAIN = 2
    GAME_PLACING_SNAILS = 3
    GAME_PLAYING = 4
    GAME_WINNING = 5