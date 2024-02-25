import sys
import os
import cv2
import numpy as np

# Check file extension, if not .jpg and .jpeg, return as 0 (exit)
def checkFileExtension(img):
    ext = os.path.splitext(img)[-1].lower()

    if ext != ".jpg" and ext != ".jpeg":
        return 0

    return 1

# Set default Hue for Red and Blue, then add/subtract with value from the arguments.
#   If val < 0, then blueHue + val, image masking will be blueish (cooler).
#   If val > 0, then redBlue - val, image masking will be reddish (warmer).
def setRedBlue(val):
    blueHue = 120
    redHue = 0

    if val < 0:
        blueHue = blueHue + val
    else:
        redHue = redHue - val

    diffHue = blueHue - redHue

    return diffHue

# Main function to change the Hue, and the rest parameters are still the same.
def changeHue(srcImg, hsv, val):
    h, s, v = cv2.split(hsv)

    diffHue = setRedBlue(val)

    lowerFirst = (150, 150, 150)
    upperFirst = (180, 255, 255)

    maskFirst = cv2.inRange(hsv, lowerFirst, upperFirst)

    lowerSecond = (0, 150, 150)
    upperSecond = (30, 255, 255)

    maskSecond = cv2.inRange(hsv, lowerSecond, upperSecond)

    maskCombine = cv2.add(maskFirst, maskSecond)
    maskCombine = cv2.merge([maskCombine, maskCombine, maskCombine])

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

    maskCombine = cv2.morphologyEx(maskCombine, cv2.MORPH_OPEN, kernel)
    maskCombine = cv2.morphologyEx(maskCombine, cv2.MORPH_CLOSE, kernel)

    hueNew = np.mod(h + diffHue, 180).astype(np.uint8)

    hsvNew = cv2.merge([hueNew, s, v])

    bgrImg = cv2.cvtColor(hsvNew, cv2.COLOR_HSV2BGR)

    destImg = np.where(maskCombine == (255, 255, 255), bgrImg, srcImg)

    return destImg

# Main code
len_argv = len(sys.argv)
print("Total arguments passed\t:", len_argv, "\n")

if len_argv < 4:
    print("Error: missed one or more arguments.")
    sys.exit()

print("File name\t\t:", sys.argv[0])
print("Source image file\t:", sys.argv[1])
print("Destination image file\t:", sys.argv[2])

if checkFileExtension(sys.argv[1]) == 0 or checkFileExtension(sys.argv[2]) == 0:
    print("Error: Invalid file type.")
    sys.exit()

# Customized value to change the image temperature
print("Image temperature\t:", sys.argv[3])

# Doing read the file first
srcImg = cv2.imread(sys.argv[1])

# Convert from RGB/BGR to HSV
hsv = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)

# h, s, v = cv2.split(hsv)
# print (h, s, v)

val = int(sys.argv[3])

print (cv2.__version__)

# Here we go for the main function
destImg = changeHue(srcImg, hsv, val)

# Write the result to the file
cv2.imwrite(sys.argv[2], destImg)
