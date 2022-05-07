

import imgui
import os
from Gui import mat_2_tex
import unittest
import cv2 as cv
class Animation():
	def __init__(self,path):
		if path is None:
			raise "Path is None"

		self.sprites=[]
		self.p=0
		

		images=[]
		for p in os.listdir(path):
			p=os.path.join(path,p)
			if not os.path.isdir(p):
				print(p)
				im=cv.imread(p)
				self.sprites.append(mat_2_tex(im))
				#cv.imshow("asd",im)



	def draw(self,n,w=100,h=100):
		n=int(len(self.sprites)*n)
		n= n if n<len(self.sprites) else len(self.sprites)-1
		if len(self.sprites)>0:
			imgui.image(self.sprites[n][0], w, h)
		else:
			imgui.dummy(w,h)
		

	def __del__(self):
		print("TODO DELETE OPENGL TEXTURE")
		for p in self.sprites:
			pass
			
			


def showProgresbar(n,sx=200,sy=20):
	imgui.dummy(sx,sy)
	bx,by=imgui.core.get_item_rect_min()
	rx,ry=imgui.core.get_item_rect_max()
	nx=(rx-bx)*n
	#print(imgui.core.get_item_rect_max())
	#print(imgui.core.get_item_rect_min())
	draw_list = imgui.get_window_draw_list()
	draw_list.add_rect_filled(bx,by, rx,ry, imgui.get_color_u32_rgba(0.2,0.2,0.2,1))
	draw_list.add_rect_filled(bx,by, nx,ry, imgui.get_color_u32_rgba(0.1,1,0.1,1))
	#print(nx)




if __name__ == "__main__":
	print("No main for this one")
	