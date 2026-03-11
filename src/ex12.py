from matrix import Matrix
from ex10 import row_echelon, round_matrix
from ex11 import determinant

def identity(n: int) -> Matrix:
    return Matrix([[1. if i == j else 0. for j in range(n)] for i in range(n)])

def hstack(m1: Matrix, m2: Matrix) -> Matrix:
    if m1.shape[0] != m2.shape[0]:
        raise ValueError(f"Row count mismatch: {m1.shape[0]} vs {m2.shape[0]}")
    return Matrix([m1.vals[i] + m2.vals[i] for i in range(m1.shape[0])])


def inverse(matrix: Matrix) -> Matrix:
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix should be square to compute inverse!")
    
    if determinant(matrix) == 0:
        raise ValueError("Matrix is not ivertible. det = 0")
    
    n = matrix.shape[0]
    
    #stack identity matrix horizontally
    i_matrix = identity(n)
    augmented_matrix = hstack(matrix, i_matrix)

    #now get reduced row echelon form of augmented matrix
    rref_augmented_matrix = row_echelon(augmented_matrix)

    #get the right half
    inverse_matrix = []
    for i in range(n):

        row = rref_augmented_matrix.get_row(i)[n:] #get only right half
        inverse_matrix.append(row)

    return Matrix(inverse_matrix)

def round_matrix(m, decimals=6):
    return [[round(v, decimals) for v in row] for row in m.vals]

#===========TEST===========
if __name__ == "__main__":
    # Identity inverse is identity
    assert inverse(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])).vals == [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]

    # Diagonal matrix
    r = inverse(Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]))
    assert r.vals == [[0.5, 0., 0.], [0., 0.5, 0.], [0., 0., 0.5]]

    # 3x3 from PDF
    r = inverse(Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]))
    rv = round_matrix(r, 6)
    assert rv == [[0.649425, 0.097701, -0.655172], [-0.781609, -0.126437, 0.965517], [0.143678, 0.074713, -0.206897]]

    # Singular matrix should raise
    try:
        inverse(Matrix([[1., 2.], [2., 4.]]))
        assert False, "Should have raised"
    except ValueError:
        pass

    print("All tests passed!")

