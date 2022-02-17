import library
import library
from library import *


# https://stackoverflow.com/questions/50025280/creating-an-rgb-picture-in-python-with-opencv-from-a-randomized-array/50025647
def image_generating():
	data = np.random.randint(0, 255, size=(900, 800, 3), dtype=np.uint8)
	show_frame('image_generating', data)


# https://www.geeksforgeeks.org/python-opencv-cv2-copymakeborder-method/
def image_bordering():
	path = askopen('zmax/n03_bordering.png')
	img1 = cv2.imread(path)
	img2 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
	img3 = cv2.copyMakeBorder(img1, 100, 100, 50, 50, cv2.BORDER_REFLECT)
	titles = ['img1', 'img2', 'img3']
	imgs = [img1, img2, img3]
	plot_images('image_bordering', titles, imgs)


# https://www.geeksforgeeks.org/image-pyramid-using-opencv-python/
def image_pyramid():
	path = askopen('zmax/n03_pyramid.png')
	sample = cv2.imread(path)
	result = sample.copy()
	trial = 4

	titles = ['sample']
	imgs = [sample]
	for i in range(trial):
		result = cv2.pyrDown(result)
		titles.append(f'trial / {i}')
		imgs.append(result)

	plot_images('image_pyramid', titles, imgs, axis='on')


# https://www.geeksforgeeks.org/python-grayscaling-of-imgs-using-opencv/
def image_grayscaling():
	path = askopen('zmax/n03_grayscaling.png')
	sample = cv2.imread(path)
	gray1 = cv2.imread(path, 0)
	gray2 = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
	gray3 = sample.copy()

	(row, col) = gray3.shape[0:2]
	# Take the average of pixel values of the BGR Channels to convert the colored image to grayscale image
	for i in range(row):
		for j in range(col):
			# Find the average of the BGR pixel values
			gray3[i, j] = sum(gray3[i, j]) * 0.33

	titles = ['sample', 'gray1', 'gray2', 'gray3']
	imgs = [sample, gray1, gray2, gray3]
	plot_images('image_grayscaling', titles, imgs)


# cv2.INTER_NEAREST
# cv2.INTER_LINEAR
# cv2.INTER_AREA / shrinking
# cv2.INTER_CUBIC / zooming
# https://www.geeksforgeeks.org/image-resizing-using-opencv-python/
# https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
def image_scaling():
	path = askopen('zmax/n03_scaling.png')
	sample = cv2.imread(path)
	height, width = sample.shape[:2]
	half = cv2.resize(sample, (0, 0), fx=0.5, fy=0.5)
	double = cv2.resize(sample, (0, 0), fx=2, fy=2)
	stretch_near = cv2.resize(sample, (780, 540), interpolation=cv2.INTER_NEAREST)
	specified = cv2.resize(sample, (int(0.1*width), int(0.1*height)), interpolation=cv2.INTER_CUBIC)

	titles = ['sample',  'half', 'double', 'interpolation_nearest', 'specified']
	imgs = [sample, half, double, stretch_near, specified]
	plot_images('image_scaling', titles, imgs, axis='on')


# https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
def image_rotating():
	path = askopen('zmax/n03_rotating.png')
	sample = cv2.imread(path)
	rows, cols = sample.shape[:2]
	# getRotationMatrix2D creates a matrix needed for transformation.
	# We want matrix for rotation w.r.t center to 45 degree without scaling.
	M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
	rotate = cv2.warpAffine(sample, M, (cols, rows))
	titles = ['sample', 'rotated']
	imgs = [sample, rotate]
	plot_images('image_rotating', titles, imgs)


# https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
def image_shifting():
	path = askopen('zmax/n03_shifting.png')
	sample = cv2.imread(path)
	M = np.float32([[1, 0, 100], [0, 1, -50]])
	rows, cols = sample.shape[:2]
	# warpAffine does appropriate shifting given the translation matrix.
	shift = cv2.warpAffine(sample, M, (cols, rows))
	titles = ['sample', 'shifted']
	imgs = [sample, shift]
	plot_images('image_shifting', titles, imgs)


if __name__ == "__main__":
	function_packages = [
		['image_generating', image_generating],
		['image_bordering', image_bordering],
		['image_pyramid', image_pyramid],
		['image_grayscaling', image_grayscaling],
		['image_scaling', image_scaling],
		['image_rotating', image_rotating],
		['image_shifting', image_shifting],
	]

	window_title = 'N03_IMAGE_MANIPULATION'
	dynamically_create_interface(window_title, function_packages)
