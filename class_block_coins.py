from class_position import Position
from class_mini_coins import MiniCoins


class CoinsBlck(Position):
    '''This class contains the breakable blocks that contain coins inside
    them.'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        # self.broken = broken
        self.coins_left = 4
        
    @property
    def sprite(self):
        # If the are no coins left then the sprite changes to a clear block
        if self.coins_left <= 0:
            return (0, 16, 16, 16, 16)
        # Othewise, it mantains as a breakable block            
        else:
            return (0, 0, 16, 16, 16)

    def creation_mini_coin(self):
        '''This method creates some mini coins on the top of the CoinsBlock
        object, it is called when an collision occurs.'''
        return MiniCoins(self.x, self.y - 16, self.coins_left)

