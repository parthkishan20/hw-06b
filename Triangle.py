# -*- coding: utf-8 -*-
"""
Correct triangle classification with robust input validation.
"""

def classifyTriangle(a, b, c):
    """
    Classify a triangle given three side lengths (integers).

    Returns one of:
        'Equilateral'   : all three sides equal
        'Isosceles'     : exactly two sides equal
        'Scalene'       : no sides equal
        'Right'         : Pythagorean triple (any order)
        'NotATriangle'  : violates triangle inequality
        'InvalidInput'  : non-integers, non-positive, or > 200
    """

    # 1) TYPE CHECK FIRST
    # If any side is not an integer (e.g., str or float), we can't safely
    # compare with numbers or do arithmetic (like a > 200), so return InvalidInput.
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # 2) RANGE & POSITIVITY CHECKS
    # The assignment spec typically restricts sides to 1..200 (inclusive).
    # If a side is <= 0 or > 200, it's invalid.
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # 3) TRIANGLE INEQUALITY
    # For any triangle, the sum of any two sides must be STRICTLY greater
    # than the third. If not, it's NotATriangle (e.g., 1,2,3 or 1,1,3)
    if not (a + b > c and a + c > b and b + c > a):
        return 'NotATriangle'

    # 4) EQUILATERAL CHECK
    # If all three sides are equal, it's Equilateral (this must be tested
    # BEFORE isosceles/scalene/right; equilateral is a special, exclusive case).
    if a == b == c:
        return 'Equilateral'

    # 5) RIGHT-TRIANGLE CHECK
    # Sort sides so x <= y <= z; then test Pythagoras: x^2 + y^2 == z^2
    # Sorting makes the check work regardless of side order (3,4,5) or (5,4,3).
    x, y, z = sorted([a, b, c])
    if x * x + y * y == z * z:
        return 'Right'

    # 6) ISOSCELES VS SCALENE
    # If exactly two sides are equal -> Isosceles, otherwise -> Scalene.
    if a == b or b == c or a == c:
        return 'Isosceles'

    return 'Scalene'
