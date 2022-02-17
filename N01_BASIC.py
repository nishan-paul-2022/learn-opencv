import library
from library import *


# IMREAD_ANYCOLOR : the image is read in any possible color format
# IMREAD_COLOR : always convert image to the 3 channel BGR color image
# IMREAD_GRAYSCALE : the image is read in gray color format
# https://www.geeksforgeeks.org/reading-image-opencv-using-python/
def image_read():
    path = askopen('zmax/n01_read.png')
    modes = [cv2.IMREAD_ANYCOLOR, cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE]
    titles = ['IMREAD_ANYCOLOR', 'IMREAD_COLOR', 'IMREAD_GRAYSCALE']
    imgs = list()
    for mode in modes:
        img = cv2.imread(path, mode)
        imgs.append(img)
    plot_images('image_read', titles, imgs)


# https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/
def image_write():
    path1 = askopen('zmax/n01_read.png')
    path2 = 'zmax/n01_write.png'
    img1 = cv2.imread(path1)
    cv2.imwrite(path2, img1)
    img2 = cv2.imread(path2)
    show_frame('image_write', img2)


# https://www.geeksforgeeks.org/how-to-find-width-and-height-of-an-image-using-python/
def get_image_height_and_width():
    path = askopen('zmax/n01_h&w.png')
    img = cv2.imread(path)
    h, w = img.shape[:2]  # get the height and width of the image
    text = f'height = {h}, width = {w}'
    img = library.put_text_on_image(img, text)
    show_frame('get_image_height_and_width', img)


# https://www.geeksforgeeks.org/introduction-to-opencv/
def extract_bgr_value_of_pixel():
    path = askopen('zmax/n01_extract_bgr.png')
    img = cv2.imread(path)

    # Extracting RGB values. Here we have randomly chosen a pixel by passing in 100, 100 for height and width.
    (B, G, R) = img[100, 100]
    text1 = f'R = {R}, G = {G}, B = {B}'

    # We can also pass the channel to extract the value for a specific channel
    B = img[100, 100, 0]
    text2 = f'B = {B}'

    text = f'{text1} . {text2}'
    img = library.put_text_on_image(img, text)
    show_frame('extract_bgr_value_of_pixel', img)


# https://www.geeksforgeeks.org/python-opencv-bgr-color-palette-with-trackbars/
def bgr_color_palette():
    window_name = 'bgr_color_palette'
    image = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow(window_name)
    mT = lambda _: print()  # empty function called when any trackbar moves

    # there trackbars which have the name of trackbars min and max value
    cv2.createTrackbar('Blue', window_name, 0, 255, mT)
    cv2.createTrackbar('Green', window_name, 0, 255, mT)
    cv2.createTrackbar('Red', window_name, 0, 255, mT)

    # Used to open the window till press the ESC key
    while show_frame(window_name, image, screens=[]):
        try:
            # values of blue, green, red
            blue = cv2.getTrackbarPos('Blue', window_name)
            green = cv2.getTrackbarPos('Green', window_name)
            red = cv2.getTrackbarPos('Red', window_name)
            image[:] = [blue, green, red]  # merge all three color chanels and make the image composites image from rgb
        except:
            break


# https://www.geeksforgeeks.org/color-spaces-in-opencv-python/
def color_spaces_of_image():
    path = askopen('zmax/n01_color_spaces.png')
    sample = cv2.imread(path)
    B, G, R = cv2.split(sample)  # Corresponding channels are seperated
    titles = ['sample', 'blue', 'green', 'red']
    imgs = [sample, B, G, R]
    # for img in imgs:
    #     show_frame('', img)
    plot_images('color_spaces_of_image', titles, imgs)


# https://www.geeksforgeeks.org/python-visualizing-image-in-different-color-spaces/
def color_conversion_of_image():
    path = askopen('zmax/n01_color_conversion.png')
    sample = cv2.imread(path)
    titles = ['BGR', 'GRAY', 'YCrCb', 'HSV', 'LAB', 'CV_8U']
    GRAY = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    YCrCb = cv2.cvtColor(sample, cv2.COLOR_BGR2YCrCb)
    HSV = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    LAB = cv2.cvtColor(sample, cv2.COLOR_BGR2LAB)
    CV_8U = cv2.Laplacian(sample, cv2.CV_8U)
    imgs = [sample, GRAY, YCrCb, HSV, LAB, CV_8U]
    plot_images('color_conversion_of_image', titles, imgs)


# https://www.geeksforgeeks.org/introduction-to-opencv/
def extract_user_defined_region_of_image():
    path = askopen('zmax/n01_extract_user_defined_region.png')
    sample = cv2.imread(path)
    extracted = sample[100: 500, 200: 700]  # We will calculate the region of interest by slicing the pixels of the image
    titles = ['sample', 'extracted']
    imgs = [sample, extracted]
    plot_images('extract_user_defined_region_of_image', titles, imgs)


if __name__ == "__main__":
    function_packages = [
        ['image_read', image_read],
        ['image_write', image_write],
        ['get_image_height_and_width', get_image_height_and_width],
        ['extract_bgr_value_of_pixel', extract_bgr_value_of_pixel],
        ['bgr_color_palette', bgr_color_palette],
        ['color_spaces_of_image', color_spaces_of_image],
        ['color_conversion_of_image', color_conversion_of_image],
        ['extract_user_defined_region_of_image', extract_user_defined_region_of_image],
    ]

    window_title = 'N01_BASIC'
    dynamically_create_interface(window_title, function_packages)