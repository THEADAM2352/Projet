class point:
    def __init__(self,x,y):
        #assert isinstance(x, float) and x>=0
        self.__x=x
        self.__y=y
        
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def setx(self,value):
        self.__x=value
        
    def sety(self,value):
        self.__y=value   