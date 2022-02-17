import library
from library import *


# https://www.geeksforgeeks.org/filter-color-with-opencv/
def color_segmentation_to_identify_specific_color():
    blue = np.uint8([[[255, 0, 0]]])  # here insert the bgr values which you want to convert to hsv
    hsvBlue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)  # Threshold of blue in HSV space
    lowerLimit = np.array([hsvBlue[0][0][0] - 10, 100, 100])
    upperLimit = np.array([hsvBlue[0][0][0] + 10, 255, 255])

    vCap = cv2.VideoCapture(0)
    screens = [vCap]
    while vCap.isOpened():
        _, frame = vCap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # It converts the BGR color space of image to HSV color space
        mask = cv2.inRange(hsv, lowerLimit, upperLimit)  # preparing the mask to overlay
        # mask = cv2.bitwise_not(mask)
        result = cv2.bitwise_and(frame, frame, mask=mask)  # The black region in the mask has the value of 0, so when multiplied with sample_image removes all non-blue regions
        imgs = [frame, mask, result]
        combined = library.image_merge(imgs)
        combined = library.image_resize_specified(combined, 1, 0.75)
        show_frame('color_segmentation_to_identify_specific_color', combined, screens)


if __name__ == "__main__":
    function_packages = [
        ['color_segmentation_to_identify_specific_color', color_segmentation_to_identify_specific_color],
    ]

    window_title = 'N27_COLOR_SEGMENTATION'
    dynamically_create_interface(window_title, function_packages)