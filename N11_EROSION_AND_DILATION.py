import library
from library import *


# https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html
class erosion_and_dilation:
    def __init__(self):  
        path = askopen('zmax/n11_erosion_and_dilation.png')
        self.sample = cv2.imread(path)
        self.morph_shape = {0: cv2.MORPH_RECT, 1: cv2.MORPH_CROSS, 2: cv2.MORPH_ELLIPSE}
        self.title_erosion = 'EROSION'
        self.title_dilation = 'DILATION'
        self.trackbar_element_shape = 'S'  # element shape: [0: rect] [1: cross] [2: ellipse]
        self.trackbar_kernel_size = 'K'  # kernel size: 2n+1
        self.main()

    def create_window(self, title, function):
        max_elem = 2
        max_kernel_size = 21
        cv2.namedWindow(title)
        cv2.createTrackbar(self.trackbar_element_shape, title, 0, max_elem, function)
        cv2.createTrackbar(self.trackbar_kernel_size, title, 0, max_kernel_size, function)

    def morphology(self, title, function):
        shape = self.morph_shape[cv2.getTrackbarPos(self.trackbar_element_shape, title)]
        size = cv2.getTrackbarPos(self.trackbar_kernel_size, title)
        element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1), (size, size))
        dst = function(self.sample, element)
        cv2.imshow(title, dst)

    def erosion(self, _):
        self.morphology(self.title_erosion, cv2.erode)

    def dilation(self, _):
        self.morphology(self.title_dilation, cv2.dilate)

    def main(self):
        self.create_window(self.title_erosion, self.erosion)
        self.create_window(self.title_dilation, self.dilation)
        self.erosion(None)
        self.dilation(None)
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()


if __name__ == "__main__":
    function_packages = [
        ['erosion_and_dilation', erosion_and_dilation],
    ]

    window_title = 'N11_EROSION_AND_DILATION'
    dynamically_create_interface(window_title, function_packages)