import unittest
import sys
sys.path.append("../")

from Point.Point import point

class Test_Point:
    def setUp(self) -> None:
        self.__x=x
        self.__y=y
        
    def tearDown(self):
        pass
        
    def test_getx(self):
        return self.__x
    
    def test_gety(self):
        return self.__y
    
    def test_setx(self,value):
        self.__x=value
        
    def test_sety(self,value):
        self.__y=value   


#assert isinstance(x, float) and x>=0 #ajouter limites de taille ecran et temps si tems est dans classe point
#assert isinstance(y, float) and y>=0