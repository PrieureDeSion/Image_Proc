import PIL
from PIL import Image
import numpy
import matplotlib.pyplot as plot
import matplotlib.image as mimg
import time
from copy import deepcopy

def threshold(array):
	tempAr = []
	newAr = deepcopy(array)
	array.flags.writeable = True
	for eachRow in array:
		for eachPix in eachRow:
			avg = reduce(lambda x, y: x+y, eachPix[:3])/3
			tempAr.append(avg)
	bal = reduce(lambda x, y: x+y,tempAr)/len(tempAr)
	for eachRow in newAr:
		for eachPix in eachRow:
			if reduce(lambda x, y: x+y, eachPix[:3])/3 > bal :
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				eachPix[3] = 255
	return newAr

img1 = Image.open('images/numbers/0.1.png')
img2 = Image.open('images/numbers/y0.5.png')
img3 = Image.open('images/sentdex.png')
img4 = Image.open('images/numbers/y0.4.png')
imgAr1 = numpy.asarray(img1)
imgAr2 = numpy.asarray(img2)
imgAr3 = numpy.asarray(img3)
imgAr4 = numpy.asarray(img4)

new2 = threshold(imgAr2)
new3 = threshold(imgAr3)
new4 = threshold(imgAr4)
plt1 = plot.subplot2grid((8,8), (0,0), rowspan=4, colspan = 4)
plt2 = plot.subplot2grid((8,8), (4,0), rowspan=4, colspan = 4)
plt3 = plot.subplot2grid((8,8), (0,4), rowspan=4, colspan = 4)
plt4 = plot.subplot2grid((8,8), (4,4), rowspan=4, colspan = 4)

plt1.imshow(imgAr1)
plt2.imshow(new2)
plt3.imshow(new3)
plt4.imshow(new4)

plot.show()
#print imgAr
#plot.imshow(imgAr)
#plot.show()
