import math #lets us use the math lib
import unittest #lib to test functions easily

def circleArea(radius): 
    return math.pi * radius * radius

def rectArea(base, height):
    return base * height

def trapArea(base1, base2, height):
    return height * abs( (base1 + base2) / 2)

def triArea(base,height):
    return (base * height)/2
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest modual
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25 * math.pi)
    def testRectArea(self):
        self.assertEqual(rectArea(3, 10), 30)
    def testTrapArea(self):
        self.assertEqual(trapArea(14, 20, 12), 204)
    def testTriArea(self):
        self.assertEqual(triArea(6, 6), 18)
    