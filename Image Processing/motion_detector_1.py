import cv2
import time


if __name__ == '__main__':
    first_frame = None
    video = cv2.VideoCapture(0)
    time.sleep(0.5)
    cnt = 0
    while True:
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (27, 27), 0)
        cnt += 1
        if first_frame is None:
            first_frame = gray
            continue
        if cnt%7 == 0:
            first_frame = gray

        delta_frame = cv2.absdiff(first_frame, gray)
        thresh_frame = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, kernel=None, iterations=2)

        (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        cv2.imshow('first', delta_frame)
        cv2.imshow('Capturing', frame)

        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()