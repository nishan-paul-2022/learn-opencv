import library
from library import *


# https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
def line_detection_from_image():
	# (a) get the gray image and process GaussianBlur
	path = askopen('zmax/n21_line.png')
	img = cv2.imread(path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	kernel_size = 5
	blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

	# (b) process edge detection use Canny
	low_threshold, high_threshold = 50, 150
	edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

	# (c) use HoughLinesP to get the lines. You can adjust the parameters for better performance.
	rho = 1  # distance resolution in pixels of the Hough grid
	theta = np.pi / 180  # angular resolution in radians of the Hough grid
	threshold = 15  # minimum number of votes (intersections in Hough grid cell)
	min_line_length = 50  # minimum number of pixels making up a line
	max_line_gap = 20  # maximum gap in pixels between connectable line segments
	line_image = np.copy(img) * 0  # creating a blank to draw lines on

	# (d) Run Hough on edge detected image
	# Output "lines" is an array containing endpoints of detected line segments
	lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
	color = (255,0,0)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(line_image, (x1,y1), (x2,y2), color, 5)

	# (e) draw the lines on your srcImage.
	# Draw the lines on the  image
	lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
	titles = ['sample', 'detected_line_from_sample_image']
	imgs = [img, lines_edges]
	plot_images('line_detection_from_image', titles, imgs)


if __name__ == '__main__':
	function_packages = [
		['line_detection_from_image', line_detection_from_image],
	]

	window_title = 'N21_LINE_DETECTION'
	dynamically_create_interface(window_title, function_packages)