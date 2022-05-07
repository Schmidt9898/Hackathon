import time
from Gui import * 
import imgui
import matplotlib.pyplot as plt
from Animated import *
import webbrowser

from Data_example import Data_obj # remove this

class App_window(Gui_Window):
	

	def __init__(self,w=640,h=480,title="Life is good, but can be better."):
		super(App_window, self).__init__(w,h,title)
		
		self.tabs=["input","plot","progresbar","radioweb","anim"]
		#self.cur_tab=self.tabs[0] if len(self.tabs)>0 else None
		self.cur_tab="b"
		self.fps=0
		self.fps_time=0
		self.data=Data_obj()



		io = imgui.get_io()												 #font
		self.new_font = io.fonts.add_font_from_file_ttf("./DroidSans.ttf", 30,)
		self.impl.refresh_font_texture()


		self.anim=Animation("./anim0")


		#testing plot
		########################################################
		fig = plt.figure()
		x1 = np.linspace(0.0, 5.0)
		x2 = np.linspace(0.0, 2.0)

		y1 = np.cos(2 * np.pi * x1) * np.exp(-x1) 
		y2 = np.cos(2 * np.pi * x2)

		ax = fig.add_subplot(2,1,1)
		line1, = ax.plot(x1, y1, 'ko-')        # so that we can update data later
		ax.set_title('A tale of 2 subplots')
		ax.set_ylabel('Damped oscillation')

		ay = fig.add_subplot(2, 1, 2)
		ay.plot(x2, y2, 'r.-')
		ay.set_xlabel('time (s)')
		ay.set_ylabel('Undamped')
		img = fig_2_mat(fig)
		#cv.imshow("asd",img)
		#plt.show()
		self.plot_text= mat_2_tex(img)
		#####################################
		self.n=0
		self.nc=0.001
		# Radio test
		self.radio_selected = 0
		


	def context(self):
		self.fps+=1
		if self.fps_time<time.time():
			print(self.fps)
			self.fps_time=time.time()+1
			self.fps=0.0



		imgui.push_font(self.new_font)
		io = imgui.get_io()
		#print(io.display_size.x)
		w_flags= imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_MENU_BAR
		
		imgui.set_next_window_position(0,0)
		imgui.set_next_window_size(io.display_size.x,io.display_size.y)
		imgui.begin("main",flags=w_flags)

		if imgui.begin_menu_bar():
			#imgui.button("asd")
			#imgui.selectable("sad")
			for i in self.tabs:
				if imgui.menu_item(i)[0]:
					print(i)
					self.cur_tab=i
	

			#if imgui.begin_menu('File'):
			#	print(imgui.menu_item('Close'))
			#	imgui.end_menu()

			imgui.end_menu_bar()
		
		
		if self.cur_tab == "input":
			self.sceen_test()
		elif self.cur_tab == "plot":
			self.sceen_menu()
		elif self.cur_tab == "progresbar":
			showProgresbar(self.n,1000)
			showProgresbar(self.n,1000)
			showProgresbar(self.n,1000)
			imgui.text("adsdasd")
			showProgresbar(self.n,1000)
			if self.n > 1 :
				self.n=0.0
			self.n+=0.001
		elif self.cur_tab == "radioweb":
			self.sceen_radio()
			self.sceen_url()
		elif self.cur_tab == "anim":
			self.anim.draw(self.n)
			imgui.text("anim")
			self.n+=self.nc
			if self.n > 1 or self.n<0:
				self.nc*=-1
		elif self.cur_tab == "d":
			imgui.text("tab d")




		
		#if imgui.button("nyomj meg",):
		#	print("most")
		imgui.end()
		imgui.pop_font()

	def sceen_url(self):
		if imgui.button('webbrowser docs'):
			webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
		if imgui.button('Lung Cancer Info'):
			webbrowser.open('https://en.wikipedia.org/wiki/Lung_cancer')
		if imgui.button('Survivor Stories <3'):
			webbrowser.open('https://en.wikipedia.org/wiki/Walter_White_(Breaking_Bad)')
		if imgui.button('Donation'):
			webbrowser.open('http://www.savewalterwhite.com/')
	
	def sceen_radio(self):
		if imgui.radio_button("Walt", self.radio_selected==0):
		    self.radio_selected = 0
		elif imgui.radio_button("Hank", self.radio_selected==1):
		    self.radio_selected = 1
		elif imgui.radio_button("Marie", self.radio_selected==2):
		    self.radio_selected = 2
		elif imgui.radio_button("Skyler", self.radio_selected==3):
		    self.radio_selected = 3
	
	def sceen_menu(self):
		imgui.text("menu akar lenni")
		imgui.image(self.plot_text[0], self.plot_text[1], self.plot_text[2])

	def sceen_test(self):
		if imgui.button("button"):
			print("megnyomtal")
		float_val = 0.4
		changed, float_val = imgui.input_float('Type coefficient:', float_val)
		#e=1,1
		#_,e=imgui.input_int2("sad",*e)
		imgui.text('You wrote: %f' % float_val)
		int_val = 3
		changed, int_val = imgui.input_int('Type multiplier:', int_val)
		imgui.text('You wrote: %i' % int_val)
		text_val = 'Please, type the coefficient here.'
		changed, text_val = imgui.input_text(
		    'Amount:',
		    text_val,
		    256
		)
		imgui.text('You wrote:')
		imgui.same_line()
		imgui.text(text_val)

		imgui.separator()

		for k,v in self.data.__dict__.items():
			if type(v) is int:
				imgui.text("Give me int")
				changed, int_val = imgui.input_int(k, int_val)
			if type(v) is float:
				imgui.text("Give me float")
				changed, float_val = imgui.input_float(k, float_val)
			if type(v) is str:
				imgui.text("Give me string")
				changed, text_val = imgui.input_text(k,text_val,256)

		if imgui.button("ok"):
			self.data.asd=100

	def set_style(self):
		pass
		#rgb(232, 249, 253) 0.9098039215686274, 0.9764705882352941, 0.9921568627450981
		#rgb(121, 218, 232) 0.4745098039215686, 0.8549019607843137, 0.9098039215686274
		#rgb(10, 161, 221)  0.4745098039215686, 0.8549019607843137, 0.9098039215686274
		#rgb(33, 85, 205) 0.12941176470588237, 0.3333333333333333, 0.803921568627451
		imgui.push_style_color(imgui.COLOR_TEXT, 0, 0.0, 0.0)
		imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, 0.4745098039215686, 0.8549019607843137, 0.9098039215686274)
		imgui.push_style_color(imgui.COLOR_MENUBAR_BACKGROUND , 0.12941176470588237, 0.3333333333333333, 0.803921568627451)
		imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND , 0.9098039215686274, 0.9764705882352941, 0.9921568627450981)
		imgui.push_style_color(imgui.COLOR_BUTTON, 0.12941176470588237, 0.3333333333333333, 0.803921568627451)
		imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED,0.4745098039215686, 0.8549019607843137, 0.9098039215686274)
	def pop_style(self):
		pass
		imgui.pop_style_color(6)







if __name__ == "__main__":
	tw= App_window()
	tw.start_loop()
	tw.terminate()
	cv.destroyAllWindows()

	
		
