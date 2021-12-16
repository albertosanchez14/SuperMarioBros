from class_position import Position


class PowerUps(Position):
    def __init__(self, x: int, y: int, power_up_type: str):
        '''
        @param power_up_type: type of power up
        '''
        super().__init__(x, y)
        self.power_up_type = power_up_type
        
    @property
    def sprite(self):
        if self.power_up_type == 'mushroom':
            return (0, 0, 32, 16, 16, 6)
        elif self.power_up_type == 'coin':
            return (0, 0, 216, 16, 16, 6)
        

    