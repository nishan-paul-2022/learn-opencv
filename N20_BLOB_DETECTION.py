import cv2

import library
from library import *


def generate_detector():
    params = cv2.SimpleBlobDetector_Params()  # to differentiate the circular blobs from non-circular blobs, we need to set some parameters. these parameters can be set by using the functions of SimpleBlobDetector_Params() class.
    params.filterByArea, params.minArea = True, 100  # set area filtering parameters in this, we can define both min as well as max area for the blob
    params.filterByCircularity, params.minCircularity = True, 0.9  # set circularity filtering parameters. the minCircularity value=1 defines a perfect circle & 0 defines it's opposite
    params.filterByConvexity, params.minConvexity = False, 0.2  # set convexity filtering parameters
    params.filterByInertia, params.minInertiaRatio = True, 0.01  # setting inertia filtering parameters
    detector = cv2.SimpleBlobDetector_create(params)  # creating a detector with the specified parameters
    return detector


def detect_keypoints(detector, title, img):
    color = [255, 0, 0]
    keypoints = detector.detect(img)  # detect blobs
    blank = np.zeros((1, 1))  # draw blobs on our image as red circles
    blobs = cv2.drawKeypoints(img, keypoints, blank, color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    number_of_blobs = len(keypoints)  # displaying number of blobs detected
    title = f"detected_{title}: {number_of_blobs}"
    return title, blobs


# https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/
# https://learnopencv.com/blob-detection-using-opencv-python-c/
# https://github.com/ss0028/Blob-Detection
def blob_detection():
    path = askopen('zmax/n20_blob1.png')
    sample = cv2.imread(path)
    gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    functions = {'blobs': cv2.SimpleBlobDetector_create, 'circular_blobs': generate_detector}
    titles = ['sample']
    imgs = [sample]

    for title, function in functions.items():
        detector = function()
        title, blobs = detect_keypoints(detector, title, gray)
        titles.append(title)
        imgs.append(blobs)

    plot_images('blob_detection', titles, imgs)


if __name__ == '__main__':
    function_packages = [
        ['blob_detection', blob_detection],
    ]

    window_title = 'N20_BLOB_DETECTION'
    dynamically_create_interface(window_title, function_packages)