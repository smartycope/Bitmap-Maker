from Game import Game
import argparse

description = ''
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-v' , '--verbose' , action='store_true')
args = parser.parse_args()

game = Game(args=args, size=[310, 455])
game.run()
game.currentScene.exit()