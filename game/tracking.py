import imutils
import cv2


# Initialize important stuff
XML_PATH = "/home/bikeboi/Wazz/dogdunk/game/venv/lib/python3.7/site-packages/cv2/data/"
face_cascade = cv2.CascadeClassifier(XML_PATH + 'haarcascade_frontalface_default.xml')
if not face_cascade:
    print("Could not print face cascade")
cap = cv2.VideoCapture("mwandia_2.mp4")
tracker_type = 'MIL'
tracker = cv2.TrackerMIL_create()

# Helper functions
def imageTransform(img,height):
    h, w, l = img.shape
    width = int((w * height) / h)
    resized = cv2.resize(img,(width,height))
    rotated = imutils.rotate(resized,269)
    return imutils.translate(rotated,-10,-10)

def maybeFindFace(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    return safeHead(faces)

def safeHead(lst):
    if len(lst) < 1: return None
    print(lst[0])
    return lst[0]

# Get first frame to get face to track
print("Finding face...")
foundFace = False
while cap.isOpened() and not foundFace:
    ok, img = cap.read()
    image = imageTransform(img,700)
    if not ok:
        print("Error happened when trying to detect face")
        break
    faceHolder = maybeFindFace(imageTransform(image,700))
    if faceHolder is None:
        pass
    else:
        x, y, w, h = faceHolder
        tracker.init(image,(x,y,w,h))
        foundFace = True
if not foundFace:
    print("Could not detect face...")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Transformations
    img = imageTransform(frame, 700)
    ok, bbox = tracker.update(img)
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(img,p1,p2,(255,0,0),2,1)
    # Actually draw the image
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
