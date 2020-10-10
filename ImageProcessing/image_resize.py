import cv2
import os


def resize(image_name, x=100, y=100):
    # flag = 1 for colored, 0 for black and white, -1 color with alpha (transparency)
    img = cv2.imread(image_name, 1)
    image_name = os.path.split(image_name)
    new_name = 'resized_'+image_name[-1]
    new_name = os.path.join(*image_name[:-1], new_name)
    resized_image = cv2.resize(img, (x, y))
    cv2.imwrite(new_name, resized_image)


def try_multiple_image_resizing():
    # you need to change the path
    dir_name = './images'
    for image in os.listdir(dir_name):
        if not image[-4:] == '.jpg' and not image[-4:] == '.png' or image.startswith('resized_'):
            print('Already Resized image: ' + image)
            continue
        image_name = os.path.join(dir_name, image)
        # change size params
        width, height = 1900, 1080
        resize(image_name, width, height)


if __name__ == '__main__':
    try_multiple_image_resizing()
