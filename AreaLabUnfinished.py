import math #lets us use the math lib
import unittest #lib to test functions easily

def circleArea(radius): 
    return math.pi * radius * radius

def rectArea(base, height):
    return base * height

def trapArea(base1, base2, height):
    return height * (base1 + base2) / 2

def triArea(base,height):
    return (base * height)/2
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest modual
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25 * math.pi)
        self.assertAlmostEqual(circleArea(3.25), 33.1830724035)
    def testRectArea(self):
        self.assertEqual(rectArea(3, 10), 30)
        self.assertEqual(rectArea(5, 12), 60)
    def testTrapArea(self):
        self.assertEqual(trapArea(14, 20, 12), 204)
        self.assertEqual(trapArea(10, 20, 2), 30)
    def testTriArea(self):
        self.assertEqual(triArea(6, 6), 18)
        self.assertEqual(triArea(10, 10), 50)
    