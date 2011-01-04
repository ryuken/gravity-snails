from game import Game
from enums import Direction
game = Game()
game.addTeam('test', 2, Direction.UP)
game.addTeam('test2', 2, Direction.DOWN)
#game.addTeam('test', 2, Direction.LEFT)
#game.addTeam('test2', 2, Direction.RIGHT)
game.run()