# Color_detection

## Introduction

#### For this project I wanted to implement Computer vision. I did go through a lot of different ideas.
#### I wanted something that would make it easy to detect what colors are in a photograph (I recently have gotten into photography, so wanted something along those lines). The RGB and the human readable color so that I can paint it, or if I'm just curious so that I may talk about it.
#### First I thought about a machine learning model that would tell me the top 10 colors used in an image. This seemed challenging but fun
#### I then thought about an algorithm that would draw out a certain color of your choice. So choose blue, then everything that's "blue" in that picture would be highlighted. 
#### Example can be found here: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
#### In the end though, after some attemps at both models and algorithms, I figured a simple point and click would be the best option and by far the most efficient for what i'm going for.

##### The reason this is the best method is this method can make the user decide how many colors are relevant to their needs. Rather of the machine learning algorithm deciding 10 or X number of colors are relevant, just let the user decide. This can stop having too much information if the user just wants one or a few colors detected.

#### A simple point and click algorithm was decided upon using opencv.

<p>&nbsp;</p>

#### This will be ran on bash or cmd. Just run the python script.
#### Lets first run it before explaining how it works just to see it in action
## While running from your terminal you should see something like this
#### you can find these files in the "download_these" folder in this github

![](https://github.com/Xderic2/Color_detection/blob/master/images/bash_terminal.PNG)

#### If this does not work, then make sure you have all the packages installed

```bash
pip install pandas opencv-python
```

#### After this. Enter in the command

```bash
 python color_detection.py
```
#### After that, enter in the path of the picture you want to see. This can be anywhere on your computer. 
#### Make sure there are no quotes in the path if you use the "copy path" shift-right click method on your picture
#### press enter and the picture should pop up as seen below
#### double click on any pixel to get the RGB and the human readable color of the pixel. This will resize everything, so it may be warped a bit

![](https://github.com/Xderic2/Color_detection/blob/master/images/paul_andrus.PNG)

#### We can see Regis first Data Science Masters graduate has a Dark Sienna skin complexion under low light.

#### We can see some drastic resizing on the image below of my favorite graduate. Unfortunately all pics had to go to one size. After some tweaking most of mine looked pretty good at 1000 by 800. This can be changed in the code quite easily to have user input though if someone wanted. I could not figure out a way to not have it at all though.

![](https://github.com/Xderic2/Color_detection/blob/master/images/carly_bear.PNG)

#### Apparently angels are "Grullo" colored. 
#### The text is placed there by OpenCV "puttext" https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
#### The algorithm can iterate over as many pixels as you want, so you can keep on clicking if your heart desires
##### To exit out of the terminal, just press ctr + C. Might take a few seconds

## The code/how it works

#### now that we've seen it in action, lets see what's under the hood. As stated earlier, you may download the python file from this github under "download_these/color_detection.py"

#### First make sure you have these packages
```bash
pip install pandas opencv-python
```
<p>&nbsp;</p>

#### Then import said packages

```python
import cv2
import pandas as pd
```
#### This is the csv we're using as the colors.
##### This can be found under download_these/all_the_colors_of_the_universe.csv

![](https://github.com/Xderic2/Color_detection/blob/master/images/colors.PNG)

#### First we read into the csv

```python
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)
```

#### We then resize it
```python
img = cv2.imread(img_path)
img = cv2.resize(img, (1000,800))
```

#### If you wanted to have less distortion on your own set up on photos then you can use something like this

```python
x_dimension = input()
y_dimension = input()
img = cv2.imread(img_path)
img = cv2.resize(img, (x_dimension,y_dimension))
```

#### Since this is not exactly for viewing pleasure and exactness from that perspective, it's not needed, but the option is there

#### We then calculate the minimum distance iteating over all the colors. We want the one that matches most closesly to it

```python
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
```

#### We then get a function that gets the x and y coordinates from a doubleclick
##### More can be found here about how to do that, and different methods - https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

```python
def double_click(clicky, x_oord, y_coord, flags, paramaters):
	if clicky == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x_oord
		ypos = y_coord
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)
```

#### We create a window, then add in the text that you see at the top left as shown below

![](https://github.com/Xderic2/Color_detection/blob/master/images/top_left.PNG)

```python
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
```


























