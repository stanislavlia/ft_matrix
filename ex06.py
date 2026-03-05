from matrix import Vector

#finds a vector that is perpendicular to both v1 and v2
def cross_product(v1: Vector, v2: Vector) -> Vector:
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors")

    return Vector([
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ])

#===========TEST===========
if __name__ == "__main__":
    assert cross_product(Vector([0., 0., 1.]), Vector([1., 0., 0.])).vals == [0., 1., 0.]
    assert cross_product(Vector([1., 2., 3.]), Vector([4., 5., 6.])).vals == [-3., 6., -3.]
    assert cross_product(Vector([4., 2., -3.]), Vector([-2., -5., 16.])).vals == [17., -58., -16.]

    print("All tests passed!")
