from class_position import Position

class Floor(Position):
    '''A class that contains the floor block.'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        
    @property    
    def sprite(self):
        return (0, 32, 104, 16, 16)