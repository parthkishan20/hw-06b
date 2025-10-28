# -*- coding: utf-8 -*-
"""
Enhanced unit tests for classifyTriangle().
Covers: invalid inputs, triangle inequality, and all triangle classes
(Right, Scalene, Isosceles, Equilateral) with permutations and boundaries.
"""

import unittest
from Triangle import classifyTriangle

class TestTrianglesEnhanced(unittest.TestCase):

    # ---------- Invalid input tests ----------
    def test_invalid_zero_or_negative(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput')
        self.assertEqual(classifyTriangle(2, -1, 2), 'InvalidInput')
        self.assertEqual(classifyTriangle(2, 2, -1), 'InvalidInput')

    def test_invalid_over_max(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput')
        self.assertEqual(classifyTriangle(10, 201, 10), 'InvalidInput')
        self.assertEqual(classifyTriangle(10, 10, 201), 'InvalidInput')

    def test_invalid_non_integer(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle('3', 4, 5), 'InvalidInput')

    # ---------- Not a triangle (triangle inequality) ----------
    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 3, 1), 'NotATriangle')
        self.assertEqual(classifyTriangle(3, 1, 1), 'NotATriangle')
        # edge boundary: sum equals third -> not a triangle
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle')
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle')

    # ---------- Equilateral ----------
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    # ---------- Isosceles (not right) ----------
    def test_isosceles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isosceles')
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles')

    # ---------- Scalene (not right) ----------
    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 6, 9), 'Scalene')
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene')

    # ---------- Right triangles (all permutations) ----------
    def test_right_3_4_5(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    def test_right_5_12_13(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right')
        self.assertEqual(classifyTriangle(12, 13, 5), 'Right')

    def test_right_isosceles_legs(self):
        # 1,1,sqrt(2) would be right-isosceles but sides must be integers, so skip fractional hypotenuse
        # Ensure nearby integer triple that's not right is not misclassified
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle')

if __name__ == '__main__':
    unittest.main()
