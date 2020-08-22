# pip install pandas opencv-python

import cv2
import pandas as pd

img_path = input()
csv_path = 'all_the_colors_of_the_universe.csv.csv'


index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)


img = cv2.imread(img_path)
img = cv2.resize(img, (1000,800))

clicked = False
r = g = b = xpos = ypos = 0


def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname


def double_click(clicky, x_oord, y_coord, flags, paramaters):
	if clicky == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x_oord
		ypos = y_coord
		b,g,r = img[y_coord,x_oord]
		b = int(b)
		g = int(g)
		r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', double_click)

while True:
	cv2.imshow('image', img)
	if clicked:
		cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)
		text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()
