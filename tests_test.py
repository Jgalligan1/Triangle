import unittest
import triangle
import math

class TriangleTest(unittest.TestCase):
    def test_Equilateral(self):
        self.assertEqual(triangle.Triangle.classify_Triangle(1,1,1),"not right Equilateral")
        self.assertEqual(triangle.Triangle.classify_Triangle(4,4,4),"not right Equilateral")
        self.assertEqual(triangle.Triangle.classify_Triangle(.5,.5,.5),"not right Equilateral")
    def test_Isosceles(self):
        self.assertEqual(triangle.Triangle.classify_Triangle(1,4,4),"not right Isosceles")
        self.assertEqual(triangle.Triangle.classify_Triangle(7,7,1),"not right Isosceles")
        self.assertEqual(triangle.Triangle.classify_Triangle(100,50,100),"not right Isosceles")
    def test_Scalene(self):
        self.assertEqual(triangle.Triangle.classify_Triangle(1,2,3),"not right Scalene")
        self.assertEqual(triangle.Triangle.classify_Triangle(5,8,4),"not right Scalene")
        self.assertEqual(triangle.Triangle.classify_Triangle(20,13,43),"not right Scalene")
    def test_Right(self):
        self.assertEqual(triangle.Triangle.classify_Triangle(5,12,13),"right Scalene")
        self.assertEqual(triangle.Triangle.classify_Triangle(3,5,4),"right Scalene")
        self.assertEqual(triangle.Triangle.classify_Triangle(1,1,math.sqrt(2)),"right Isosceles")
        self.assertEqual(triangle.Triangle.classify_Triangle(3,3,math.sqrt(2)*3),"right Isosceles")



if __name__ == '__main__':
    unittest.main()