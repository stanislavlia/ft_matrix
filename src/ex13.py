from matrix import Matrix
from ex10 import row_echelon

def rank(matrix: Matrix):

    rref_matrix = row_echelon(matrix=matrix)

    non_zero_rows_count = 0
    for i in range(rref_matrix.shape[0]):

        row = rref_matrix.get_row(i)
        if any([v != 0 for v in row]):
            non_zero_rows_count += 1
        
    return non_zero_rows_count

#===========TEST===========
if __name__ == "__main__":
    # Identity: rank 3
    assert rank(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])) == 3

    # Rank-deficient 3x4
    assert rank(Matrix([[1., 2., 0., 0.], [2., 4., 0., 0.], [-1., 2., 1., 1.]])) == 2

    # 4x3, rank 3
    assert rank(Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.], [21., 18., 7.]])) == 3

    print("All tests passed!")

