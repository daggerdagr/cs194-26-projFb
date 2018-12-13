from miniature import *

def farmhouse(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    imFarm = Image.fromPath("./sample_imgs/online/farmhouse.jpg", 0.25)
    if bumpSatBool:
        imFarm.imArr = bumpSaturation(imFarm.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        maskPts = np.array([(15.758064516128997, 461.53870967741943), (1135.2419354838707, 477.79677419354846)])

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([(676.9230839582953, 383.1956283153466), (939.1509968904335, 346.9051582220595),
                               (943.8336381927933, 349.2464788732394), (984.8067495884399, 315.2973294311322),
                               (1021.0972196817269, 350.4171391988293), (1012.9025974025975, 355.0997805011889),
                               (1010.5612767514177, 509.6269434790561), (1014.0732577281873, 510.79760380464603),
                               (1014.0732577281873, 517.8215657581854), (987.1480702396196, 524.8455277117248),
                               (987.1480702396196, 531.8694896652643), (985.9774099140296, 537.7227912932137),
                               (747.1627034936895, 575.1839217120908), (640.6326138650082, 531.8694896652643),
                               (640.6326138650082, 469.8244924089994), (635.9499725626487, 466.3125114322297),
                               (657.021858423267, 403.09685385037494)])

    maskFarm = generateMask(imFarm, maskStrength=100, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=imFarm, maskIm=maskFarm, largestBlurSigma=250, gaussLevelsCt=50)
    # res.imArr = bumpSaturation(res.imArr, 0.05)
    printImage("%s.png" % res.name, res.imArr)



def shuttle(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    im = Image.fromPath("./sample_imgs/online/shuttle.jpg", 0.25)

    if bumpSatBool:
        im.imArr = bumpSaturation(im.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        maskPts = np.array([(1048.5551948051948, 409.88149350649337), (1048.5551948051948, 504.72727272727263),
                            (12.1915584415583, 393.6883116883116), (12.1915584415583, 319.66233766233756),
                            (1046.2418831168832, 358.98863636363626)])

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([])

    maskFarm = generateMask(im, maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=im, maskIm=maskFarm, largestBlurSigma=250, gaussLevelsCt=50)

    printImage("%s.png" % res.name, res.imArr)


def rocketship(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    im = Image.fromPath("./sample_imgs/online/rocketship.jpg", 0.25)
    if bumpSatBool:
        im.imArr = bumpSaturation(im.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        maskPts = np.array([(11.029220779220736, 641.5454545454545), (631.9707792207791, 633.4285714285713),
                            (629.9415584415585, 710.538961038961), (6.97077922077915, 722.7142857142857)])

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([(372.4020029266509, 558.2616608743369), (371.25877995244196, 550.2591000548746),
                               (366.68588805560637, 533.1107554417413), (371.25877995244196, 497.67084324126574),
                               (365.54266508139744, 481.66572160234125), (373.5452259008597, 467.9470459118346),
                               (371.25877995244196, 449.6554783244924), (363.2562191329797, 416.5020120724346),
                               (362.1129961587708, 258.73724163160773), (352.9672123650997, 234.7295591732211),
                               (352.9672123650997, 225.58377537954993), (350.6807664166819, 221.01088348271446),
                               (348.39432046826414, 184.4277483080299), (351.8239893908908, 180.99807938540323),
                               (349.53754344247307, 176.42518748856776), (348.39432046826414, 152.41750503018102),
                               (346.1078745198464, 150.13105908176328), (342.67820559721974, 152.41750503018102),
                               (340.3917596488019, 223.2973294311322), (340.3917596488019, 234.7295591732211),
                               (330.1027528809219, 258.73724163160773), (333.5324218035486, 523.9649716480702),
                               (326.67308395829525, 555.9752149259191), (320.95696908725074, 557.118437900128),
                               (322.10019206145967, 568.5506676422169), (330.1027528809219, 571.9803365648436),
                               (330.1027528809219, 575.4100054874702), (338.10531370038416, 571.9803365648436),
                               (342.67820559721974, 567.407444668008), (360.969773184562, 567.407444668008),
                               (370.11555697823303, 571.9803365648436), (376.97489482348635, 571.9803365648436),
                               (376.97489482348635, 560.5481068227547)])

    maskFarm = generateMask(im, maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=im, maskIm=maskFarm, largestBlurSigma=250, gaussLevelsCt=50)
    # res.imArr = bumpSaturation(res.imArr, 0.05)
    printImage("%s.png" % res.name, res.imArr)


def uppersproul(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    im = Image.fromPath("./sample_imgs/custom/uppersproul.jpg", 0.50)
    if bumpSatBool:
        im.imArr = bumpSaturation(im.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        #         maskPts = np.array([(21.854838709677438, 235.55806451612904), (991.241935483871, 247.7516129032258)]) * 2
        maskPts = np.array([(64.53225806451616, 264.00967741935483), (249.4677419354839, 343.26774193548385),
                            (725.016129032258, 341.23548387096776), (960.758064516129, 320.9129032258064),
                            (985.1451612903227, 229.46129032258068), (907.9193548387098, 20.138709677419456),
                            (141.75806451612902, 26.235483870967755), (68.59677419354841, 131.91290322580653)]) * 2

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([])

    maskFarm = generateMask(im, maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=im, maskIm=maskFarm, largestBlurSigma=75, gaussLevelsCt=50)
    # res.imArr = bumpSaturation(res.imArr, 0.05)
    printImage("%s.jpg" % res.name, res.imArr)


def intersection(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    im = Image.fromPath("./sample_imgs/custom/intersection.jpg", 0.50)
    if bumpSatBool:
        im.imArr = bumpSaturation(im.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        maskPts = np.array([(56.403225806451616, 261.97741935483873), (985.1451612903227, 304.6548387096774)]) * 2

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([])

    maskFarm = generateMask(im, maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=im, maskIm=maskFarm, largestBlurSigma=75, gaussLevelsCt=50)
    # res.imArr = bumpSaturation(res.imArr, 0.05)
    printImage("%s.jpg" % res.name, res.imArr)


def lowersproul(bumpSatBool=True, usePresetBlurMaskBool=True, usePresetObjMaskBool=True, printMask = True):
    im = Image.fromPath("./sample_imgs/custom/lowersproul.jpg", 0.50)
    if bumpSatBool:
        im.imArr = bumpSaturation(im.imArr, 0.05)

    maskPts = None
    if usePresetBlurMaskBool:
        maskPts = np.array([(56.403225806451616, 261.97741935483873), (985.1451612903227, 304.6548387096774)]) * 2

    objMaskPts = None
    if usePresetObjMaskBool:
        objMaskPts = np.array([])

    maskFarm = generateMask(im, maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                            debugB=printMask)
    res = maskedBlur(im=im, maskIm=maskFarm, largestBlurSigma=150, gaussLevelsCt=50)
    # res.imArr = bumpSaturation(res.imArr, 0.05)
    printImage("%s.jpg" % res.name, res.imArr)


def uppersproulGif(printMask = True):
    totalDirPath = "./sample_imgs/custom/burst"
    fileList = getImgNames(totalDirPath)
    completeFileList = ["%s/%s" % (totalDirPath, imName) for imName in fileList]
    imList = [Image.fromPath(filename, 0.25) for filename in completeFileList]

    maskPts = np.array([(64.53225806451616, 264.00967741935483), (249.4677419354839, 343.26774193548385),
                        (725.016129032258, 341.23548387096776), (960.758064516129, 320.9129032258064),
                        (985.1451612903227, 229.46129032258068), (907.9193548387098, 20.138709677419456),
                        (141.75806451612902, 26.235483870967755), (68.59677419354841, 131.91290322580653)])
    objMaskPts = np.array([])

    mask = generateMask(imList[0], maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                        debugB=printMask)

    results = []
    for im in imList:
        res = maskedBlur(im=im, maskIm=mask, largestBlurSigma=75, gaussLevelsCt=50)
        results.append(res)

    convertToGif("uppersproul", results, resizeFactor=None)


def lowersproulGif(printMask = True):
    totalDirPath = "./sample_imgs/custom/burst2"
    fileList = getImgNames(totalDirPath)
    completeFileList = ["%s/%s" % (totalDirPath, imName) for imName in fileList]
    imList = [Image.fromPath(filename, 0.25) for filename in completeFileList]

    maskPts = np.array([(56.403225806451616, 261.97741935483873), (985.1451612903227, 304.6548387096774)])
    objMaskPts = np.array([])

    mask = generateMask(imList[0], maskStrength=50, maskPoints=maskPts, objMask=True, objMaskPoints=objMaskPts,
                        debugB=printMask)

    results = []
    for im in imList:
        res = maskedBlur(im=im, maskIm=mask, largestBlurSigma=75, gaussLevelsCt=50)
        results.append(res)

    convertToGif("lowersproul", results, resizeFactor=None)