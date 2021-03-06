import unittest
import sys
sys.path.append("../")
from liste.liste import liste, cell

class Test_liste(unittest.TestCase):

    def setUp(self) -> None:
        self.__liste = liste()
        self.__first = cell("first")
        self.__second = cell("second")
        self.__third = cell("third")

    def tearDown(self):
        pass
        
    def test_isEmpty(self):
        self.assertTrue(self.__liste.isEmpty())

    def test_addFirstWithEmptyList(self):
        self.__liste.addFirst(self.__first)
        self.assertTrue(self.__liste.getFirst() is self.__first)

    def test_addLastWithEmptyList(self):
        self.__liste.addLast(self.__second)
        self.assertTrue(self.__liste.getFirst() is self.__second)

    def test_addFirst(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addFirst(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__third)
        self.assertTrue(self.__liste.getLast() is self.__first)

    def test_addLast(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addLast(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__second)
        self.assertTrue(self.__liste.getLast() is self.__third)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    