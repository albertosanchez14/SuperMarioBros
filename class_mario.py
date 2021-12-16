from class_block_breakable import Breakable
from class_block_coins import CoinsBlck
from class_block_question import QuestionBlck
from class_power_ups import PowerUps


class Mario:
    """ This class stores all the information needed for Mario"""

    def __init__(self, x: int, y: int):
        """ This method creates the Mario object
        @param x the starting x of Mario
        @param y the starting y of Mario
        """
        self.x = x
        self.y = y
        self.sprite = (0, 0, 48, 16, 16, 6)
        self.phase = 'MiniMario'  # Phase of mario (MiniMario, SuperMario)
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3
        # We declare a counter to later set a max of y's to do on a jump and
        # jumping to see if it is jumping.
        self.counter_y = 0
        # We declare a variable that establish if mario can jump
        self.can_jump = True
        # Counter to change the sprite of Mario when walking
        self.__posR = 1
        self.__posL = 1
        self.velocity = 2
        if self.phase == 'SuperMario':
            self.y -= 16

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        if type(sprite) != tuple:
            raise TypeError('sprite should be a tuple')
        else:
            self.__sprite = sprite

    def right(self, object_list: list):
        '''Method for right movement of Mario.
        @param object_list: a list with the blocks.
        '''
        entities_left = []
        # Fill entitities_left with the left coordinates of object
        for i in range(len(object_list)):
            object_list[i].coordinates_left(entities_left)
        # Collision of Mario with blocks
        if [self.x + self.sprite[3], self.y] in entities_left:
            self.x = self.x - self.velocity
        elif [self.x + self.sprite[3], self.y + self.sprite[4] - 2] in entities_left:
            self.x = self.x - self.velocity

        # Mario animations and movement to the right
        if self.__posR == 1:
            # Mario moves
            self.x += self.velocity
            # Change the sprite depending on the state
            if self.phase == 'MiniMario':
                self.sprite = (0, 16, 120, 16, 16, 6)
            elif self.phase == 'SuperMario':
                self.sprite = (0, 0, 72, 16, 32, 6)
        elif self.__posR == 5:
            # Mario moves
            self.x += self.velocity
            # Change the sprite depending on the state
            if self.phase == 'MiniMario':
                self.sprite = (0, 0, 120, 16, 16, 6)
            elif self.phase == 'SuperMario':
                self.sprite = (0, 0, 72, 16, 32, 6)
        elif self.__posR == 10:
            # Mario moves
            self.x += self.velocity
            # Change the sprite depending on the state
            if self.phase == 'MiniMario':
                self.sprite = (0, 32, 120, 16, 16, 6)
            elif self.phase == 'SuperMario':
                self.sprite = (0, 0, 72, 16, 32, 6)
        else:
            # Mario moves
            self.x += self.velocity
        # Counter to make the animations of Mario
        self.__posR += 1
        if self.__posR == 15:
            self.__posR = 1

        # If x position of Mario is in the middle it is not going to move
        if self.x >= 128:
            # Collision of Mario with blocks
            if [self.x + self.sprite[3], self.y] in entities_left:
                self.x = self.x - self.velocity
            elif [self.x + self.sprite[3], self.y + self.sprite[4] - 2] in entities_left:
                self.x = self.x - self.velocity
            else:
                self.x = 128

    def left(self, object_list: list):
        '''Method for left movement of Mario.
        @param object_list: a list with the blocks.
        '''
        entities_right = []
        # Fill entitities_right with the left coordinates of object
        for i in range(len(object_list)):
            object_list[i].coordinates_right(entities_right)
        # Collision of Mario with blocks
        if [self.x, self.y] in entities_right:
            self.x = self.x + self.velocity
        elif [self.x, self.y + self.sprite[4] - 2] in entities_right:
            self.x = self.x + self.velocity

        # Mario animations and movement to the left
        if self.x > 0:
            if (self.x > 0) and self.__posL == 1:
                # Mario moves
                self.x -= self.velocity
                # Change the sprite depending on the state
                if self.phase == 'MiniMario':
                    self.sprite = (0, 16, 136, 16, 16, 6)
                elif self.phase == 'SuperMario':
                    self.sprite = (0, 0, 72, 16, 32, 6)
            elif (self.x > 0) and self.__posL == 5:
                # Mario moves
                self.x -= self.velocity
                # Change the sprite depending on the state
                if self.phase == 'MiniMario':
                    self.sprite = (0, 0, 136, 16, 16, 6)
                elif self.phase == 'SuperMario':
                    self.sprite = (0, 0, 72, 16, 32, 6)
            elif (self.x > 0) and self.__posL == 10:
                # Mario moves
                self.x -= self.velocity
                # Change the sprite depending on the state
                if self.phase == 'MiniMario':
                    self.sprite = (0, 32, 136, 16, 16, 6)
                elif self.phase == 'SuperMario':
                    self.sprite = (0, 0, 72, 16, 32, 6)
            else:
                # Mario moves
                self.x -= self.velocity

        # Counter to make the animations of Mario
        self.__posL += 1
        if self.__posL == 15:
            self.__posL = 1

    def gravity(self, object_list: list):
        '''Method for gravity movement of Mario.
        @param object_list: a list with the blocks.
        '''
        enitity_up = []
        for i in range(len(object_list)):
            object_list[i].coordinates_up(enitity_up)

        if [self.x, self.y + self.sprite[4]] in enitity_up:
            self.can_jump = True
            self.counter_y = 0
        elif [self.x + self.sprite[3] - 2, self.y + self.sprite[4]] in enitity_up:
            self.can_jump = True
            self.counter_y = 0
        else:
            self.y += 4
            self.can_jump = False
            if self.phase == 'MiniMario':
                self.sprite = (0, 48, 104, 16, 16, 6)
            elif self.phase == 'SuperMario':
                self.sprite = (0, 0, 72, 16, 32, 6)

    def jump(self, object_list: list):
        '''Method for jump movement of Mario.
        @param object_list: a list with the blocks.
        '''
        colision = False    # We declare that by default there is no colision
        entities_down = []
        for i in range(len(object_list) - 1, -1, -1):   # We check colisions
            object_list[i].coordinates_down(entities_down)
            if [self.x, self.y - 1] in entities_down:
                self.counter_y = 96
                colision = True
            elif [self.x + self.sprite[3] - 2, self.y - 1] in entities_down:
                self.counter_y = 96
                colision = True
            # Now we are going to check the colisions depending on the type of 
            # the block we are coliding with we will do one thing or other.
            if [self.x + self.sprite[3] / 2, self.y - 1] in entities_down:
                if self.phase == 'SuperMario':    
                    if isinstance(object_list[i], Breakable):
                        extracted_object = object_list.pop(i)
                        return extracted_object
                if isinstance(object_list[i], QuestionBlck):
                    if not object_list[i].broken == True:  
                        object_list[i].broken = True
                        if object_list[i].content == 'mushroom':
                            self.phase = 'SuperMario'
                        return object_list[i]
                if isinstance(object_list[i], CoinsBlck):
                    object_list[i].coins_left -= 1
                    return object_list[i]
            entities_down.clear()
        
        # If no colision Mario will continue jumping
        if not colision:
            self.y -= 8
            if self.phase == 'MiniMario':
                self.sprite = (0, 48, 104, 16, 16, 6)
            elif self.phase == 'SuperMario':
                self.sprite = (0, 0, 72, 16, 32, 6)
            self.counter_y += 8

    def collision_enemies(self, size_x: int, enemies: list):
        '''Method for gravity movement of Mario.
        @param size_x: width of the sreen
        @param enemies: a list with the enemies.
        '''
        coords_up = []
        coords_right = []
        coords_left = []
        coords_down = []

        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].x < size_x:
                enemies[i].coordinates_up(coords_up)
                enemies[i].coordinates_right(coords_right)
                enemies[i].coordinates_left(coords_left)
                enemies[i].coordinates_down(coords_down)

                # Check if the lower coordinates of Mario are the same as the upper coordinates
                # of Goomba and Koopa
                if [self.x, self.y + self.sprite[4]] in coords_up:
                    # Delete the enemy from the list
                    del (enemies[i])
                elif [self.x + self.sprite[3] - 2, self.y + self.sprite[4]] in coords_up:
                    # Delete the enemy from the list
                    del (enemies[i])

                # Check if the left coordinates of Mario are the same as the right coordinates
                # of Goomba and Koopa
                if [self.x, self.y] in coords_right[i]:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 0, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 0, 16, 16, 6):  # Small Mario
                        self.lives -= 1
                elif [self.x, self.y + self.sprite[4] - 2] in coords_right:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 0, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 0, 16, 16, 6):  # Small Mario
                        self.lives -= 1

                # Check if the right coordinates of Mario are the same as the left coordinates
                # of Goomba and Koopa
                if [self.x + self.sprite[3], self.y] in coords_left:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 48, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 48, 16, 16, 6):  # Small Mario
                        self.lives -= 1
                elif [self.x + self.sprite[3], self.y + self.sprite[4] - 2] in coords_left:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 0, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 48, 16, 16, 6):  # Small Mario
                        self.lives -= 1

                # Check if the upper coordinates of Mario are the same as the down coordinates
                # of Goomba and Koopa
                if [self.x, self.y - 1] in coords_down:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 48, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 48, 16, 16, 6):  # Small Mario
                        self.lives -= 1
                elif [self.x + self.sprite[3] - 2, self.y - 1] in coords_down:
                    # Transforms Big Mario into Small Mario
                    if self.sprite == (0, 0, 72, 16, 32, 6):  # Big Mario
                        self.sprite == (0, 0, 48, 16, 16, 6)
                    # Subtract 1 live
                    elif self.sprite == (0, 0, 48, 16, 16, 6):  # Small Mario
                        self.lives -= 1

                # We clear the list of coordinates
                coords_up.clear()
                coords_right.clear()
                coords_left.clear()
                coords_down.clear()
