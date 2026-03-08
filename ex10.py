from matrix import Matrix, Vector
from ex04 import abs

EPS=1e-14 #small constant


def row_echelon(matrix: Matrix):
    """Gaussian Elimination"""

    #deepcopy
    matrix_copy = Matrix([row[:] for row in matrix.vals]) 

    pivot_row = 0

    for j in range(matrix_copy.shape[1]):
        
        max_abs_value = 0
        max_row_idx = 0

        #find row with max abs value in j column
        for i in range(pivot_row, matrix_copy.shape[0]):
            
            if abs(matrix_copy[i, j]) > max_abs_value:
                max_abs_value = abs(matrix_copy[i, j])
                max_row_idx = i
            
        if max_abs_value < EPS:
            #skip column
            continue
        
        #swap max_row with pivot_row
        matrix_copy.swap_rows(pivot_row, max_row_idx)

        #Now row with max value is at pivot_row index
        #Make values zero below pivot row
        

        #normalize pivot row so leading entry is 1
        pivot_val = matrix_copy[pivot_row, j]
        matrix_copy.set_row(
            matrix_copy.get_row(pivot_row) * (1 / pivot_val), idx=pivot_row
        )


        #Elimination below and above pivot row
        for i in range(matrix_copy.shape[0]):
            if i == pivot_row:
                continue


            factor = matrix_copy[i, j] / matrix_copy[pivot_row, j]

            matrix_copy.set_row(
                matrix_copy.get_row(i) - factor * matrix_copy.get_row(pivot_row), idx=i
            )
                

        pivot_row += 1
    
    return matrix_copy

def round_matrix(m, decimals=6):
    return [[round(v, decimals) for v in row] for row in m.vals]

#===========TEST===========
if __name__ == "__main__":
    assert row_echelon(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])).vals == [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]
    assert row_echelon(Matrix([[1., 2.], [3., 4.]])).vals == [[1., 0.], [0., 1.]]
    assert row_echelon(Matrix([[1., 2.], [2., 4.]])).vals == [[1., 2.], [0., 0.]]

    r = row_echelon(Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]]))
    assert round_matrix(r) == [[1., 0.625, 0., 0., -12.166667], [0., 0., 1., 0., -3.666667], [0., 0., 0., 1., 29.5]]

    print("All tests passed!")
