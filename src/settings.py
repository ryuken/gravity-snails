class Settings:
    """
    Settings which can be customized at the beginning of the game.
    All classes use this general settings class, which is similar to an enum.
    The values can be modified.
    """
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    SCREEN_COLOR = (0, 0, 64)
    # TIMER SETTINGS
    TIMER_SIZE = (40, 40)
    TIMER_POSITION = (0,0)
    TIMER_FONT_SIZE = 25
    TIMER_STARTTIME = 10
    TIMER_BREAKTIME = 3

    GAME_TITLE = "Gravity Snails"
    GAME_PLAYERS = 2
    GAME_SNAILS = 2
    GAME_SNAILS_HP = 100