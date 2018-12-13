from scenarios import *

def main():
    farmhouse(bumpSatBool = True,
              usePresetBlurMaskBool = True,
              usePresetObjMaskBool = True,
              printMask = True)

    shuttle(bumpSatBool = True,
            usePresetBlurMaskBool = True,
            usePresetObjMaskBool = True,
            printMask = True)

    rocketship(bumpSatBool = True,
               usePresetBlurMaskBool = True,
               usePresetObjMaskBool = True,
               printMask = True)

    uppersproul(bumpSatBool = True,
                usePresetBlurMaskBool = True,
                usePresetObjMaskBool = True,
                printMask = True)

    intersection(bumpSatBool = True,
                 usePresetBlurMaskBool = True,
                 usePresetObjMaskBool = True,
                 printMask = True)

    lowersproul(bumpSatBool = True,
                usePresetBlurMaskBool = True,
                usePresetObjMaskBool = True,
                printMask = True)


    uppersproulGif(printMask = True)

    lowersproulGif(printMask = True)

    return


main()