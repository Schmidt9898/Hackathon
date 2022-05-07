from Gui import * 
import imgui

from Data_example import Data_obj # remove this

class App_window(Gui_Window):
	

	def __init__(self,w=640,h=480,title="Life is good, but can be better."):
		super(App_window, self).__init__(w,h,title)
		
		self.tabs=["test","a","b","c","d"]
		self.cur_tab=self.tabs[0] if len(self.tabs)>0 else None
		self.fps=0
		self.data=Data_obj()


	def context(self):
		
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
			imgui.text("tab 2")
		elif self.cur_tab == "c":
			imgui.text("tab 3")
		elif self.cur_tab == "d":
			imgui.text("tab d")




		
		#if imgui.button("nyomj meg",):
		#	print("most")
		imgui.end()

	def sceen_menu(self):
		imgui.text("menu akar lenni")

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

	
		