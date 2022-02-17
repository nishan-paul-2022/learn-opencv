import library
from library import *


def findColor(img, myColors, myColorValues, imgResult):  # function to pick color of object
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converting the image to HSV format
    count = 0
    newPoints = []

    for color in myColors:  # running for loop to work with all colors
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)  # making the circles
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


def getContours(img):  # contours function used to improve accuracy of paint
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:  # working with contours
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawing_points(myPoints, myColorValues, imgResult):  # draws your action on virtual canvas
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


# https://www.geeksforgeeks.org/live-webcam-drawing-using-opencv/
def draw_on_webcam():
    # set Width and Height of output Screen
    frameWidth, frameHeight = 640, 480

    vCap = cv2.VideoCapture(0)
    vCap.set(3, frameWidth)
    vCap.set(4, frameHeight)
    vCap.set(10, 150)  # set brightness, id is 10 and value can be changed accordingly

    myColors = [[5, 107, 0, 19, 255, 255], [133, 56, 0, 159, 156, 255], [57, 76, 0, 100, 255, 255], [90, 48, 0, 118, 255, 255]]  # object color values
    myColorValues = [[51, 153, 255], [255, 0, 255], [0, 255, 0], [255, 0, 0]]  # color values which will be used to paint values needs to be in BGR
    myPoints = []  # [x , y , colorId ]

    screens = [vCap]
    while vCap.isOpened():
        success, img = vCap.read()
        imgResult = img.copy()
        newPoints = findColor(img, myColors, myColorValues, imgResult)  # finding the colors for the points

        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)

        if len(myPoints) != 0:
            drawing_points(myPoints, myColorValues, imgResult)

        # displaying output on Screen
        show_frame('draw_on_webcam', imgResult, screens)


if __name__ == '__main__':
    function_packages = [
        ['draw_on_webcam', draw_on_webcam],
    ]

    window_title = 'N23_DRAW_ON_WEBCAM'
    dynamically_create_interface(window_title, function_packages)