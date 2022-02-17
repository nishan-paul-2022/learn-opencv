import library
from library import *


# https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/
def contour_detection_summarized():
    path = askopen('zmax/n16_contour.png')
    sample = cv2.imread(path)
    result = sample.copy()
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)  # Find Canny edges
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # finding Contours. Use a copy of the image e.g. edged.copy() since findContours alters the image
    color = [255, 0, 0]
    cv2.drawContours(result, contours, -1, color, 3)  # Draw all contours. -1 signifies drawing all contours

    title = f'detected_contours: {len(contours)}'
    titles = ['sample', 'edged', title]
    images = [sample, edged, result]
    plot_images('contour_detection_summarized', titles, images)


# https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/
def contour_detection_detailed():
    path = askopen('zmax/n16_contour.png')
    sample = cv2.imread(path)
    result = sample.copy()
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)  # Converting image to a binary image black and white only image).
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Detecting contours in image.
    title = f'detected_contours: {len(contours)}'
    color = [255, 0, 0]

    for item in contours:  # Going through every contours found in the image.
        approx = cv2.approxPolyDP(item, 0.009 * cv2.arcLength(item, True), True)
        cv2.drawContours(result, [approx], 0, color, 5)  # draws boundary of contours.
        approx_ = approx.ravel()  # Used to flatted the array containing the co-ordinates of the vertices.
        count = len(approx_)

        for i in range(count):
            if i % 2 == 0:
                x, y = approx_[i], approx_[i + 1]
                string = f'{x}, {y}'  # String containing the co-ordinates.
                color_ = [0, 255, 0] if i == 0 else [0, 0, 255]
                text = 'arrow tip' if i == 0 else string
                # text on topmost co-ordinate V text on remaining co-ordinates
                put_text_on_image(result, text, (x, y), 0.5, color_, 1)

    titles = ['sample', 'threshold', title]
    images = [sample, threshold, result]
    plot_images('contour_detection_detailed', titles, images)


if __name__ == '__main__':
    function_packages = [
        ['contour_detection_summarized', contour_detection_summarized],
        ['contour_detection_detailed', contour_detection_detailed],
    ]

    window_title = 'N16_CONTOUR_DETECTION'
    dynamically_create_interface(window_title, function_packages)