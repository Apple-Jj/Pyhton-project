import cv2 as cv

# 判断人脸的方法
fd = cv.CascadeClassifier('./haarcascade_frontalface_alt.xml')

vc = cv.VideoCapture(0)
print(vc)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (123, 123, 230), 3)
    cv.imshow('frame', frame)
    if cv.waitKey(40) == 27:
        break

vc.release()
cv.destroyAllWindows()