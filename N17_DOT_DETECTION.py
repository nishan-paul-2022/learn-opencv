import library
from library import *


# https://www.geeksforgeeks.org/white-and-black-dot-detection-using-opencv-python/
def dot_detection_from_binary_image():
    path = askopen('zmax/n19_dot_binary1.png')
    sample = cv2.imread(path)
    result = sample.copy()
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # threshold
    contours = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]  # find contours
    s1, s2 = 3, 20  # filter by area
    contours_list = []

    color = [255, 0, 0]
    for contour in contours:
        if s1 < cv2.contourArea(contour) < s2:
            contours_list.append(contour)
            coordinates = [(x,y) for i in contour for (x, y) in i]
            for x,y in coordinates:
                cv2.circle(result, (x, y), 1, color, 1)

    text = f'detected_dots: {len(contours_list)}'
    titles = ['sample', text]
    imgs = [sample, result]
    plot_images('dot_detection_from_binary_image', titles, imgs)


# https://stackoverflow.com/questions/44439555/count-colored-dots-in-image/44443494
def dot_detection_from_specific_colored_image():
    path = askopen('zmax/n19_dot_colored.png')
    img = cv2.imread(path)
    # apply medianBlur to smooth image before thresh holding. smooth image by 7x7 pixels, may need to adjust a bit
    blur = cv2.medianBlur(img, 7)
    # lower and upper
    red = [(0, 0, 240), (10, 10, 255)]
    green = [(0, 240, 0), (10, 255, 10)]
    yellow = [(0, 240, 250), (10, 255, 255)]
    dot_colors = [red, green, yellow]

    titles = ['sample', 'number_of_red_dot', 'number_of_green_dot', 'number_of_yellow_dot']
    imgs = [img]
    n = len(dot_colors)

    for i in range(n):
        output = img.copy()
        lower, upper = dot_colors[i]
        # apply threshhold color to white (255,255,255) and the rest to black(0,0,0)
        mask = cv2.inRange(blur, lower, upper)
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=8, minRadius=0, maxRadius=60)
        count = 0

        color = [0, 0, 0]
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype('int')
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle corresponding to the center of the circle
                cv2.circle(output, (x, y), r, color, 2)
                count = count + 1

            imgs.append(output)
            titles[i+1] = f'{titles[i+1]}: {count}'

    plot_images('dot_detection_from_specific_colored_image', titles, imgs)


if __name__ == '__main__':
    function_packages = [
        ['dot_detection_from_binary_image', dot_detection_from_binary_image],
        ['dot_detection_from_specific_colored_image', dot_detection_from_specific_colored_image],
    ]

    window_title = 'N19_DOT_DETECTION'
    dynamically_create_interface(window_title, function_packages)