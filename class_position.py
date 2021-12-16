class Position:
    """This class defines the position of any object in the game"""
    def __init__(self, x, y):
        '''
        @param x: the coordinates of x
        @param y: the coordinates of y
        '''
        self.x = x 
        self.y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        else:
            self.__y = y
            
    def coordinates_up(self, lista_to_append: list):
        '''This  function creates a list with the top side coordinates of the
        objects in the list introduced.
        @param lista_to_append: list to append the values of the coordinates
        ''' 
        for i in range(0, self.sprite[3], 2):
            cord = [self.x + i, self.y]
            lista_to_append.append(cord)

    def coordinates_left(self, lista_to_append: list):
        '''This  function creates a list with the left side coordinates of the
        objects in the list introduced.
        @param lista_to_append: list to append the values of the coordinates
        '''
        for i in range(0, self.sprite[4], 2):   # self.sprite[4] because we want the lenght of the y's 
            cord = [self.x, self.y + i]
            lista_to_append.append(cord)
        
    def coordinates_right(self, lista_to_append: list):
        '''This  function creates a list with the right side coordinates of the
        objects in the list introduced.
        @param lista_to_append: list to append the values of the coordinates
        '''
        for i in range(0, self.sprite[4], 2):   # self.sprite[4] because we want the lenght of the y's 
            cord = [self.x + self.sprite[3], self.y + i]
            lista_to_append.append(cord)    
    
    def coordinates_down(self, lista_to_append: list):
        '''This  function creates a list with the bottom side coordinates of the
        objects in the list introduced.
        @param lista_to_append: list to append the values of the coordinates
        '''
        for i in range(0, self.sprite[3], 2):
            cord = [self.x + i, self.y + 15]
            lista_to_append.append(cord)
