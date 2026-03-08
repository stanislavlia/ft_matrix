from matrix import Vector
from ex03 import dot_product
from ex04 import norm

def angle_cos(v1: Vector, v2: Vector):
    
    if v1.is_zero_vector() or v2.is_zero_vector():
        raise ValueError("Cos is undefined")


    cos = dot_product(v1, v2) / (norm(v1) * norm(v2))
    return cos


#===========TEST===========
if __name__ == "__main__":
    assert round(angle_cos(Vector([1., 0.]), Vector([1., 0.])), 6) == 1.0
    assert round(angle_cos(Vector([1., 0.]), Vector([0., 1.])), 6) == 0.0
    assert round(angle_cos(Vector([-1., 1.]), Vector([1., -1.])), 6) == -1.0
    assert round(angle_cos(Vector([2., 1.]), Vector([4., 2.])), 6) == 1.0
    assert round(angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.])), 6) == round(0.974631846, 6)

    print("All tests passed!")

