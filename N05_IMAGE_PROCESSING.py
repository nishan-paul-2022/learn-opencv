import library
from library import *


# https://www.geeksforgeeks.org/python-image-blurring-using-opencv/
def image_blurring():
    path = askopen('zmax/n05_blurring.png')
    sample = cv2.imread(path)
    gaussian = cv2.GaussianBlur(sample, (7, 7), 0)  # Gaussian Blur
    median = cv2.medianBlur(sample, 5)  # Median Blur
    bilateral = cv2.bilateralFilter(sample, 9, 75, 75)  # Bilateral Blur
    titles = ['sample', 'gaussian_blurring', 'median_blurring', 'bilateral_blurring']
    imgs = [sample, gaussian, median, bilateral]
    plot_images('image_blurring', titles, imgs)


# https://www.geeksforgeeks.org/python-denoising-of-colored-images-using-opencv/
def image_denoising():
    path = askopen('zmax/n05_denoising.png')
    sample = cv2.imread(path)
    denoised = cv2.fastNlMeansDenoisingColored(sample, None, 10, 10, 7, 15)  # denoising of image saving it into dst image
    titles = ['sample', 'denoised']
    images = [sample, denoised]
    plot_images('image_denoising', titles, images)


# https://www.geeksforgeeks.org/image-inpainting-using-opencv/
def image_inpainting():
    path1 = askopen('zmax/n05_inpainting_a.png')
    path2 = askopen('zmax/n05_inpainting_b.png')
    sample = cv2.imread(path1)
    damaged = cv2.imread(path2, 0)
    filtered = cv2.inpaint(sample, damaged, 3, cv2.INPAINT_NS)
    titles = ['sample', 'damaged', 'filtered']
    imgs = [sample, damaged, filtered]
    plot_images('image_inpainting', titles, imgs)


# https://www.geeksforgeeks.org/python-bilateral-filtering/
def image_bilateral_filtering():
    path = askopen('zmax/n05_bilateral.png')
    sample = cv2.imread(path)
    bilateralFilter = cv2.bilateralFilter(sample, 15, 75, 75)  # apply bilateral filter with d = 15, sigmaColor = sigmaSpace = 75
    blur = cv2.blur(sample, (5, 5))
    medianBlur = cv2.medianBlur(sample, 5)
    GaussianBlur = cv2.GaussianBlur(sample, (5, 5), 0)
    titles = ['sample', 'bilateralFilter', 'blur', 'medianBlur', 'GaussianBlur']
    imgs = [sample, bilateralFilter, blur, medianBlur, GaussianBlur]
    plot_images('image_bilateral_filtering', titles, imgs)


# https://www.geeksforgeeks.org/cartooning-an-image-using-opencv-python/
# https://datahacker.rs/002-opencv-projects-how-to-cartoonize-an-image-with-opencv-in-python/
def image_cartooning():
    paths = askopen(['zmax/n05_cartooning1.png', 'zmax/n05_cartooning2.png'])
    imgs, titles = list(), list()

    for i in paths:
        img = cv2.imread(i)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        titles += ['image', 'edge', 'cartoon']
        imgs += [img, edges, cartoon]

    plot_images('image_cartooning', titles, imgs)


# https://www.geeksforgeeks.org/image-registration-using-opencv-python/
def image_registration():
    # image to be aligned & reference image
    path1, path2 = askopen('zmax/n05_registration_a3.png'), askopen('zmax/n05_registration_b3.png')
    sample, reference = cv2.imread(path1), cv2.imread(path2)
    sample_ = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    reference_ = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    height, width = reference_.shape

    orb_detector = cv2.ORB_create(5000)  # Create ORB detector with 5000 features.
    kp1, d1 = orb_detector.detectAndCompute(sample_, None)  # Find keypoints and descriptors. The first arg is the image, second arg is the mask (which is not reqiured in this case).
    kp2, d2 = orb_detector.detectAndCompute(reference_, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Match features between the two zmax. We create a Brute Force matcher with Hamming distance as measurement mode.
    matches = matcher.match(d1, d2)  # Match the two sets of descriptors.
    matches.sort(key=lambda x: x.distance)  # Sort matches on the basis of their Hamming distance.
    matches = matches[: len(matches)*90]  # Take the top 90 % matches forward.
    no_of_matches = len(matches)
    p1 = np.zeros((no_of_matches, 2))  # Define empty matrices of shape no_of_matches * 2.
    p2 = np.zeros((no_of_matches, 2))

    for i in range(no_of_matches):
        p1[i, :] = kp1[matches[i].queryIdx].pt
        p2[i, :] = kp2[matches[i].trainIdx].pt

    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)  # Find the homography matrix.
    transformed_img = cv2.warpPerspective(sample, homography, (width, height))  # Use this matrix to transform the colored image wrt the reference image.

    imgs = [sample, reference, transformed_img]
    titles = ['image to be aligned', 'reference image', 'registered image']
    plot_images('image_registration', titles, imgs)


if __name__ == "__main__":
    function_packages = [
        ['image_blurring', image_blurring],
        ['image_denoising', image_denoising],
        ['image_inpainting', image_inpainting],
        ['image_bilateral_filtering', image_bilateral_filtering],
        ['image_cartooning', image_cartooning],
        ['image_registration', image_registration],
    ]

    window_title = 'N05_IMAGE_PROCESSING'
    dynamically_create_interface(window_title, function_packages)