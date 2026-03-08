from matrix import Matrix

#Reference: https://www.mathsisfun.com/algebra/matrix-determinant.html

def remove_row(matrix: Matrix, i: int) -> Matrix:
    new_vals = [row[:] for idx, row in enumerate(matrix.vals) if idx != i]
    return Matrix(new_vals)

def remove_column(matrix: Matrix, j: int) -> Matrix:
    new_vals = [[val for col, val in enumerate(row) if col != j] for row in matrix.vals]
    return Matrix(new_vals)

def minor(matrix: Matrix, i: int, j: int) -> Matrix:
    #removes from matrix row i and col j
    return remove_column(remove_row(matrix, i), j)



def determinant(matrix: Matrix):

    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"Determinant can only be calculated for square matrix!")

    n = matrix.shape[0]

    #base case
    if n == 1:
        return matrix[0,0]

    det = 0
    for j in range(matrix.shape[1]):

        if j % 2 == 0: #positive if order number is odd
            det += matrix[0, j] * determinant(minor(matrix, 0, j))
        
        else:
            #negative if order number is even
            det -= matrix[0, j] * determinant(minor(matrix, 0, j))
        
    return det

#===========TEST===========
if __name__ == "__main__":
    # 2x2 singular
    assert determinant(Matrix([[1., -1.], [-1., 1.]])) == 0.

    # 3x3 diagonal
    assert determinant(Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])) == 8.

    # 3x3
    assert determinant(Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])) == -174.

    # 4x4
    assert determinant(Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])) == 1032.

    print("All tests passed!")
