import cv2
import os

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')


def face_detector(images):
    for image in images:
        if not image[-4:] == '.jpg' and not image[-4:] == '.png':
            continue
        img = cv2.imread(os.path.join(base_dir, image))
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray_img,
            scaleFactor=1.1,
            minNeighbors=5
        )
        for x, y, w, h in faces:
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Image', img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    base_dir = 'faces'
    images = os.listdir(base_dir)
    face_detector(images)
