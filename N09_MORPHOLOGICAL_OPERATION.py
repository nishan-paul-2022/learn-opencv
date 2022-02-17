import library
from library import *


# https://www.geeksforgeeks.org/python-morphological-operations-in-image-processing-opening-set-1/
def morphological_operation():
	vCap = cv2.VideoCapture(0)  # return video from the first webcam on your computer.
	while vCap.isOpened():  # loop runs if capturing has been initialized.
		_, image = vCap.read()  # reads frames from a camera
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Converts to HSV color space, OCV reads colors as BGR frame is converted to hsv
		blue1 = np.array([110, 50, 50])  # defining the range of masking
		blue2 = np.array([130, 255, 255])
		mask = cv2.inRange(hsv, blue1, blue2)  # initializing the mask to be convoluted over input image
		kernel = np.ones((5, 5), np.uint8)  # defining the kernel i.e. Structuring element

		# passing the bitwise_and over each pixel convoluted
		# dont_know = cv2.bitwise_and(image, image, mask=mask)
		# defining the opening function over the image and structuring element
		morph_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
		morph_close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
		morph_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

		# The mask and opening operation is shown in the window
		frames = [image, mask, morph_open, morph_close, morph_gradient]
		combined = image_merge(frames)
		combined = image_resize_specified(combined, 1, 0.5)
		show_frame('morphological_operation', combined, [vCap])


# https://www.geeksforgeeks.org/image-segmentation-using-morphological-operation/
def image_segmentation_using_morphological_operation():
	img = cv2.imread('zmax/n09_segmentation_using_morphology.png')  # image operation using thresholding
	titles = ['sample']
	imgs = [img]

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
	titles.append('thresh')
	imgs.append(thresh)

	kernel = np.ones((3, 3), np.uint8)  # noise removal using Morphological closing operation
	closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
	# background = cv2.dilate(closing, kernel, iterations=1)  # Background area using Dialation
	dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)  # Finding foreground area
	_, fg = cv2.threshold(dist_transform, 0.02 * dist_transform.max(), 255, 0)
	titles.append('fg')
	imgs.append(fg)

	plot_images('image_segmentation_using_morphological_operation', titles, imgs)


if __name__ == '__main__':
	function_packages = [
		['morphological_operation', morphological_operation],
		['image_segmentation_using_morphological_operation', image_segmentation_using_morphological_operation],
	]

	window_title = 'N09_MORPHOLOGICAL_OPERATION'
	dynamically_create_interface(window_title, function_packages)