from class_position import Position
from class_power_ups import PowerUps


class QuestionBlck(Position):
    '''This class contains the Question Block'''
    def __init__(self, x: int, y: int, content: str):        
        '''
        @param content: an str parameter that indicates the thing that is  
        inside the question block. The program acceptes 'mushroom' or 'coin'
        '''
        super().__init__(x, y)
        self.broken = False
        self.content = content            
         
    @property
    def sprite(self):
        if self.broken == False:
            return (0, 16, 0, 16, 16)
        else:
            return (0, 16, 16, 16, 16)
    
    @property
    def broken(self):
        return self.__broken
    @broken.setter
    def broken(self, broken):
        if type(broken) != bool:
            raise TypeError('broken must be a bool')
        else:
            self.__broken = broken

    @property
    def content(self):
        return self.__content
    @content.setter 
    def content(self, content):
        if content != 'mushroom' and content != 'coin':
            raise ValueError('content parameter should be mushroom or coin')
        else:
            self.__content = content

    def creation_power_up(self):
        # Returns the class PowerUps with the same x and y-16
        return PowerUps(self.x, self.y - 16, self.content)

