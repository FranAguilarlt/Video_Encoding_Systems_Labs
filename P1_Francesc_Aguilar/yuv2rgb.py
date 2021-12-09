import numpy as np


def YUV2RGB(YUV):
    Y = YUV[0]
    U = YUV[1]
    V = YUV[2]

    # Here we observe the transform matrix to converto from YUV to RGB.
    B = 1.164 * (Y - 16) + 2.018 * (U - 128)
    G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128)
    R = 1.164 * (Y - 16) + 1.596 * (V - 128)

    return np.array([R, G, B])
