import math
import numpy as np




def dct(matrix):
    m, n = matrix.shape
    ci = 0
    cj = 0
    dct = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if i == 0:
                ci = 1 / math.sqrt(m)
            else:
                ci = math.sqrt(2) / math.sqrt(m)
            if j == 0:
                cj = 1 / math.sqrt(n)
            else:
                cj = math.sqrt(2) / math.sqrt(n)

            suma = 0

            for k in range(m):
                for l in range(n):
                    dct1 = matrix[k][l] * math.cos((2 * k + 1) * i * math.pi / (2 * m)) * math.cos((2 * l + 1) * j * math.pi / (2 * n))
                    suma += dct1
            dct[i, j] = ci * cj * suma
    return dct
