import library
from library import *


def _foreground_extraction_using_grabcut_algorithm(img):
	result = img.copy()
	# Create a simple mask image similar to the loaded image, with the shape and return type
	mask = np.zeros(result.shape[:2], np.uint8)
	# Specify the background and foreground model using numpy the array is constructed of 1 row and 65 columns,
	# and all array elements are 0. Data type for the array is np.float64 (default)
	backgroundModel = np.zeros((1, 65), np.float64)
	foregroundModel = np.zeros((1, 65), np.float64)
	# Define the ROI as the coordinates of the rectangle where the values are entered as (startingPoint_x, startingPoint_y, width, height).
	# These coordinates are according to the input image. it may vary for different image
	rectangle = (20, 100, 150, 150)
	# apply the grabcut algorithm with appropriate values as parameters (number of iterations = 3)
	# cv2.GC_INIT_WITH_RECT is used because of the rectangle mode is used
	cv2.grabCut(result, mask, rectangle, backgroundModel, foregroundModel, 3, cv2.GC_INIT_WITH_RECT)
	# In the new mask image, pixels will be marked with four flags four flags denote the background / foreground mask is changed,
	# all the 0 and 2 pixels are converted to the background mask is changed,
	# all the 1 and 3 pixels are now the part of the foreground the return type is also mentioned, this gives us the final mask
	mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
	result = result * mask2[:, :, np.newaxis]  # The final mask is multiplied with the input image to give the segmented image.
	return result


# https://www.geeksforgeeks.org/python-foreground-extraction-in-an-image-using-grabcut-algorithm/
def foreground_extraction_using_grabcut_algorithm():
	path = askopen('zmax/n26_extraction_and_subtraction.mp4')
	vCap = cv2.VideoCapture(path)
	screens = [vCap]

	while vCap.isOpened():
		ret, frame = vCap.read()
		if not ret:
			break
		extracted = _foreground_extraction_using_grabcut_algorithm(frame)
		frames = [frame, extracted]
		combined = image_merge(frames)
		show_frame('foreground_extraction_using_grabcut_algorithm', combined, screens)


# https://www.geeksforgeeks.org/python-background-subtraction-using-opencv/
def background_subtraction_using_mog2():
	path = askopen('zmax/n26_extraction_and_subtraction.mp4')
	vCap = cv2.VideoCapture(path)
	screens = [vCap]
	fgbg = cv2.createBackgroundSubtractorMOG2()
	while vCap.isOpened():
		ret, frame = vCap.read()
		if not ret:
			break
		fgmask = fgbg.apply(frame)
		frames = [frame, fgmask]
		combined = image_merge(frames)
		show_frame('background_subtraction_using_mog2', combined, screens)


# https://www.geeksforgeeks.org/background-subtraction-in-an-image-using-concept-of-running-average/
def background_subtraction_using_running_average_concept():
	vCap = cv2.VideoCapture(0)  # capture frames from a camera
	screens = [vCap]
	_, frame = vCap.read()  # read the frames from the camera
	avg_value = np.float32(frame)  # modify the data type setting to 32-bit floating point

	while vCap.isOpened():
		_, frame = vCap.read()  # reads frames from a camera
		# using the cv2.accumulateWeighted() function that updates the running average
		cv2.accumulateWeighted(frame, avg_value, 0.02)
		# converting the matrix elements to absolute values and converting the result to 8-bit.
		frame_ = cv2.convertScaleAbs(avg_value)  # output of alpha value 0.02
		frames = [frame, frame_]
		combined = image_merge(frames)
		show_frame('background_subtraction_using_running_average_concept', combined, screens)


if __name__ == '__main__':
	function_packages = [
		['foreground_extraction_using_grabcut_algorithm', foreground_extraction_using_grabcut_algorithm],
		['background_subtraction_using_mog2', background_subtraction_using_mog2],
		['background_subtraction_using_running_average_concept', background_subtraction_using_running_average_concept],
	]

	window_title = 'N26_EXTRACTION_AND_SUBTRACTION'
	dynamically_create_interface(window_title, function_packages)
