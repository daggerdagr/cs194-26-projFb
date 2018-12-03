import numpy as np
import skimage.filters

### laplacian

def multiResBlendOp(im1, im2, mask, levels, sigma):
    assert im1.shape == im2.shape == mask.shape

    L1 = laplacianPyrOp_3D(im1, levels, sigma)
    L2 = laplacianPyrOp_3D(im2, levels, sigma)
    LM = gaussStackOp_3D(mask, levels, sigma)

    #     for i in range(len(LM)):
    #         printImage(str(i) + ".png", LM[i])

    #     for i in range(len(L1)):
    #         printImage(str(i) + ".png", L1[i])
    LM1 = LM
    LM2 = (1 - LM1)

    L1_post = LM1 * L1
    L2_post = LM2 * L2

    finalL = L1_post + L2_post

    tes = np.zeros(L1[0].shape)

    for i in range(len(L1)):
        tes += finalL[i]

    tes2 = np.clip(tes, -1, 1)

    return tes2

def laplacianPyrOp_3D(im, levels, sigma, scaleB = False):
    gaussStack = gaussStackOp_3D(im, levels, sigma)

    for i in range(levels):
        res = gaussStack[i] - gaussStack[i+1]
        if scaleB:
            finalCurrLayer = (res - res.min()) / (res.max() - res.min())
        else:
            finalCurrLayer = res
        gaussStack[i] = finalCurrLayer

    return gaussStack

def gaussStackOp_3D(im, levels, sigma):
    assert levels > 0
    #inclusive of original img, at layer indexed 0

    result = []
    # newLayer = (lambda: np.zeros(im.shape))

    for i in range(levels+1):
        if i == 0:
            result.append(im)
            continue
        # currLayer = newLayer()
        currLayer = skimage.filters.gaussian(result[i - 1], sigma, mode="nearest")
        result.append(currLayer)

    return np.array(result)