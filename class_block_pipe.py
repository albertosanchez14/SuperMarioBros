from class_position import Position


class Pipe(Position):
    '''This class contains the Pipe block'''
    def __init__(self, x: int, y: int, pipe_size: str ='low'):
        '''
        @param pipe_size: an str parameter to introduce the size of the 
        pipe desired. The program accepts 'low' or 'mid' or 'high'.
        '''
        super().__init__(x, y)
        self.pipe_size = pipe_size
    
    @property 
    def pipe_size(self):
        return self.__pipe_size
    @pipe_size.setter
    def pipe_size(self, pipe_size):
        if type(pipe_size) != str:
            raise TypeError('pipe_size must be a str')
        elif pipe_size != 'low' and pipe_size != 'mid' and pipe_size != 'high':
            raise ValueError('pipe_size value not accepted')
        else:
            self.__pipe_size = pipe_size
               
    @property
    def sprite(self):
        if self.pipe_size == 'low':
            return (0, 32, 0, 32, 32, 6)
        elif self.pipe_size == 'mid':
            return (0, 0, 152, 32, 48, 6)
        elif self.pipe_size == 'high':
            return (0, 32, 152, 32, 64, 6)
        else:
            raise ValueError('Error in the pipe_size input')
    