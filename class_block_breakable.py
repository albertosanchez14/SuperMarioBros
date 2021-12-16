from class_position import Position


class Breakable(Position):
    '''This class contains the standard breakable block'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        return (0, 0, 16, 16, 16)

    