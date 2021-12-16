from class_position import Position


class Decoration(Position):
    '''In this class are stored the clouds and the bushes'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def cloud(self):
        # Cloud at bank 0, pos 16, 64, size, 48, 24, bckgnd color: 13
        self.__sprite = (0, 16, 64, 48, 24, 13)
        return self.__sprite
    
    def bush(self):
        # Bush at bank 0, pos 16, 88, size, 48, 16, bckgnd color: 6
        self.__sprite = (0, 16, 88, 48, 16, 12)
        return self.__sprite