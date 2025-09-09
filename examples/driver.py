import numpy as np
from my_python_package.operators import (
    add,
    multiply,
    divide,
    exp
)

def main():
    # test for scalars
    print(f'add(1, 3): {add(1, 3)}')
    print(f'multiply(2, 12.): {multiply(2, 12.)}')
    # test for arrays
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = 2. * np.ones(A.shape)
    print(f'A:\n{A}')
    print(f'B:\n{B}')
    print(f'add(A, B):\n{add(A, B)}')
    print(f'multiply(A, B):\n{multiply(A, B)}')

def polygon_unc():
    # multiply the perimeter of the polygon by the spatial resolution to get the standard uncertainty
    print(f'the standard uncertainty is {multiply(322, 25)}')
    ux = multiply(322,25)

    # divide the random pixel error (up to 1 pixel in this case) by 2 to get the exponent for the correction factor.
    e = divide(1, 2)

    # calculate the correction factor by raising the number of vertices in the polygon to the power of the previously calculated expponent
    cf = exp(37, e)

    # multiple the correction factor by the standard uncertainty
    print(f'the standard uncertainty with the correction factor applied is {multiply(cf, ux)}')

if __name__ == '__main__':
    main()
    polygon_unc()
