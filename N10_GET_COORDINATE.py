import library
from library import *


def put_coordinate(event, x, y, _, window_name_and_img):
	window_name, img = window_name_and_img
	text = None

	if event == cv2.EVENT_LBUTTONDOWN:  # checking for left mouse clicks
		text = f'{x}, {y}'

	if event == cv2.EVENT_RBUTTONDOWN:  # checking for right mouse clicks
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		text = f'{b}, {g}, {r}'

	put_text_on_image(img, text, (x, y))
	cv2.imshow(window_name, img)


# https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
def get_coordinate_of_clicked_point():
	window_name = 'get_coordinate_of_clicked_point'
	path = askopen('zmax/n10_coordinates.png')
	img = cv2.imread(path)
	cv2.imshow(window_name, img)
	# setting mouse handler for the image and calling the put_coordinate() function
	cv2.setMouseCallback(window_name, put_coordinate, (window_name, img))
	if cv2.waitKey(0) == ord('q'):
		cv2.destroyAllWindows()


if __name__ == '__main__':
	function_packages = [
		['get_coordinate_of_clicked_point', get_coordinate_of_clicked_point],
	]

	window_title = 'N10_GET_COORDINATE'
	dynamically_create_interface(window_title, function_packages)