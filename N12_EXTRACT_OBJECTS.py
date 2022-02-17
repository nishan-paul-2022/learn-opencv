import library
from library import *


# https://www.geeksforgeeks.org/python-draw-rectangular-shape-and-extract-objects-using-opencv/
class extract_objects_from_image_using_cursor:
    def __init__(self):
        self.window_name = 'sample'
        path = askopen('zmax/n12_extract_using_cursor.png')
        self.img = cv2.imread(path)
        self.img_ = self.img.copy()
        self.ref_point = list()
        self.main()

    def shape_selection(self, event, x, y, _, __):
        if event == cv2.EVENT_LBUTTONDOWN:  # if the left mouse button was clicked, record the starting (x, y) coordinates and indicate that cropping is being performed
            self.ref_point = [(x, y)]
        elif event == cv2.EVENT_LBUTTONUP:  # check to see if the left mouse button was released
            self.ref_point.append((x, y))  # record the ending (x, y) coordinates and indicate that the cropping operation is finished
            color = [255, 0, 0]
            cv2.rectangle(self.img, self.ref_point[0], self.ref_point[1], color, 2)  # draw a rectangle around the region of interest
            cv2.imshow(self.window_name, self.img)
    
    def main(self):
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.shape_selection)
    
        while True:
            cv2.imshow(self.window_name, self.img)
            key = cv2.waitKey(0)
            if key == ord('r'):  # press 'r' to reset the window
                self.img = self.img_.copy()
            if key == ord('c'):  # if the 'c' key is pressed, break from the loop
                break
            if key == ord('q'):  # if the 'c' key is pressed, break from the loop
                cv2.destroyAllWindows()
                return 0
    
        if len(self.ref_point) == 2:
            extracted = self.img_[self.ref_point[0][1]:self.ref_point[1][1], self.ref_point[0][0]:self.ref_point[1][0]]
            show_frame('extracted', extracted)


# https://stackoverflow.com/questions/56604151/python-extract-multiple-objects-from-img-opencv
def extract_objects_from_image_using_contour_detection():
    path = askopen('zmax/n12_extract_using_contour.png')
    sample = cv2.imread(path)
    img = sample.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 120, 255, 1)
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(canny, kernel, iterations=1)
    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours
    contours = contours[0] if len(contours) == 2 else contours[1]
    titles = list()
    imgs = list()
    idx = 1

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)
        ROI = sample[y:y + h, x:x + w]
        titles.append(f'object {idx}')
        imgs.append(ROI)
        idx += 1

    titles += ['objects']
    imgs += [img]
    titles.reverse(), imgs.reverse()
    plot_images('extract_objects_from_image_using_contour_detection', titles, imgs)


if __name__ == '__main__':
    function_packages = [
        ['extract_objects_from_image_using_cursor', extract_objects_from_image_using_cursor],
        ['extract_objects_from_image_using_contour_detection', extract_objects_from_image_using_contour_detection],
    ]

    window_title = 'N12_EXTRACT_OBJECTS'
    dynamically_create_interface(window_title, function_packages)