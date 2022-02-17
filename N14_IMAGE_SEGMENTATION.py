import library
from library import *


def _image_segmentation_using_watershed_algorithm(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)  # noise removal
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)  # sure background area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2, 5)  # Finding sure foreground area
    _, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)  # Finding unknown region
    unknown = cv2.subtract(sure_bg, sure_fg)

    _, markers = cv2.connectedComponents(sure_fg)  # Marker labelling
    markers = markers+1  # Add one to all labels so that sure background is not 0, but 1
    markers[unknown == 255] = 0  # Now, mark the region of unknown with zero

    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    return img


# https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html
def image_segmentation_using_watershed_algorithm():
    path = askopen('zmax/n14_segmentation_using_watershed1.png')
    sample = cv2.imread(path)
    segmented = _image_segmentation_using_watershed_algorithm(path)
    titles = ['sample', 'segmented']
    images = [sample, segmented]
    plot_images('image_segmentation_using_watershed_algorithm', titles, images)


if __name__ == '__main__':
    function_packages = [
        ['image_segmentation_using_watershed_algorithm', image_segmentation_using_watershed_algorithm],
    ]

    window_title = 'N14_IMAGE_SEGMENTATION'
    dynamically_create_interface(window_title, function_packages)