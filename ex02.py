from matrix import Vector, Matrix

V = float | Vector | Matrix

def lerp(v1: V, v2: V, t: float) -> V:
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1]")
    return v1 + (v2 - v1) * t

#===========TEST===========
if __name__ == "__main__":
    # Scalar examples from PDF
    assert lerp(0., 1., 0.) == 0.
    assert lerp(0., 1., 1.) == 1.
    assert lerp(0., 1., 0.5) == 0.5
    assert lerp(21., 42., 0.3) == 27.3

    # Vector example from PDF
    assert lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3).vals == [2.6, 1.3]

    # Matrix example from PDF
    assert lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5).vals == [[11., 5.5], [16.5, 22.]]

    print("All tests passed!")

