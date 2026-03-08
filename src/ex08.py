from matrix import Matrix


def trace(matrix: Matrix):
    #check if square matrix
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"Trace can be computed for square matrix only. Got shape {matrix.shape}")
    
    diag_sum = 0
    for i in range(matrix.shape[0]):
        diag_sum += matrix[i, i] #sum diagonal elements

    return diag_sum

#===========TEST===========
if __name__ == "__main__":
    assert trace(Matrix([[1., 0.], [0., 1.]])) == 2.
    assert trace(Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])) == 9.
    assert trace(Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]])) == -21.

    print("All tests passed!")
