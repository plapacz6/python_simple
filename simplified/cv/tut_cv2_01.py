
import cv2 as cv
import numpy as np

img = np.zeros((600,900,3), dtype=np.uint8)
cv.rectangle(img, (0,0),(900,500),(255,225,85), -1)
cv.rectangle(img, (0,500),(900,600),(75,180,70), -1)
cv.circle(img, (200,150), 60, (0,255,255), -1)
cv.circle(img, (200,150), 75, (220,255,255), 10)
cv.line(img, (600,500),(600,420), (30,65,155), 25)
triangle = np.array([[550,440],[700,440],[600,75]], dtype=np.int32)
cv.fillPoly(img, [triangle], (75,180,70))
#text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img, "I Love Pythonw", (120,490), font, 1.5, (255,255,255), 2)

cv.imwrite("tree.png", img)
cv.imshow("tree", img)

cv.waitKey(0)
cv.destroyAllWindows()
