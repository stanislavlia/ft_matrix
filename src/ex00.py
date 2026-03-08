from matrix import Vector, Matrix

V = Vector | Matrix #either Vector or Matrix

def add(v1: V, v2: V) -> V:
    return v1 + v2

def subtract(v1: V, v2: V) -> V:
    return v1 - v2

def scale(v1: V, scalar: float) -> V:
    return v1 * scalar

#===========TEST===========
if __name__ == "__main__":
    # Vector - PDF examples
    assert add(Vector([2., 3.]), Vector([5., 7.])).vals == [7., 10.]
    assert subtract(Vector([2., 3.]), Vector([5., 7.])).vals == [-3., -4.]
    assert scale(Vector([2., 3.]), 2.).vals == [4., 6.]

    # Matrix - PDF examples
    assert add(Matrix([[1., 2.], [3., 4.]]), Matrix([[7., 4.], [-2., 2.]])).vals == [[8., 6.], [1., 6.]]
    assert subtract(Matrix([[1., 2.], [3., 4.]]), Matrix([[7., 4.], [-2., 2.]])).vals == [[-6., -2.], [5., 2.]]
    assert scale(Matrix([[1., 2.], [3., 4.]]), 2.).vals == [[2., 4.], [6., 8.]]

    print("All tests passed!")

