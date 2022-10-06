import cv2


if __name__ == "__main__":
    cam = cv2.VideoCapture(2)

    while True:
        ret, frame = cam.read()
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.imwrite("frame.png", frame)
            frame = cv2.imread("frame.png")
            cv2.imshow("frame", frame)
            cv2.waitKey(0)
            break
