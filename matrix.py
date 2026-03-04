from typing import List



class Vector():
    def __init__(self, vals=List[int|float]):

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

    def __repr__(self):
        return self.__str__()

    #=========OPERATORS============
    def __neg__(self):
        return Vector([-v for v in self.vals])

    def __add__(self, other):

        if isinstance(other, (float, int)):
            new_vals = [v + other for v in new_vals]
            return Vector(new_vals)
    
        if isinstance(other, Vector):
            self.check_shapes(self, other)

            new_vals = [self[i] + other[i] for i in range(len(self.vals))]
            return Vector(new_vals)
        
        raise NotImplementedError("This type is not supported")
    
    def __sub__(self, other):
        return self.__add__(-other)



