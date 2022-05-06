from Gui import * 
import imgui


class App_window(Gui_Window):
	

	def __init__(self,w=640,h=480,title="Life is good, but can be better."):
		super(App_window, self).__init__(w,h,title)
		

		self.tab=0 # 0 menu 1 etc

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
			for i in range(5):
				if imgui.menu_item('push'+str(i))[0]:
					print(i)
					self.tab=i
	

			#if imgui.begin_menu('File'):
			#	print(imgui.menu_item('Close'))
			#	imgui.end_menu()

			imgui.end_menu_bar()
		
		
		if self.tab == 0:
			self.sceen_menu()
		elif self.tab == 1:
			imgui.text("tab 1")
		elif self.tab == 2:
			imgui.text("tab 2")
		elif self.tab == 3:
			imgui.text("tab 3")
		elif self.tab == 4:
			imgui.text("tab 4")




		
		if imgui.button("nyomj meg",):
			print("most")
		imgui.end()

	def sceen_menu(self):
		imgui.text("menu akar lenni")




if __name__ == "__main__":
	tw= App_window()
	tw.start_loop()
	tw.terminate()
	cv.destroyAllWindows()

	
		