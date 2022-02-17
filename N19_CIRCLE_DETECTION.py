import library
from library import *


def _circle_detection(circles, img):
    result = img.copy()
    title = 'detected_circles: 0'

    color1 = [255, 0, 0]
    color2 = [0, 255, 0]
    if circles is not None:  # ensure at least some circles were found
        circles = np.round(circles[0, :]).astype("int")  # convert the (x, y) coordinates and radius of the circles to integers
        title = f'detected_circles: {len(circles)}'
        for (x, y, r) in circles:  # loop over the (x, y) coordinates and radius of the circles
            cv2.circle(result, (x, y), r, color1, 4)  # draw the circle in the result image, then draw a rectangle corresponding to the center of the circle
            cv2.rectangle(result, (x - 5, y - 5), (x + 5, y + 5), color2, -1)

    return title, result


# https://pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
# https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
def circle_detection():
    paths = askopen(['zmax/n17_circle1.png', 'zmax/n17_circle2.png', 'zmax/n17_circle3.png', 'zmax/n17_circle4.png'])
    titles, imgs = list(), list()

    for path in paths:
        sample = cv2.imread(path)
        gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(gray, (3, 3))

        circles_a = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 75)
        title_a, result_a = _circle_detection(circles_a, sample)

        circles_b = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)
        title_b, result_b = _circle_detection(circles_b, sample)

        titles += ['sample', title_a, title_b]
        imgs += [sample, result_a, result_b]

    plot_images('circle_detection', titles, imgs, r=4, c=3)


if __name__ == '__main__':
    function_packages = [
        ['circle_detection', circle_detection],
    ]

    window_title = 'N17_CIRCLE_DETECTION'
    dynamically_create_interface(window_title, function_packages)