from matrix import Vector, Matrix
from ex03 import dot_product

def mul_vec(matrix: Matrix, vector: Vector) -> Vector:
    
    #check dimensions
    if not matrix.shape[1] == vector.shape[0]:
        raise ValueError(f"Cannot multiply {matrix.shape} matrix by vector of size {vector.shape[0]}: columns ({matrix.shape[1]}) must match vector dimension ({vector.shape[0]})")
    
    res_vec_vals = []

    for i in range(matrix.shape[0]):

        row = matrix.get_row(i)
        val = dot_product(row, vector)
        res_vec_vals.append(val)

    return Vector(res_vec_vals)


def mul_mat(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    #check dimensions
    if not matrix1.shape[1] == matrix2.shape[0]:
        raise ValueError(f"Cannot multiply {matrix1.shape} by {matrix2.shape} matrix: columns of first ({matrix1.shape[1]}) must match rows of second ({matrix2.shape[0]})")
    

    res_matrix_vals = []

    for i in range(matrix1.shape[0]):

        row = []
        for j in range(matrix2.shape[1]):

            val = dot_product(matrix1.get_row(i),
                              matrix2.get_column(j))
            
            row.append(val)
        
        res_matrix_vals.append(row)

    return Matrix(res_matrix_vals)

#===========TEST===========
if __name__ == "__main__":
    # mul_vec PDF examples
    assert mul_vec(Matrix([[1., 0.], [0., 1.]]), Vector([4., 2.])).vals == [4., 2.]
    assert mul_vec(Matrix([[2., 0.], [0., 2.]]), Vector([4., 2.])).vals == [8., 4.]
    assert mul_vec(Matrix([[2., -2.], [-2., 2.]]), Vector([4., 2.])).vals == [4., -4.]

    # mul_mat PDF examples
    assert mul_mat(Matrix([[1., 0.], [0., 1.]]), Matrix([[1., 0.], [0., 1.]])).vals == [[1., 0.], [0., 1.]]
    assert mul_mat(Matrix([[1., 0.], [0., 1.]]), Matrix([[2., 1.], [4., 2.]])).vals == [[2., 1.], [4., 2.]]
    assert mul_mat(Matrix([[3., -5.], [6., 8.]]), Matrix([[2., 1.], [4., 2.]])).vals == [[-14., -7.], [44., 22.]]

    print("All tests passed!")
