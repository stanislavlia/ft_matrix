from matrix import Matrix


def transpose(matrix: Matrix) -> Matrix:


    transpose_mat_vals = []
    
    #convert columns into rows
    for j in range(matrix.shape[1]):

        col_vals = list(matrix.get_column(j))
        transpose_mat_vals.append(col_vals)

    return Matrix(transpose_mat_vals)

#===========TEST===========
if __name__ == "__main__":
    # Square identity - unchanged
    assert transpose(Matrix([[1., 0.], [0., 1.]])).vals == [[1., 0.], [0., 1.]]

    # Non-square 2x4 -> 4x2
    assert transpose(Matrix([[1., 2., 3., 4.], [5., 6., 7., 8.]])).vals == [[1., 5.], [2., 6.], [3., 7.], [4., 8.]]

    # Square 3x3
    assert transpose(Matrix([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])).vals == [[1., 4., 7.], [2., 5., 8.], [3., 6., 9.]]

    print("All tests passed!")