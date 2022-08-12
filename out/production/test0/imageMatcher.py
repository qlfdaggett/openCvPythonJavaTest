import cv2
import sys

if len(sys.argv) < 3:
	print("Missing argument(s), needs 2 image file names")
	sys.exit()

# Read in image files and get dimensions of target screnshot
img = cv2.imread(sys.argv[1],0)
template = cv2.imread(sys.argv[2], 0)
w, h = template.shape[::-1]

# Determine location of matching template
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Calculate center of matching template and print to console
center = (int(max_loc[0] + (w/2)), int(max_loc[1] + (h/2)))

print("{0} {1}".format(center[0], center[1]))
#cv2.circle(img, center, 5,255, 5)

#cv2.imshow("image", img)



#cv2.waitKey(0)
#cv2.destroyAllWindows()
