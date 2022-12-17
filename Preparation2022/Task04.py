# This solution provides several versions of functions, only one version is required for the test.
# The functions __str__, __eq__, __hash__ are provided for information only as well as the comments,
# they are not required for the test.

from typing import Tuple, List


class Matrix2Dim:
    """
    The class Matrix2Dim is composed of a pair of integers that represent the size of both the dimensions.
    The elements of the two-dimensional matrix are stored in a list of lists. This representation is not
    ideal because there is no guaranty that the sub-lists have the same length, this is one reason of the
    package NumPy. In this exercise we assume that all the sub-lists of 'elements' have the right size.
    """

    def __init__(self, dimensions: Tuple[int, int], elements: List[List[float]]) -> None:
        """ Constructor

        :param dimensions: tuple (pair) of the size of both the dimensions
        :param elements: content of the matrix (list of list of floats)
        """
        self.dimensions = dimensions
        self.elements = elements

    def __str__(self):
        """
        Defines the way that class instance should be displayed. The __str__ method is called when
        the following functions are invoked on the object and return a string: print() and str().
        Without this function print() displays a class instance as an object and not as a
        human-readable way.

        :return: the human-readable string of a class instance (object)
        """
        output = "(" + str(self.dimensions[0]) + ", " + str(self.dimensions[1]) + ")" + "\n"
        for line in self.elements:
            for element in line:
                output += "|" + str(element) + "|"
            output += "\n"
        return output

    def __eq__(self, other) -> bool:
        """
        The comparison operator '==' compares two objects according to their value. 'is' operator compares
        objects according ot their identity. Two objects have the same identity when they are identical, i.e. they
        are stored in the same memory space. To compare two object according to their content and not if they are
        identical it is necessary to define the method '__eq__' that specifies how the contents (attributes) are
        compared.  Note that for predefined data structures, .e.g List, Dictionaries, etc., the '__eq__' is already
        defined, in other words one can compare two lists based on their content with '=='. Consult the Python
        documentation for more information about the differences between 'is', '==', '__eq__'.

        :param other: the other object to compare
        :return: true if the content of the two objects is the same, false otherwise.
        """
        if not isinstance(other, Matrix2Dim):
            return False
        return self.dimensions == other.dimensions and self.elements == other.elements

    def __hash__(self):
        """
        The '__hash__' function MUST be defined if the '__eq__' function is defined to guaranty that
        if two objects are the same the '__hash__' function must return the same hash value. A correct hash value
        is essential for hashable data structure such as hash tables, hash maps, etc. For more information
        consult the Python documentation.

        :return: hash value
        """
        return hash((self.dimensions, self.elements))

    # classic solution
    def transpose(self):
        """
        Performs the matrix transposition based on swapping row and column.
        Because List in Python is mutable it is necessary to reserve the space of the transposed matrix before
        the copy swapping row and column. This avoids the exceptions "out of bounds".

        :return: the transposed matrix
        """
        transposed_elements = []
        for i in range(self.dimensions[1]):                # reserve the space for the transposed elements
            line = []
            for j in range(self.dimensions[0]):
                line.append(0)
            transposed_elements.append(line)

        for i in range(self.dimensions[0]):                # perform the transposition swapping the indexes
            for j in range(self.dimensions[1]):
                transposed_elements[j][i] = self.elements[i][j]
        return Matrix2Dim((self.dimensions[1], self.dimensions[0]), transposed_elements) # the final transposed matrix

    def transpose2(self):
        """
        Performs the matrix transposition using list comprehension.

        :return: the transposed matrix
        """
        # construction of the transposed list of lists using list comprehension.
        # observe how rows and columns are swapped, no need to reserve space.
        transposed_elements = \
            [[self.elements[j][i] for j in range(len(self.elements))] for i in range(len(self.elements[0]))]
        return Matrix2Dim((self.dimensions[1], self.dimensions[0]), transposed_elements)

    def is_symmetric(self) -> bool:
        """
        Determine if a matrix is symmetric or not. First verifies that the matrix is a square-matrix, then
        verify if the elements at postion [i][j] are equals to those at [j][i].

        :return: true if the matrix is symmetric, false otherwise
        """
        if self.dimensions[0] != self.dimensions[1]:  # is a square matrix, return false if not
            return False
        symmetric = True
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                symmetric &= self.elements[i][j] == self.elements[j][i]
        return symmetric

    # use the property symmetry <=> transpose = transpose transpose (2 times)
    def is_symmetric2(self) -> bool:
        """
        Determine is a matrix is symmetric or not using the property:  transposition two times of a matrix = matrix.
        Note that it is necessary to define the function '__eq__' to compare the matrix with the transposition

        :return: true if the matrix is symmetric, false otherwise
        """
        if self.dimensions[0] != self.dimensions[1]:  # is a square matrix, return false if not
            return False
        return self == self.transpose2().transpose2()


def main():
    matrix2_3 = Matrix2Dim((2, 3), [[10, 11, 12], [13, 14, 15]])
    print(f"matrix 2x3: \n{matrix2_3}")
    matrix2_2 = Matrix2Dim((2, 2), [[10, 11], [11, 55]])
    print(f"matrix 2x2: \n{matrix2_2}")

    print("matrix 2x3 is symmetric:" + str(matrix2_3.is_symmetric2()))
    print("matrix 2x2 is symmetric:" + str(matrix2_2.is_symmetric2()))

    print("transpostion of matrix 2x3")
    print(matrix2_3.transpose())

if __name__ == "__main__":
    main()