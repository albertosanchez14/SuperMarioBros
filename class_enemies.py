from pyxel import RESOURCE_FILE_EXTENSION
from class_position import Position
import random


class Enemies(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)    
        self.__sense = True   # sense = True -> left sense
                              # sense = False -> right sense
        self.velocity = 2
        self.__coordinates = []
        self.__enemy_type = random.randint(1, 100)
        
        # If the sprite is the one the Koopa, the y will be higher
        # because the Koopa is taller
        if self.sprite == (0, 48, 32, 16, 24, 12):       
            self.y -= 8        

    @property
    def sprite(self):
        if self.__enemy_type <= 75:
            return (0, 32, 48 , 16, 16, 12) # Goomba's sprite
        else:
            return (0, 48, 32, 16, 24, 12)  # Koopa's sprite    


        
    def displacement(self, size_x: int, list_of_objects: int):
        '''A method to make the enemies move
        @param size_x_x: width of the screen
        @param list_of_objects: a list with all the blocks as objects (ex. engame_crossover)
        ''' 
        if self.x < size_x:
            # If the enemy is going to the left  
            if self.__sense:
                self.__coordinates.clear()
                for i in range(len(list_of_objects)):
                    # Fill self.__coordinates with the lower coordinates of
                    # the list_of_objects
                    list_of_objects[i].coordinates_right(self.__coordinates)
                if [self.x, self.y] in self.__coordinates:
                    # Change direction
                    self.__sense = False
                elif [self.x, self.y + self.sprite[4] - 2] in self.__coordinates:
                    # Change direction
                    self.__sense = False
                else:
                    # Enemy moves
                    self.x -= self.velocity
            # If the enemy is going to the right
            elif not self.__sense:
                self.__coordinates.clear()
                for i in range(len(list_of_objects)):
                    # Fill self.__coordinates with the left coordinates of
                    # the list_of_objects
                    list_of_objects[i].coordinates_left(self.__coordinates)
                if [self.x + self.sprite[3], self.y] in self.__coordinates:
                    # Change direction
                    self.__sense = True
                elif [self.x + self.sprite[3], self.y + self.sprite[4] - 2] in self.__coordinates:
                    # Change direction
                    self.__sense = True
                else:
                    # Enemy moves
                    self.x += self.velocity        
            
            # Doing the gravity movement
            self.__coordinates.clear()
            for i in range(len(list_of_objects)):
                # Fill self.__coordinates with the up coordinates of
                # the list_of_objects
                list_of_objects[i].coordinates_up(self.__coordinates)
            # When there is no colision
            if not ([self.x, self.y + self.sprite[4]] and 
            [self.x + self.sprite[3] - 2, self.y + self.sprite[4]]) in self.__coordinates:
                # Gravity
                self.y += 4
            
            
