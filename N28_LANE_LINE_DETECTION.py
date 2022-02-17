import library
from library import *


def RGB_color_selection(image):
    lower_threshold = np.uint8([200, 200, 200])  # White color mask
    upper_threshold = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(image, lower_threshold, upper_threshold)

    lower_threshold = np.uint8([175, 175, 0])  # Yellow color mask
    upper_threshold = np.uint8([255, 255, 255])
    yellow_mask = cv2.inRange(image, lower_threshold, upper_threshold)

    mask = cv2.bitwise_or(white_mask, yellow_mask)  # Combine white and yellow masks
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image


def convert_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


def HSV_color_selection(image):
    converted_image = convert_hsv(image)  # Convert the input image to HSV

    lower_threshold = np.uint8([0, 0, 210])  # White color mask
    upper_threshold = np.uint8([255, 30, 255])
    white_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    lower_threshold = np.uint8([18, 80, 80])  # Yellow color mask
    upper_threshold = np.uint8([30, 255, 255])
    yellow_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    mask = cv2.bitwise_or(white_mask, yellow_mask)  # Combine white and yellow masks
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image


def convert_hsl(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2HLS)


def HSL_color_selection(image):
    converted_image = convert_hsl(image)  # Convert the input image to HSL

    lower_threshold = np.uint8([0, 200, 0])  # White color mask
    upper_threshold = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    lower_threshold = np.uint8([10, 0, 100])  # Yellow color mask
    upper_threshold = np.uint8([40, 255, 255])
    yellow_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    mask = cv2.bitwise_or(white_mask, yellow_mask)  # Combine white and yellow masks
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image


def gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def gaussian_smoothing(image, kernel_size=13):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def canny_detector(image, low_threshold=50, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)


def region_selection(image):
    mask = np.zeros_like(image)

    if len(image.shape) > 2:  # Defining a 3 channel or 1 channel color to fill the mask with depending on the input image
        channel_count = image.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    rows, cols = image.shape[:2]      # We could have used fixed numbers as the vertices of the polygon, but they will not be applicable to zmax with different dimesnions.
    bottom_left = [cols * 0.1, rows * 0.95]
    top_left = [cols * 0.4, rows * 0.6]
    bottom_right = [cols * 0.9, rows * 0.95]
    top_right = [cols * 0.6, rows * 0.6]
    vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def hough_transform(image):
    rho = 1  # Distance resolution of the accumulator in pixels.
    theta = np.pi / 180  # Angle resolution of the accumulator in radians.
    threshold = 20  # Only lines that are greater than threshold will be returned.
    minLineLength = 20  # Line segments shorter than that are rejected.
    maxLineGap = 300  # Maximum allowed gap between points on the same line to link them
    return cv2.HoughLinesP(image, rho=rho, theta=theta, threshold=threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)


def draw_lines(image, lines, color=None, thickness=2):
    if color is None:
        color = [255, 0, 0]
    image = np.copy(image)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
    return image


def average_slope_intercept(lines):
    left_lines = []  # (slope, intercept)
    left_weights = []  # (length,)
    right_lines = []  # (slope, intercept)
    right_weights = []  # (length,)

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            length = np.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
            if slope < 0:
                left_lines.append((slope, intercept))
                left_weights.append(length)
            else:
                right_lines.append((slope, intercept))
                right_weights.append(length)

    left_lane = np.dot(left_weights, left_lines) / np.sum(left_weights) if len(left_weights) > 0 else None
    right_lane = np.dot(right_weights, right_lines) / np.sum(right_weights) if len(right_weights) > 0 else None
    return left_lane, right_lane


def pixel_points(y1, y2, line):
    if line is None:
        return None
    slope, intercept = line
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    y1 = int(y1)
    y2 = int(y2)
    return (x1, y1), (x2, y2)


def lane_lines(image, lines):
    left_lane, right_lane = average_slope_intercept(lines)
    y1 = image.shape[0]
    y2 = y1 * 0.6
    left_line = pixel_points(y1, y2, left_lane)
    right_line = pixel_points(y1, y2, right_lane)
    return left_line, right_line


def draw_lane_lines(image, lines, color=None, thickness=12):
    if color is None:
        color = [255, 0, 0]
    line_image = np.zeros_like(image)
    for line in lines:
        if line is not None:
            cv2.line(line_image, *line, color, thickness)
    return cv2.addWeighted(image, 1.0, line_image, 1.0, 0.0)


def frame_processor(image):
    color_select = HSL_color_selection(image)
    gray = gray_scale(color_select)
    smooth = gaussian_smoothing(gray)
    edges = canny_detector(smooth)
    region = region_selection(edges)
    hough = hough_transform(region)
    result = draw_lane_lines(image, lane_lines(image, hough))
    return result


def process_video(test_video, output_video):
    lvideo = VideoFileClip(test_video, audio=False)
    processed = lvideo.fl_image(frame_processor)
    processed.write_videofile(output_video, audio=False)


# https://www.tutorialspoint.com/line-detection-in-python-with-opencv
# https://mohamedameen93.github.io/Lane-lines-detection-using-Python-and-OpenCV/
def lane_line_detection_from_video():
    imagesFile = ['l1_solidWhiteCurve', 'l2_solidWhiteRight', 'l3_solidYellowCurve', 'l4_solidYellowCurve2', 'l5_solidYellowLeft', 'l6_whiteCarLaneSwitch', 'l7_VideoSnapshot2', 'l8_VideoSnapshot3']
    videosFile = ['l_challenge', 'l_solidWhiteRight', 'l_solidYellowLeft']

    test_images = [cv2.imread(f'zmax/{path}.jpg') for path in imagesFile]
    RGB_color_images = list(map(RGB_color_selection, test_images))
    convert_hsv_images = list(map(convert_hsv, test_images))
    HSV_color_images = list(map(HSV_color_selection, test_images))
    convert_hsl_images = list(map(convert_hsl, test_images))
    HSL_color_images = list(map(HSL_color_selection, test_images))

    gray_images = list(map(gray_scale, HSL_color_images))
    blur_images = list(map(gaussian_smoothing, gray_images))
    edge_detected_images = list(map(canny_detector, blur_images))
    masked_image = list(map(region_selection, edge_detected_images))
    hough_lines = list(map(hough_transform, masked_image))
    line_images = [draw_lines(image, lines) for image, lines in zip(test_images, hough_lines)]
    lane_lane_images = [draw_lane_lines(image, lane_lines(image, lines)) for image, lines in zip(test_images, hough_lines)]

    plot_images('test_images', imagesFile, test_images)
    plot_images('RGB_color_images', imagesFile, RGB_color_images)
    plot_images('convert_hsv_images', imagesFile, convert_hsv_images)
    plot_images('HSV_color_images', imagesFile, HSV_color_images)
    plot_images('convert_hsl_images', imagesFile, convert_hsl_images)
    plot_images('HSL_color_images', imagesFile, HSL_color_images)

    plot_images('gray_images', imagesFile, gray_images)
    plot_images('blur_images', imagesFile, blur_images)
    plot_images('edge_detected_images', imagesFile, edge_detected_images)
    plot_images('masked_image', imagesFile, masked_image)
    plot_images('line_images', imagesFile, line_images)
    plot_images('lane_lane_images', imagesFile, lane_lane_images)

    for i in videosFile:
        path1 = f'zmax/{i}_input.mp4'
        path2 = f'zmax/{i}_output.mp4'
        process_video(path1, path2)
        show_video(i, path2)


if __name__ == '__main__':
    function_packages = [
        ['lane_line_detection_from_video', lane_line_detection_from_video],
    ]

    window_title = 'N28_LANE_LINE_DETECTION'
    dynamically_create_interface(window_title, function_packages)