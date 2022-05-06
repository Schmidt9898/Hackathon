from Gui import * 
import imgui


class App_window(Gui_Window):
	

	def context(self):
		
		io = imgui.get_io()
		#print(io.display_size.x)
		imgui.set_next_window_position(0,0)
		imgui.set_next_window_size(io.display_size.x,io.display_size.y)

		imgui.begin("asd")
		#s=imgui.getmainviewport()
		#imgui.setnextwindowpos(s)
		if imgui.button("nyomj meg",):
			print("most")
		imgui.end()



#ImGuiIO& io = ImGui::GetIO();
#//puts the child window in the main window and match size
#const ImGuiViewport* viewport = ImGui::GetMainViewport();
#float leftside_w = viewport->Size.x * 0.16f;
#ImGui::SetNextWindowPos(viewport->WorkPos);
#ImGui::SetNextWindowSize(viewport->WorkSize);




if __name__ == "__main__":
	tw= App_window()
	tw.start_loop()
	tw.terminate()
	cv.destroyAllWindows()

	
		