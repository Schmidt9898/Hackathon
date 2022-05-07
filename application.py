from Gui import * 
import imgui
import matplotlib.pyplot as plt
import webbrowser

from Data_example import Data_obj # remove this

class App_window(Gui_Window):
	

	def __init__(self,w=640,h=480,title="Life is good, but can be better."):
		super(App_window, self).__init__(w,h,title)
		
		self.tabs=["test","a","b","c","d"]
		self.cur_tab=self.tabs[0] if len(self.tabs)>0 else None
		self.fps=0
		self.data=Data_obj()



		io = imgui.get_io()												 #font
		self.new_font = io.fonts.add_font_from_file_ttf("./DroidSans.ttf", 30,)
		self.impl.refresh_font_texture()


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
		
		


	def context(self):
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
		
		
		if self.cur_tab == "test":
			self.sceen_test()
		elif self.cur_tab == "a":
			self.sceen_menu()
		elif self.cur_tab == "b":
			self.sceen_url()
		elif self.cur_tab == "c":
			imgui.text("tab 3")
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

	def sceen_menu(self):
		imgui.text("menu akar lenni")
		imgui.image(self.plot_text[0], self.plot_text[1], self.plot_text[2])

	def sceen_test(self):
		imgui.button("button")
		float_val = 0.4
		changed, float_val = imgui.input_float('Type coefficient:', float_val)
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









if __name__ == "__main__":
	tw= App_window()
	tw.start_loop()
	tw.terminate()
	cv.destroyAllWindows()

	
		
