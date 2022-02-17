import library
from library import *


def bitwise_operation(opertion_name, path1, path2):
	img1 = cv2.imread(path1)
	img2 = cv2.imread(path2)
	img3 = getattr(cv2, opertion_name)(img1, img2, mask=None)
	titles = ['img1', 'img2', 'img3']
	imgs = [img1, img2, img3]
	plot_images(opertion_name, titles, imgs)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-arithmetic_addition-and-arithmetic_subtraction/
def arithmetic_addition():
	path1, path2 = askopen('zmax/n04_addition_a.png'), askopen('zmax/n04_addition_b.png')
	img1 = cv2.imread(path1)
	img2 = cv2.imread(path2)
	img3 = cv2.addWeighted(img1, .5, img2, 0.4, 0)  # cv2.addWeighted is applied over the image inputs with applied parameters
	titles = ['img1', 'img2', 'img3']
	imgs = [img1, img2, img3]
	plot_images('arithmetic_addition', titles, imgs)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-arithmetic_addition-and-arithmetic_subtraction/
def arithmetic_subtraction():
	path1, path2 = askopen('zmax/n04_subtraction_a.png'), askopen('zmax/n04_subtraction_b.png')
	img1 = cv2.imread(path1)
	img2 = cv2.imread(path2)
	img3 = cv2.subtract(img1, img2)  # cv2.subtract is applied over the image inputs with applied parameters
	titles = ['img1', 'img2', 'img3']
	imgs = [img1, img2, img3]
	plot_images('arithmetic_subtraction', titles, imgs)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/
def bitwise_and():
	path1, path2 = askopen('zmax/n04_bitwise_a.png'), askopen('zmax/n04_bitwise_b.png')
	bitwise_operation('bitwise_and', path1, path2)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/
def bitwise_or():
	path1, path2 = askopen('zmax/n04_bitwise_a.png'), askopen('zmax/n04_bitwise_b.png')
	bitwise_operation('bitwise_or', path1, path2)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/
def bitwise_xor():
	path1, path2 = askopen('zmax/n04_bitwise_a.png'), askopen('zmax/n04_bitwise_b.png')
	bitwise_operation('bitwise_xor', path1, path2)


# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/
def bitwise_not():
	path = askopen('zmax/n04_bitwise_a.png')
	img1 = cv2.imread(path)
	img2 = cv2.bitwise_not(img1, mask=None)
	titles = ['img1', 'img2']
	imgs = [img1, img2]
	plot_images('bitwise_not', titles, imgs)


if __name__ == "__main__":
	function_packages = [
		['arithmetic_addition', arithmetic_addition],
		['arithmetic_subtraction', arithmetic_subtraction],
		['bitwise_and', bitwise_and],
		['bitwise_or', bitwise_or],
		['bitwise_xor', bitwise_xor],
		['bitwise_not', bitwise_not],
	]

	window_title = 'N04_ARITHMETC_AND_BITWISE_OPERATION'
	dynamically_create_interface(window_title, function_packages)