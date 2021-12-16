from class_position import Position


class Rigid(Position):
    '''This class contains the rigis blocks'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        return 0, 0, 200, 16, 16
