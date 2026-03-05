from typing import List



class Vector():
    def __init__(self, vals: List[int | float]):

        self.vals = vals
        self.shape = (len(vals), )

    def __str__(self):

        repr = ", ".join(map(str, self.vals))
        return f"Vector([{repr}])"
        
    @staticmethod
    def check_shapes(vec1, vec2):
        if vec1.shape != vec2.shape:
            raise ValueError("Vectors should be of the same shape")

    #========ITERATIONS==========
    def __getitem__(self, index):
        return self.vals[index]

    def __setitem__(self, index, value):
        self.vals[index] = value

    def __len__(self):
        return len(self.vals)

    def __repr__(self):
        return self.__str__()

    #=========OPERATORS============
    def __neg__(self):
        return Vector([-v for v in self.vals])

    def __add__(self, other):

        if isinstance(other, (float, int)):
            new_vals = [v + other for v in self.vals]
            return Vector(new_vals)
    
        if isinstance(other, Vector):
            self.check_shapes(self, other)

            new_vals = [self[i] + other[i] for i in range(len(self.vals))]
            return Vector(new_vals)
        
        raise NotImplementedError(f"This type is not supported for add operation: {type(other)}")
    
    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            new_vals = [v * other for v in self.vals]
            return Vector(new_vals)

        raise NotImplementedError(f"This type is not supported for mul operation: {type(other)}")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            return Vector([other - v for v in self.vals])
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)


class Matrix():
    def __init__(self, vals: List[List[float | int]]):
        
        self._validate(vals)
        self.vals = vals
        self.shape = (len(vals), len(vals[0]))
    
    @staticmethod
    def _validate(vals):
        if not vals or not vals[0]:
            raise ValueError("Matrix cannot be empty")
        row_len = len(vals[0])
        if not all(len(row) == row_len for row in vals):
            raise ValueError("All rows must be the same length")
    
    def __getitem__(self, index):
        row, col = index
        return self.vals[row][col]

    def __setitem__(self, index: tuple, value):
        row, col = index
        self.vals[row][col] = value
    
    def reshape(self, shape: tuple) -> 'Matrix':
        rows, cols = shape
        flat = [self.vals[i][j] for i in range(self.shape[0]) for j in range(self.shape[1])]
        if len(flat) != rows * cols:
            raise ValueError(f"Cannot reshape {self.shape} into {shape}")
        return Matrix([[flat[i * cols + j] for j in range(cols)] for i in range(rows)])
    
    def flatten(self) -> 'Vector':
        return Vector([self.vals[i][j] for i in range(self.shape[0]) for j in range(self.shape[1])])

    def __str__(self):
        rows = [", ".join(map(str, row)) for row in self.vals]
        return "Matrix([" + "], [".join(rows) + "])"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def check_shapes(m1, m2):
        if m1.shape != m2.shape:
            raise ValueError("Matrices should be of the same shape")

    def __add__(self, other):
        if isinstance(other, Matrix):
            self.check_shapes(self, other)
            new_vals = [[self.vals[i][j] + other.vals[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(new_vals)
        raise NotImplementedError(f"This type is not supported for add operation: {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            self.check_shapes(self, other)
            new_vals = [[self.vals[i][j] - other.vals[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(new_vals)
        raise NotImplementedError(f"This type is not supported for sub operation: {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            new_vals = [[self.vals[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(new_vals)
        raise NotImplementedError(f"This type is not supported for mul operation: {type(other)}")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            new_vals = [[other - self.vals[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(new_vals)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
