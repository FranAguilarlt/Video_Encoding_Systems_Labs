import numpy as np


def RGB2YUV(R, G, B):
    # This is the matrix of format conversion.Returns the formatted value YUV.
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128
    return np.array([Y, U, V])
