import library
from library import *


def _face_detection_using_haarcascades(gray, frame):
    frontalfaces_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    smiles_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

    frontalfaces = frontalfaces_cascade.detectMultiScale(gray, 1.3, 5)
    color = [255, 0, 0]
    for (x, y, w, h) in frontalfaces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), color, 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), color, 2)

        smiles = smiles_cascade.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), color, 2)

    return frame


# https://www.geeksforgeeks.org/python-smile-detection-using-opencv/
def face_detection_using_haarcascades():
    vCap = cv2.VideoCapture(0)
    screens = [vCap]
    while vCap.isOpened():
        _, frame = vCap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = _face_detection_using_haarcascades(gray, frame)
        show_frame('face_detection_using_haarcascades', canvas, screens)


if __name__ == '__main__':
    function_packages = [
        ['face_detection_using_haarcascades', face_detection_using_haarcascades],
    ]

    window_title = 'N24_FACE_DETECTION'
    dynamically_create_interface(window_title, function_packages)