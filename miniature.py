from region.image import Image
from outputMake import *
from utils import *
from scipy.interpolate import RegularGridInterpolator
from skimage.color import rgb2hsv, hsv2rgb

import numpy as np
import skimage

def createPolygon(im, polygonPts):
    finIm = np.zeros(im.imArr.shape[:2])
    if len(polygonPts) == 2:
        rr, cc,val = skimage.draw.line_aa(int(polygonPts[0][1]), int(polygonPts[0][0]), int(polygonPts[1][1]), int(polygonPts[1][0]))
        finIm[rr, cc] = val
    elif len(polygonPts) > 2:
        polyRR, polyCC = skimage.draw.polygon(polygonPts[:, 1], polygonPts[:, 0])
        finIm[polyRR, polyCC] = 1
    return finIm


def getGradientMask(im, sigma, points=None, printMask=False):
    emptyImage = createPolygon(im, points)

    if printMask:
        printImage("mask_start.jpg", emptyImage)

    res = skimage.filters.gaussian(emptyImage, sigma, mode="nearest")

    resMax = np.max(res)
    scaledRes = res * (1 / resMax)

    if printMask:
        printImage("mask_final.jpg", scaledRes)

    return scaledRes


def generateMask(im, maskStrength, maskPoints=None, objMask=False, objMaskPoints=None, debugB=False):
    if maskPoints is None:
        maskPoints = getPoints(im, -4, "Pick 2+ coords of line/area of gradient. Press ESC when done.")
        assert len(maskPoints) >= 2
    mask = getGradientMask(im, maskStrength, maskPoints, printMask=debugB)

    pathName = "p%i-mSig_%i-mObj_%s" % (len(maskPoints), maskStrength, objMask)

    if objMask:
        if objMaskPoints is None:
            objMaskPoints = getPoints(im, -1, "Pick 0+ coords off polygon for mask. Press ESC when done.")
        mask = np.clip(mask + createPolygon(im, objMaskPoints), 0, 1)
        if debugB:
            printImage("mask_%s_wObjM.jpg" % pathName, mask)

    maskIm = Image(pathName, mask)

    return maskIm


def maskedBlur(im, maskIm, largestBlurSigma, gaussLevelsCt):
    gaussStack = gaussStackOp_3D(im.imArr, gaussLevelsCt, largestBlurSigma / gaussLevelsCt)

    mask = maskIm.imArr

    levelsCoords = range(gaussLevelsCt + 1)
    rowsCoords = range(im.height)
    colsCoords = range(im.width)

    allR = gaussStack[:, :, :, 0]
    allG = gaussStack[:, :, :, 1]
    allB = gaussStack[:, :, :, 2]

    rInterpF = RegularGridInterpolator((levelsCoords, rowsCoords, colsCoords), allR)
    gInterpF = RegularGridInterpolator((levelsCoords, rowsCoords, colsCoords), allG)
    bInterpF = RegularGridInterpolator((levelsCoords, rowsCoords, colsCoords), allB)

    finalImObj = Image(
        "%s-MASK-%s--blurSig_%s-gaussLevels_%s" % (im.name, maskIm.name, largestBlurSigma, gaussLevelsCt),
        np.zeros(im.imArr.shape))
    finalIm = finalImObj.imArr

    xv, yv = np.meshgrid(colsCoords, rowsCoords)
    vals = 1 - mask[yv, xv]

    strengthRCCoords = np.vstack((np.ndarray.flatten(vals), np.ndarray.flatten(yv), np.ndarray.flatten(xv))).T

    finalImCoords = strengthRCCoords[:, 1:].astype(int)

    #     print("rInterpF(strengthRCCoords):", rInterpF(strengthRCCoords).shape, rInterpF(strengthRCCoords))

    finalIm[finalImCoords[:, 0], finalImCoords[:, 1], 0] = rInterpF(strengthRCCoords)
    finalIm[finalImCoords[:, 0], finalImCoords[:, 1], 1] = gInterpF(strengthRCCoords)
    finalIm[finalImCoords[:, 0], finalImCoords[:, 1], 2] = bInterpF(strengthRCCoords)

    return finalImObj

def bumpSaturation(im, bumpVal):
    hsvIm = rgb2hsv(im)
    hsvIm[:, :, 1] += bumpVal
    finalIm = hsv2rgb(hsvIm)
    return finalIm