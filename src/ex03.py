from matrix import Vector

def dot_product(v1: Vector, v2: Vector) -> float:
    Vector.check_shapes(v1, v2)

    return sum(v1[i] * v2[i] for i in range(len(v1)))

#===========TEST===========
if __name__ == "__main__":
    assert dot_product(Vector([0., 0.]), Vector([1., 1.])) == 0.
    assert dot_product(Vector([1., 1.]), Vector([1., 1.])) == 2.
    assert dot_product(Vector([-1., 6.]), Vector([3., 2.])) == 9.

    print("All tests passed!")
