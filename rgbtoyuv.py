from numpy import *
#import numpy as np
#print(np.version.version)
from PIL import Image
import sys

def yuv_import(filename, dims, frmnum, startfrm):
	fp=open(filename,'rb')
	if (fp == None):
		print ("Error open yuv image")
		return
	blk_size=prod(dims)*3/2
	fp.seek(int(blk_size*startfrm), 0)
	Y=[]
	U=[]
	V=[]
	width=dims[0]//2
	height=dims[1]//2
	print(width,dims[0])
	print(height,dims[1])
	yt=zeros((dims[0],dims[1]), uint8, 'C')
	ut=zeros((width,height), uint8, 'C')
	vt=zeros((width,height), uint8, 'C')
	for i in range(frmnum):
		for wn in range(dims[0]):
			for hn in range(dims[1]):
				yt[wn,hn]=ord(fp.read(1))
		for wn in range(width):
			for hn in range(height):
				ut[wn,hn]=ord(fp.read(1))
		for wn in range(width):
			for hn in range(height):
				vt[wn,hn]=ord(fp.read(1))
		Y=Y + [yt]
		U=U + [ut]
		V=V + [vt]
	fp.close()
	return(Y,U,V)
def main():
	strarc=sys.argv[1]
	res=strarc.split('x')
	if (len(res) != 2):
		print("Error input,please add 'wxh'!")
		return
	data=yuv_import("./test.yuv", (int(res[0]),int(res[1])), 1, 0)
	yy=data[0][0]
	if (yy is None):
		print(" get yuv data error")
		return
	print(yy.shape)
	im=Image.frombytes('L', (int(res[0]),int(res[1])),yy.tostring())
	if (im == None):
		print("error image get")
	im.show
	im.save("./test.jpeg")
main()
