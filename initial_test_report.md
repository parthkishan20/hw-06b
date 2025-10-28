| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| TC01 | (0, 1, 1) | InvalidInput | InvalidInput | Pass |
| TC02 | (-1, 2, 2) | InvalidInput | InvalidInput | Pass |
| TC03 | (2, -1, 2) | InvalidInput | InvalidInput | Pass |
| TC04 | (2, 2, -1) | InvalidInput | InvalidInput | Pass |
| TC05 | (201, 10, 10) | InvalidInput | InvalidInput | Pass |
| TC06 | (10, 201, 10) | InvalidInput | InvalidInput | Pass |
| TC07 | (10, 10, 201) | InvalidInput | InvalidInput | Pass |
| TC08 | (3.5, 4, 5) | InvalidInput | InvalidInput | Pass |
| TC09 | ('3', 4, 5) | InvalidInput | **Error: TypeError** | Fail |
| TC10 | (1, 1, 3) | NotATriangle | InvalidInput | Fail |
| TC11 | (1, 3, 1) | NotATriangle | InvalidInput | Fail |
| TC12 | (3, 1, 1) | NotATriangle | InvalidInput | Fail |
| TC13 | (1, 2, 3) | NotATriangle | InvalidInput | Fail |
| TC14 | (2, 3, 1) | NotATriangle | InvalidInput | Fail |
| TC15 | (3, 1, 2) | NotATriangle | InvalidInput | Fail |
| TC16 | (1, 1, 1) | Equilateral | InvalidInput | Fail |
| TC17 | (200, 200, 200) | Equilateral | InvalidInput | Fail |
| TC18 | (2, 2, 3) | Isosceles | InvalidInput | Fail |
| TC19 | (2, 3, 2) | Isosceles | InvalidInput | Fail |
| TC20 | (3, 2, 2) | Isosceles | InvalidInput | Fail |
| TC21 | (4, 6, 9) | Scalene | InvalidInput | Fail |
| TC22 | (5, 6, 7) | Scalene | InvalidInput | Fail |
| TC23 | (3, 4, 5) | Right | InvalidInput | Fail |
| TC24 | (5, 4, 3) | Right | InvalidInput | Fail |
| TC25 | (4, 5, 3) | Right | InvalidInput | Fail |
| TC26 | (5, 12, 13) | Right | InvalidInput | Fail |
| TC27 | (13, 12, 5) | Right | InvalidInput | Fail |
| TC28 | (12, 13, 5) | Right | InvalidInput | Fail |
