from board import Board
import pyxel


SIZE_SCREEN_X = 255 
SIZE_SCREEN_Y = 255

board = Board(SIZE_SCREEN_X, SIZE_SCREEN_Y)

# The first thing to do is to create the screen, see API for more parameters
pyxel.init(board.width, board.height, caption="Super Mario Bros")
# Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
pyxel.load("mario_assets/marioassets.pyxres")
# To start the game we invoke the run method with the update and draw functions
pyxel.run(board.update, board.draw)
 