import library
from library import *


# https://www.geeksforgeeks.org/invisible-cloak-using-opencv-python-project/
def invisible_cloak():
    path = 'zmax/n25_invisible_cloak.mp4'
    vCap = cv2.VideoCapture(path)
    screens = [vCap]
    count = 0
    frame_background = ''

    for i in range(60):
        ret, frame_background = vCap.read()
        if not ret:
            continue

    frame_background = np.flip(frame_background, axis=1)  # flipping of the frame

    while vCap.isOpened():
        ret, frame = vCap.read()
        if not ret:
            break

        count += 1
        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([100, 40, 40])
        upper_red = np.array([100, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        lower_red = np.array([155, 40, 40])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        mask1 = mask1 + mask2
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
        mask2 = cv2.bitwise_not(mask1)
        res1 = cv2.bitwise_and(frame_background, frame_background, mask=mask1)
        res2 = cv2.bitwise_and(frame, frame, mask=mask2)
        frame_final = cv2.addWeighted(res1, 1, res2, 1, 0)
        show_frame('invisible_cloak', frame_final, screens)


if __name__ == "__main__":
    function_packages = [
        ['invisible_cloak', invisible_cloak],
    ]

    window_title = 'N25_INVISIBLE_CLOAK'
    dynamically_create_interface(window_title, function_packages)