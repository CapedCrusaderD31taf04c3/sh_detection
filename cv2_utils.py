import cv2
import numpy as np
def read_image(image_path : str):
    """

    :param image_path:
    :return:
    """
    image = cv2.imread(image_path)
    return image

def convert_color_to_gray(image):
    """

    :param image:
    :return:
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def draw_filled_point_and_add_number(image, location_points: list[list[int]]):
    """

    :param image:
    :param location_points:
    :return:
    """
    count = 0
    for location in location_points:
        cv2.circle(image, (location[0], location[1]), 3, (0, 0, 255), -1)
        cv2.putText(image, str(count), (location[0], location[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        count += 1
    return image

def show_image_and_wait(image) -> bool:
    """

    :param image:
    :return:
    """
    cv2.imshow("Color", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return True

def get_masked_image(image, polygon_points):
    """

    :param image:
    :param polygon_points:
    :return:
    """
    polygon_points_array = np.array(polygon_points)
    convex_hull_wrap = cv2.convexHull(polygon_points_array)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [convex_hull_wrap], (255, 255, 255))

    return mask


def resize_image_by_percentage(image, scale_percent: int):
    """

    :param image:
    :param percentage:
    :return:
    """

    # calculate the 50 percent of original dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    resized_image = cv2.resize(image, dsize)

    return resized_image


def save_image_at_path(path, image) -> bool:
    """

    :param image:
    :param path:
    :return:
    """
    cv2.imwrite(path,image)

    return True
























































