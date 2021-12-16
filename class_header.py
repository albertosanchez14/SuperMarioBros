from class_position import  Position
import pyxel

class Header(Position):
    '''In this class we configure the different types of headers'''
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.coins = 0

    def counter_points(self, points: int):
        '''
        @param points: an integer type parameter that gives the number of points
        at each frame.
        '''
        pyxel.text(self.x, self.y, "POINTS", 7)
        pyxel.text(self.x, self.y + 10, str(points), 7)
    
    def counter_coins(self, coins: int):
        '''
        @param coins: an integer type parameter that gives the number of coins
        picked until that point.
        '''
        pyxel.text(self.x + 50, self.y, "COINS", 7)
        pyxel.text(self.x + 50, self.y + 10, str(coins), 7)

    def world(self):
        pyxel.text(self.x + 110, self.y, "WORLD", 7)
        pyxel.text(self.x + 110, self.y + 10, "1-1", 7)

    def timer(self, time_passed: float):
        '''
        @param time_passed: an float type parameter that we will round later on
        and gives the time that has passed since the start of the game.
        '''
        pyxel.text(self.x + 170, self.y, "TIME", 7)
        pyxel.text(self.x + 170, self.y + 10, str(400 - round(time_passed)), 7)
 