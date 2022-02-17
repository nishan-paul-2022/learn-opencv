import library
from library import *


# https://www.geeksforgeeks.org/python-corner-detection-with-harris-corner-detection-method-using-opencv/
def corner_detection_using_harris_builtin():
    path = askopen('zmax/n18_corner1.png')
    color = [255, 0, 0]
    sample = cv2.imread(path)
    result = sample.copy()
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 5, 0.07)  # apply the cv2.cornerHarris method to detect the corners with appropriate values as input parameters
    dilate = cv2.dilate(dst, None)  # Results are marked through the dilated corners
    result[dilate > 0.01 * dilate.max()] = color  # Reverting back to the sample_image, with optimal threshold value

    title = f'detected_corners: {len(dilate)}'
    titles = ['sample', title]
    imgs = [sample, result]
    plot_images('corner_detection_using_harris_builtin', titles, imgs)


# https://www.geeksforgeeks.org/python-corner-detection-with-shi-tomasi-corner-detection-method-using-opencv/
def corner_detection_using_harris_raw():
    path = askopen('zmax/n18_corner1.png')
    color = [255, 0, 0]
    sample = cv2.imread(path)
    result = cv2.cvtColor(sample, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

    k = 0.04
    window_size = 5
    threshold = 10000.00

    offset = int(window_size / 2)
    y_range = gray.shape[0] - offset
    x_range = gray.shape[1] - offset

    dy, dx = np.gradient(gray)
    Ixx = dx ** 2
    Ixy = dy * dx
    Iyy = dy ** 2

    corner_file = open('zmax/n18_corner_list.txt', 'w')
    corner_file.write('x,\t y,\t r\n')
    count = 0

    for y in range(offset, y_range):
        for x in range(offset, x_range):
            # Values of sliding window
            start_y = y - offset
            end_y = y + offset + 1
            start_x = x - offset
            end_x = x + offset + 1

            # The variable names are representative to the variable of the Harris corner equation
            windowIxx = Ixx[start_y: end_y, start_x: end_x]
            windowIxy = Ixy[start_y: end_y, start_x: end_x]
            windowIyy = Iyy[start_y: end_y, start_x: end_x]

            # Sum of squares of intensities of partial derivatives
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            # Calculate determinant and trace of the matrix
            det = (Sxx * Syy) - (Sxy ** 2)
            trace = Sxx + Syy

            # Calculate r for Harris Corner equation
            r = det - k * (trace ** 2)
            if r > threshold:
                result[y, x] = color
                text = f'{x}, {y}, {r}\n'
                corner_file.write(text)
                count += 1

    corner_file.close()

    titles = ['sample', f'detected_corners: {count}']
    imgs = [sample, result]
    plot_images('corner_detection_using_harris_raw', titles, imgs)


# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html
def corner_detection_using_shi_tomasi():
    path = askopen('zmax/n18_corner1.png')
    sample = cv2.imread(path)
    result = sample.copy()
    gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    # shi-tomasi corner detection function. We are detecting only 10 best corners here.
    # You can change the number to get desired result.
    corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
    # convert corners values to integer. So that we will be able to draw circles on them
    corners = np.int0(corners)
    title = f'detected_corners: {len(corners)}'

    color = [255, 0, 0]
    for i in corners:
        x, y = i.ravel()
        cv2.circle(result, (x, y), 2, color, 2)

    titles = ['sample', title]
    imgs = [sample, result]
    plot_images('corner_detection_using_shi_tomasi', titles, imgs)


if __name__ == '__main__':
    function_packages = [
        ['corner_detection_using_harris_builtin', corner_detection_using_harris_builtin],
        ['corner_detection_using_harris_raw', corner_detection_using_harris_raw],
        ['corner_detection_using_shi_tomasi', corner_detection_using_shi_tomasi],
    ]

    window_title = 'N18_CORNER_DETECTION'
    dynamically_create_interface(window_title, function_packages)