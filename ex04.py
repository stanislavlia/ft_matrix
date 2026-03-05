from matrix import Vector

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

#Manhattan Norm
def norm_1(v: Vector):
    
    norm = sum([
        abs(val) for val in v
    ])

    return norm

#Euclidean Norm
def norm(v: Vector):
    norm = sum([
        val**2 for val in v
    ])
    return norm ** 0.5 #sqrt

#Supremum norm
def norm_inf(v: Vector):
    return max([abs(val) for val in v])

#===========TEST===========
if __name__ == "__main__":
    assert norm_1(Vector([0., 0., 0.])) == 0.
    assert norm(Vector([0., 0., 0.])) == 0.
    assert norm_inf(Vector([0., 0., 0.])) == 0.

    assert norm_1(Vector([1., 2., 3.])) == 6.
    assert round(norm(Vector([1., 2., 3.])), 5) == round(3.74165738, 5)
    assert norm_inf(Vector([1., 2., 3.])) == 3.

    assert norm_1(Vector([-1., -2.])) == 3.
    assert round(norm(Vector([-1., -2.])), 5) == round(2.236067977, 5)
    assert norm_inf(Vector([-1., -2.])) == 2.

    print("All tests passed!")

