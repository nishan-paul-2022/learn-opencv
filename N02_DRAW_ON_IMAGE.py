import library
from library import *


# https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
def draw_straight_line():
    path = askopen(askopen('zmax/n02_draw.png'))
    sample = cv2.imread(path)
    start_point, end_point = (0, 0), (250, 250)  # top-left-corner, bottom-right-corner
    color = [255, 0, 0]
    thickness = 9  # Line thickness of 9 px
    # Using cv2.line() method. Draw a diagonal green line with thickness of 9 px
    result = cv2.line(sample, start_point, end_point, color, thickness)
    show_frame('draw_straight_line', result)


# https://www.geeksforgeeks.org/python-opencv-cv2-arrowedline-method/
def draw_arrowed_line():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    start_point, end_point = (0, 0), (200, 200)  # top-left-corner, bottom-right-corner
    color = [255, 0, 0]
    thickness = 9
    result = cv2.arrowedLine(sample, start_point, end_point, color, thickness)
    show_frame('draw_arrowed_line', result)


# https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/
def draw_polyline():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    # Polygon corner points coordinates
    points = np.array([
        [25, 70], [25, 160],
        [110, 200], [200, 160],
        [200, 70], [110, 20]],
        np.int32
    )
    points = points.reshape((-1, 1, 2))
    points = [points]
    isClosed = True
    color = [255, 0, 0]
    thickness = 2
    result = cv2.polylines(sample, points, isClosed, color, thickness)
    show_frame('draw_polyline', result)


# https://www.geeksforgeeks.org/python-opencv-cv2-ellipse-method/
def draw_ellipse():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    center_coordinates = (120, 100)
    axesLength = (100, 50)
    angle = 0
    startAngle, endAngle = 0, 360
    color = [255, 0, 0]
    thickness = 5
    # Using cv2.ellipse() method. Draw a ellipse with red line borders of thickness of 5 px
    result = cv2.ellipse(sample, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)
    show_frame('draw_ellipse', result)


# https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/
def draw_circle():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    center_coordinates = (120, 50)
    radius = 20
    color = [255, 0, 0]
    thickness = 2
    # Using cv2.circle() method. Draw a circle with blue line borders of thickness of 2 px
    result = cv2.circle(sample, center_coordinates, radius, color, thickness)
    show_frame('draw_circle', result)


# https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/
def draw_rectangle():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    start_point, end_point = (5, 5), (220, 220)
    color = [255, 0, 0]
    thickness = 2
    # Using cv2.rectangle() method. Draw a rectangle with blue line borders of thickness of 2 px
    result = cv2.rectangle(sample, start_point, end_point, color, thickness)
    show_frame('draw_rectangle', result)


# https://www.geeksforgeeks.org/draw-a-triangle-with-centroid-using-opencv/
def draw_triangle():
    path = askopen('zmax/n02_draw.png')
    sample = cv2.imread(path)
    radius = 8
    color = [255, 0, 0]
    thickness = 4

    # Three vertices(tuples) of the triangle
    p1 = (100, 200)
    p2 = (50, 50)
    p3 = (300, 100)

    # Drawing the triangle with the help of lines on the black window With given points.
    # cv2.line is the inbuilt function in opencv library
    cv2.line(sample, p1, p2, color, thickness)
    cv2.line(sample, p2, p3, color, thickness)
    cv2.line(sample, p1, p3, color, thickness)

    # finding centroid using the following formula. (X, Y) = (x1 + x2 + x3//3, y1 + y2 + y3//3)
    centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)
    # Drawing the centroid on the window
    cv2.circle(sample, centroid, radius, color)
    show_frame('draw_triangle', sample)


if __name__ == "__main__":
    function_packages = [
        ['draw_straight_line', draw_straight_line],
        ['draw_arrowed_line', draw_arrowed_line],
        ['draw_polyline', draw_polyline],
        ['draw_ellipse', draw_ellipse],
        ['draw_circle', draw_circle],
        ['draw_rectangle', draw_rectangle],
        ['draw_triangle', draw_triangle],
    ]

    window_title = 'N02_DRAW_ON_IMAGE'
    dynamically_create_interface(window_title, function_packages)