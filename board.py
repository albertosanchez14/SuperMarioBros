from class_header import Header
from class_mario import Mario
from class_block_breakable import Breakable
from class_block_floor import Floor
from class_block_pipe import Pipe
from class_block_question import QuestionBlck
from class_block_rigid import Rigid
from class_decoration import Decoration
from class_enemies import Enemies
from class_block_coins import CoinsBlck
from class_mini_coins import MiniCoins
from class_power_ups import PowerUps

import pyxel


class Board:
    """ This class contains all the information needed to represent the
    board"""

    def __init__(self, width: int, height: int):
        """ The parameters are the width and height of the board"""
        self.width = width
        self.height = height
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(int(round(self.width / 2) / 2), 215)
        
        # This creates the header at (30,10)
        self.header = Header(30, 10)

        # We create a list with all floor bolcks.
        self.floor = []
        for i in range(0, 500, 16):
            self.floor.append(Floor(i, self.height - 8))
            self.floor.append(Floor(i, self.height - 24))
        for i in range(560, 816, 16):
            self.floor.append(Floor(i, self.height - 8))
            self.floor.append(Floor(i, self.height - 24))
        for i in range(880, 3000, 16):
            self.floor.append(Floor(i, self.height - 8))
            self.floor.append(Floor(i, self.height - 24))

        # We create a list with the positions of the bricks
        self.brick = [Breakable(272, 151), Breakable(288, 167), Breakable(304, 167),
                      Breakable(320, 167), Breakable(336, 167), Breakable(352, 167),
                      Breakable(368, 151),
                      Breakable(288, 87), Breakable(352, 87),
                      Breakable(640, 167), Breakable(672, 167),
                      Breakable(704, 103), Breakable(720, 103), Breakable(736, 103),
                      Breakable(752, 103), Breakable(768, 103), Breakable(784, 103),
                      Breakable(800, 103), Breakable(816, 103), Breakable(832, 103),
                      Breakable(896, 103), Breakable(912, 103), Breakable(928, 103),
                      Breakable(1040, 167), Breakable(1056, 167),
                      Breakable(2016, 103), Breakable(2032, 103), Breakable(2048, 103),
                      Breakable(2128, 103), Breakable(2176, 103), Breakable(2144, 167),
                      Breakable(2160, 167)]
        
        self.brick_coin = [CoinsBlck(944, 167), CoinsBlck(944, 167), CoinsBlck(1968, 167)]

        # Revisar si este sirve para algo
        self.condition = 0

        # We create a list with the positions of the pipes
        self.pipes_low = [Pipe(448, 199, 'low'), Pipe(1392, 199, 'low')]
        self.pipes_mid = [Pipe(1488, 183, 'mid')]
        self.pipes_high = [Pipe(1584, 167, 'high')]

        # We create a list with the position of the question blocks
        self.question = [QuestionBlck(320, 103, 'mushroom'),
                         QuestionBlck(656, 167, 'coin'),
                         QuestionBlck(944, 103, 'coin'),
                         QuestionBlck(1168, 167, 'coin'), QuestionBlck(1232, 167, 'coin'), QuestionBlck(1296, 167, 'coin'),
                         QuestionBlck(1232, 103, 'mushroom'),
                         QuestionBlck(2144, 103, 'coin'), QuestionBlck(2160, 103, 'coin')]

        self.rigid = [Rigid(1728, 215), Rigid(1744, 215), Rigid(1760, 215),
                      Rigid(1776, 215), Rigid(1824, 215), Rigid(1840, 215),
                      Rigid(1856, 215), Rigid(1872, 215),
                      Rigid(1744, 199), Rigid(1760, 199), Rigid(1776, 199),
                      Rigid(1824, 199), Rigid(1840, 199), Rigid(1856, 199),
                      Rigid(1760, 183), Rigid(1776, 183),
                      Rigid(1824, 183), Rigid(1840, 183),
                      Rigid(1776, 167),
                      Rigid(1824, 167),
                      Rigid(2304, 215), Rigid(2320, 215), Rigid(2336, 215),
                      Rigid(2352, 215), Rigid(2368, 215), Rigid(2384, 215),
                      Rigid(2400, 215), Rigid(2416, 215), Rigid(2432, 215),

                      Rigid(2320, 199), Rigid(2336, 199), Rigid(2352, 199),
                      Rigid(2368, 199), Rigid(2384, 199), Rigid(2400, 199),
                      Rigid(2416, 199), Rigid(2432, 199),

                      Rigid(2336, 183), Rigid(2352, 183), Rigid(2368, 183),
                      Rigid(2384, 183), Rigid(2400, 183), Rigid(2416, 183),
                      Rigid(2432, 183),

                      Rigid(2352, 167), Rigid(2368, 167), Rigid(2384, 167),
                      Rigid(2400, 167), Rigid(2416, 167), Rigid(2432, 167),

                      Rigid(2368, 151), Rigid(2384, 151), Rigid(2400, 151),
                      Rigid(2416, 151), Rigid(2432, 151),

                      Rigid(2384, 135), Rigid(2400, 135), Rigid(2416, 135),
                      Rigid(2432, 135),

                      Rigid(2400, 119), Rigid(2416, 119), Rigid(2432, 119),

                      Rigid(2416, 103), Rigid(2432, 103)]

        # Create the clouds in a periodic way, we will give them now the class
        # of decoration, and later on we will draw them as clouds with the
        # corresponding method
        self.cloud = []
        for i in range(0, 3000, 287):
            self.cloud.append(Decoration(i, 40))  # At height y = 40
        for i in range(143, 3000, 287):
            self.cloud.append(Decoration(i, 50))  # At height y = 50

        # Create the bushes in a periodic way x = 174
        self.bush = []
        for i in range(20, 3000, 174):
            if i == 542:
                self.bush.append(Decoration(560, 255 - 40))
            else:
                self.bush.append(Decoration(i, 255 - 40))
        
        # List to store all the power ups
        self.power_ups = []
        
        # List with the enemies
        self.enemies = [Enemies(320, 151), Enemies(720, 87), Enemies(752, 87),
                        Enemies(1104, 215), Enemies(1152, 215), Enemies(1360, 215), Enemies(1456, 215),
                        Enemies(1552, 215)]

        # Final castle
        self.castle = [2544, 155, 0, 64, 0, 60, 76]

        # Counter for the timer
        self.__contador = 0

        # List with all of the blocks
        self.blocks_endgame_type_epic_crossover = self.floor + self.brick + self.question + \
                                             self.pipes_low + self.pipes_mid + self.pipes_high + \
                                             self.rigid + self.brick_coin
        self.__counter_coins = 0
        self.mini_coins = []
        self.points = 0
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('x from board must be an integer')
        elif width < 0:
            raise ValueError('x from board must be positive')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('y from board must be an integer')
        elif height < 0:
            raise ValueError('y from board must be positive')
        else:
            self.__height = height   

    def update(self):
        # Collision of Mario with the enemies
        self.mario.collision_enemies(self.width, self.enemies)

        # Movement of the enemies
        for i in range(len(self.enemies)):
            self.enemies[i].displacement(self.width, self.blocks_endgame_type_epic_crossover)

        # If Q is pressed the game will finish
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Mario moves to the ++++++++++++++++++++ RIGHT +++++++++++++++++++++++
        if pyxel.btn(pyxel.KEY_RIGHT):
            # We move mario, and right method also generates a list with the
            # the coordinates for the colisions
            self.mario.right(self.blocks_endgame_type_epic_crossover)
            # Collision of Mario with the enemies
            self.mario.collision_enemies(self.width, self.enemies)
            # If Mario is in the middle everything will move to the left
            if self.mario.x == int(128):
                for i in range(len(self.brick)):
                    self.brick[i].x -= self.mario.velocity
                for i in range(len(self.floor)):
                    self.floor[i].x -= self.mario.velocity
                for i in range(len(self.pipes_low)):
                    self.pipes_low[i].x -= self.mario.velocity
                for i in range(len(self.pipes_mid)):
                    self.pipes_mid[i].x -= self.mario.velocity
                for i in range(len(self.pipes_high)):
                    self.pipes_high[i].x -= self.mario.velocity
                for i in range(len(self.question)):
                    self.question[i].x -= self.mario.velocity
                for i in range(len(self.rigid)):
                    self.rigid[i].x -= self.mario.velocity
                for i in range(len(self.cloud)):
                    self.cloud[i].x -= self.mario.velocity
                for i in range(len(self.bush)):
                    self.bush[i].x -= self.mario.velocity
                for i in range(len(self.enemies)):
                    self.enemies[i].x -= self.mario.velocity
                for i in range(len(self.power_ups)):
                    self.power_ups[i].x -= self.mario.velocity
                for i in range(len(self.brick_coin)):
                    self.brick_coin[i].x -= self.mario.velocity
                for i in range(len(self.mini_coins)):
                    self.mini_coins[i].x -= self.mario.velocity
                self.castle[0] -= self.mario.velocity

        # Mario moves to the ++++++++++++++++++++ LEFT ++++++++++++++++++++++++
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.left(self.blocks_endgame_type_epic_crossover)
            
            self.mario.collision_enemies(self.width, self.enemies)
        # Mini Mario returns to the original sprite
        else:
            if self.mario.phase == "MiniMario":
                self.mario.sprite = (0, 0, 48, 16, 16, 6)

        # Mario jumps
        if ((pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE))
                and self.mario.counter_y < 96 and self.mario.can_jump):
            colision_blck = self.mario.jump(self.blocks_endgame_type_epic_crossover)
            if isinstance(colision_blck, Breakable):
                self.points += 50
            elif isinstance(colision_blck, QuestionBlck) and colision_blck != None:
                self.power_ups.append(colision_blck.creation_power_up())
                if colision_blck.content == 'mushroom':
                    self.points += 1000
                elif colision_blck.content == 'coin':
                    self.points += 200
            elif isinstance(colision_blck, CoinsBlck) and colision_blck != None:
                self.mini_coins.append(colision_blck.creation_mini_coin())
                self.points += 200
        else:
            self.mario.gravity(self.blocks_endgame_type_epic_crossover)
    
        counter_in_list = 0
        for i in range(len(self.power_ups)):
            if isinstance(self.power_ups[i], PowerUps):
                if self.power_ups[i].power_up_type == 'coin':
                    counter_in_list += 1
        for i in range(len(self.mini_coins)):
            if isinstance(self.mini_coins[i], MiniCoins):
                if self.mini_coins[i].coins_left >= 0:
                    counter_in_list += 1

        self.__counter_coins = counter_in_list
                
        # We set the counter to 1/30 which is a second 
        self.__contador += 1 / 30

    
    def draw(self):
        pyxel.cls(6)

        # We draw the header
        self.header.counter_points(self.points)
        self.header.counter_coins(self.__counter_coins)
        self.header.world()
        self.header.timer(self.__contador)

        # We draw one cloud
        for i in range(len(self.cloud)):
            pyxel.blt(self.cloud[i].x, self.cloud[i].y, *self.cloud[i].cloud())

        # We draw a bush
        for i in range(len(self.bush)):
            pyxel.blt(self.bush[i].x, self.bush[i].y, *self.bush[i].bush())

        # We draw the blocks
        for i in range(len(self.blocks_endgame_type_epic_crossover)):
            pyxel.blt(self.blocks_endgame_type_epic_crossover[i].x, self.blocks_endgame_type_epic_crossover[i].y, *self.blocks_endgame_type_epic_crossover[i].sprite)
        
        # We draw the tubes
        for i in range(len(self.pipes_low)):
            pyxel.blt(self.pipes_low[i].x, self.pipes_low[i].y, *self.pipes_low[i].sprite)
        for i in range(len(self.pipes_mid)):
            pyxel.blt(self.pipes_mid[i].x, self.pipes_mid[i].y, *self.pipes_mid[i].sprite)
        for i in range(len(self.pipes_high)):
            pyxel.blt(self.pipes_high[i].x, self.pipes_high[i].y, *self.pipes_high[i].sprite)

        # We draw the rigid blocks
        for i in range(len(self.rigid)):
            pyxel.blt(self.rigid[i].x, self.rigid[i].y, *self.rigid[i].sprite)
        
        # We draw the enemies
        for i in range(len(self.enemies)):
            pyxel.blt(self.enemies[i].x, self.enemies[i].y, *self.enemies[i].sprite)
        
        # We draw the power ups
        for i in range(len(self.power_ups)):
            pyxel.blt(self.power_ups[i].x, self.power_ups[i].y, *self.power_ups[i].sprite)
        
        # We draw the mini coins
        for i in range(len(self.mini_coins)):
            pyxel.blt(self.mini_coins[i].x, self.mini_coins[i].y, *self.mini_coins[i].sprite)

        # We draw the final castle
        pyxel.blt(*self.castle)

        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, *self.mario.sprite)
