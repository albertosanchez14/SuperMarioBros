from class_position import Position

class MiniCoins(Position):
    def __init__(self, x: int, y: int, coins_left: str):
        '''
        @param coins_left: a parameter that indicates the number of coins left
        in the breakable block with coins. It is protected with a setter to give
        the values desired.
        '''
        super().__init__(x, y)
        self.coins_left = coins_left
    
    @property
    def coins_left(self):
        return self.__coins_left
    @coins_left.setter
    def coins_left(self, coins_left):
        if coins_left < 0:
            self.__coins_left = -1  # We stablish -1 because later on we see
                                    # that the sprite for <= 0 is the one with
                                    # four mini coins
        else:
            self.__coins_left = coins_left

    @property
    def sprite(self):
        if self.coins_left == 3:
            return (1, 0, 0, 16, 16, 6)
        if self.coins_left == 2:
            return (1, 16, 0, 16, 16, 6)
        if self.coins_left == 1:
            return (1, 32, 0, 16, 16, 6)
        if self.coins_left <= 0:
            return (1, 48, 0, 16, 16, 6)
        