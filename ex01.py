from matrix import Vector
from typing import List

def linear_combination(vectors: List[Vector], coeffs: List[float]) -> Vector:
    if len(vectors) != len(coeffs):
        raise ValueError("vectors and coeffs must be the same length")
    if len(vectors) == 0:
        raise ValueError("vectors list must not be empty")

    return sum(vectors[i] * coeffs[i] for i in range(len(coeffs)))

#===========TEST===========
if __name__ == "__main__":
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    assert linear_combination([e1, e2, e3], [10., -2., 0.5]).vals == [10., -2., 0.5]

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    assert linear_combination([v1, v2], [10., -2.]).vals == [10., 0., 230.]

    print("All tests passed!")
