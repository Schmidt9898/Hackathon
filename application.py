import time
from Gui import * 
import imgui
import matplotlib.pyplot as plt
from Animated import *
import webbrowser
import questions

from Data_example import Data_obj # remove this

class App_window(Gui_Window):
	

	def __init__(self,w=640,h=480,title="Life is good, but can be better."):
		super(App_window, self).__init__(w,h,title)
		
		self.tabs=["qa","plot","progresbar","radioweb","anim","Main menu","eval","furtherinfo"]
		#self.cur_tab=self.tabs[0] if len(self.tabs)>0 else None
		self.cur_tab="Main menu"
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
		self.nc=0.05
		# Radio test
		self.radio_selected = 0
		# User's name
		self.username = ''
		if os.path.exists('username.txt'):
			f = open('username.txt')
			l = f.readline()
			if l.split():
				self.username = l[0:-1]
			f.close()


		self.questions=questions.get_questions()
		self.bi = questions.BasicInfo()
		self.resultID = [False]*40;
		self.evalonce = True

	def context(self):
		self.fps+=1
		if self.fps_time<time.time():
			print(self.fps)
			self.fps_time=time.time()+1
			self.fps=0.0
		if self.cur_tab != "eval":
			self.evalonce = True


		imgui.push_font(self.new_font)
		io = imgui.get_io()
		#print(io.display_size.x)
		w_flags= imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_MENU_BAR | imgui.WINDOW_NO_BRING_TO_FRONT_ON_FOCUS
		
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
		
		
		if self.cur_tab == "qa":
			self.sceen_qa()
		elif self.cur_tab == "plot":
			self.sceen_menu()
		elif self.cur_tab == "progresbar":
			showProgresbar(self.n,1000)
			showProgresbar(self.n,1000)
			showProgresbar(self.n,1000)
			imgui.text("adsdasd")
			showProgresbar(self.n,1000)
		elif self.cur_tab == "radioweb":
			self.sceen_radio()
			self.sceen_url()
		elif self.cur_tab == "anim":
			self.anim.draw(self.n)
			#imgui.text("anim")

		elif self.cur_tab == "d":
			imgui.text("tab d")
		elif self.cur_tab == "Main menu":
			self.screen_main()
		elif self.cur_tab == "eval":
			self.updateResultID()
			self.evalonce = False
			self.screen_eval()
		elif self.cur_tab == "furtherinfo":
			self.screen_furtherinfo()



		
		#if imgui.button("nyomj meg",):
		#	print("most")
		imgui.end()


		self.n+=self.nc
		if self.n > 1 or self.n<0:
			self.nc*=-1
		imgui.set_next_window_position(io.display_size.x,40,pivot_x=1,pivot_y=0)
		imgui.set_next_window_size(200,200)
		imgui.begin("anim",flags=imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_SCROLLBAR | imgui.WINDOW_NO_SCROLL_WITH_MOUSE )
		self.anim.draw(self.n)
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

	def sceen_qa(self):
		for q in self.questions:
			imgui.text(q.label)
			if len(q.combochoices):
				#clicked, current = imgui.combo(q.label, q.value if q.value != None else 0, q.combochoices)
				#if clicked:
				#	q.value=current
				i = 0
				for c in q.combochoices:
					if not q.ischeckbox:
						if imgui.radio_button(c, q.value == i):
							q.value = i
							setattr(self.bi, q.target, q.value)
					else:
						_, q.value[i] = imgui.checkbox(c, q.value[i])
						# TODO
						if q.target == 'symptoms':
							self.bi.symptoms[i] = q.value[i]
						elif q.target == 'history':
							self.bi.history[i] = q.value[i]
					i += 1
			elif type(q.value) is int:
				#imgui.text("Give me int")
				changed, int_val = imgui.input_int(q.label, q.value,flags=0)
				if q.value < q.min:
					q.value = q.min
					int_val = q.min
				elif q.value > q.max:
					q.value = q.max
					int_val = q.max
				else:
					q.value = int_val
				setattr(self.bi, q.target, q.value)
			elif type(q.value) is float:
				#imgui.text("Give me float")
				changed, float_val = imgui.input_float(q.label, q.value)
				if q.value < q.min:
					q.value = q.min
					float_val = q.min
				elif q.value > q.max:
					q.value = q.max
					float_val = q.max
				else:
					q.value = float_val
				setattr(self.bi, q.target, q.value)
			elif type(q.value) is str:
				#imgui.text("Give me string")
				changed, text_val = imgui.input_text(q.label,q.value,256)
				if changed:
					q.value=text_val
			elif type(q.value) is tuple:
				# TODO hogy lehet ezt min-maxolni?
				val=val1,val2=q.value
				changed, val = imgui.input_float2(q.label, *val)
				if changed:
					q.value=(val)
				setattr(self.bi, q.target, q.value)
			imgui.separator()

#		for k,v in self.data.__dict__.items():
#			if type(v) is int:
#				imgui.text("Give me int")
#				changed, int_val = imgui.input_int(k, int_val)
#			if type(v) is float:
#				imgui.text("Give me float")
#				changed, float_val = imgui.input_float(k, float_val)
#			if type(v) is str:
#				imgui.text("Give me string")
#				changed, text_val = imgui.input_text(k,text_val,256)
#
#		if imgui.button("ok"):
#			self.data.asd=100

	def screen_main(self):
		imgui.columns(3, border=False)
		imgui.set_column_width(0, imgui.get_window_width() * 0.20)
		imgui.set_column_width(1, imgui.get_window_width() * 0.60)
		imgui.set_column_width(2, imgui.get_window_width() * 0.20)
		imgui.next_column()
		imgui.text(' '*(int(24*imgui.get_window_width()/640-len(self.username)*1.5)) + 'Welcome ' + self.username + '!')
		imgui.text('')
		imgui.button('Start questionnaire', imgui.get_window_width() * 0.60, 75)
		imgui.text('')
		imgui.button('Change basic info', imgui.get_window_width() * 0.60, 50)
		imgui.text('')
		if imgui.button('Quit application', imgui.get_window_width() * 0.60, 50):
			quit()
		imgui.next_column()
	
	
	def updateResultID(self):
		if self.evalonce:
			self.resultID[0] = self.bi.weight/(self.bi.height*self.bi.height)*10000 <= 18.5
			self.resultID[1] = (self.bi.weight/(self.bi.height*self.bi.height)*10000 > 18.5) and (self.bi.weight/(self.bi.height*self.bi.height)*10000 <= 24.9)
			self.resultID[2] = (self.bi.weight/(self.bi.height*self.bi.height)*10000 > 24.9) and (self.bi.weight/(self.bi.height*self.bi.height)*10000 <= 29.9)
			self.resultID[3] = (self.bi.weight/(self.bi.height*self.bi.height)*10000 > 29.9) and (self.bi.weight/(self.bi.height*self.bi.height)*10000 <= 34.9)
			self.resultID[4] = (self.bi.weight/(self.bi.height*self.bi.height)*10000 > 34.9) and (self.bi.weight/(self.bi.height*self.bi.height)*10000 <= 39.9)
			self.resultID[5] = self.bi.weight/(self.bi.height*self.bi.height)*10000 > 39.9
			self.resultID[6] = True in self.bi.history
			self.resultID[7] = self.bi.alcohol == 0
			self.resultID[8] = self.bi.alcohol == 1
			self.resultID[9] = self.bi.alcohol == 2
			self.resultID[10] = self.bi.smoking == 0
			self.resultID[11] = self.bi.smoking == 1
			self.resultID[12] = self.bi.smoking == 2
			self.resultID[13] = (self.bi.diabetic == 0) and (self.bi.bloodsugar >= 4.4) and (self.bi.bloodsugar <= 6.1)
			self.resultID[14] = (self.bi.diabetic == 1) and (self.bi.bloodsugar >= 5.0) and (self.bi.bloodsugar <= 7.2)
			self.resultID[15] = not self.resultID[13] and not self.resultID[14]
			self.resultID[21] = False
			self.resultID[22] = False
			self.resultID[23] = (self.bi.age >= 50) and (self.bi.checkup >= 12)
			self.resultID[24] = (self.bi.age < 50) and (self.bi.checkup >= 36)
			self.resultID[25] = (True in self.bi.history) and (self.bi.checkup >= 12)
			self.resultID[26] = self.bi.symptoms[0]
			self.resultID[27] = self.bi.symptoms[1]
			self.resultID[28] = self.bi.symptoms[2]
			self.resultID[29] = self.bi.symptoms[3]
			self.resultID[30] = self.bi.symptoms[4]
			self.resultID[31] = self.bi.symptoms[5]
			self.resultID[32] = self.bi.symptoms[6]
			self.resultID[33] = self.bi.history[0]
			self.resultID[34] = self.bi.history[1]
			self.resultID[35] = self.bi.history[2]
			self.resultID[36] = self.bi.diabetic == 0
			self.resultID[37] = self.bi.diabetic == 1
			self.resultID[38] = self.resultID[21] or self.resultID[22] or self.resultID[23] or self.resultID[24] or self.resultID[25]
			self.resultID[39] = not self.resultID[39]
			for i in vars(self.bi):
				print("'"+i+"': " + str(getattr(self.bi, i)))
			for i in range(len(self.resultID)):
				print(str(i)+": " + str(self.resultID[i]))
	
	def screen_eval(self):
		imgui.text('For general guidelines on cancer prevention, see this website.')
		if imgui.button('cancer.org'):
			webbrowser.open('https://www.cancer.org/healthy/find-cancer-early/screening-recommendations-by-age.html')

		# Fatigue
		if self.resultID[26] or self.resultID[32]:
			imgui.text('\nOne of your symptoms (fatigue) may be reason for concern.')
			imgui.text('Make an appointment with a doctor as soon as possible.')
			if imgui.button('maps.google.com'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

		# Bleeding
		if self.resultID[30] or self.resultID[31]:
			imgui.text('\nOne of your symptoms (bleeding) is cause for major concern.')
			imgui.text('Make an appointment with a doctor immediately!')
			if imgui.button('maps.google.com##'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

		# Skin disease
		if self.resultID[27] or self.resultID[28]:
			imgui.text('\nOne of your symptoms (skin disease) indicates the possibility of melanoma.')
			imgui.text('Make an appointment with a doctor as soon as possible.')
			if imgui.button('maps.google.com##1'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

		# Cough
		if self.resultID[29]:
			imgui.text('\nA persisting cough may be cause for concern.')
			imgui.text('If you find it unusual, make an appointment with a doctor.')
			if imgui.button('maps.google.com##2'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

		if self.resultID[0]:
			imgui.text('\nYou should consider putting on some weight! Check out this website for advice.')
			if imgui.button('nhs.uk'):
				webbrowser.open('https://www.nhs.uk/live-well/healthy-weight/managing-your-weight/advice-for-underweight-adults/')

		if self.resultID[2]:
			imgui.text('\nYour weight is above optimal. Check out this website for advice.')
			if imgui.button('nhs.uk##'):
				webbrowser.open('https://www.nhs.uk/conditions/obesity/treatment/')

		if self.resultID[3] or self.resultID[4] or self.resultID[5]:
			imgui.text('\nYou are considered obese. You should start working on dropping some pounds!')
			imgui.text('Check out this website for advice.')
			if imgui.button('nhs.uk##1'):
				webbrowser.open('https://www.nhs.uk/conditions/obesity/treatment/')

		if self.resultID[8]:
			imgui.text('\nModerate consumption of alcohol is linked with increased cancer risk.')
			imgui.text('See this site for further information.')
			if imgui.button('cancer.gov##'):
				webbrowser.open('https://www.cancer.gov/about-cancer/causes-prevention/risk/alcohol/alcohol-fact-sheet')

		if self.resultID[9]:
			imgui.text('\nModerate consumption of alcohol is linked with increased cancer risk.')
			imgui.text('See this site for further information.')
			if imgui.button('cancer.gov##1'):
				webbrowser.open('https://www.cancer.gov/about-cancer/causes-prevention/risk/alcohol/alcohol-fact-sheet')
			imgui.text('Additionally, if you feel like you need help regarding alcohol, visit this site.')
			if imgui.button('nhs.uk##2'):
				webbrowser.open('https://www.nhs.uk/conditions/alcohol-misuse/treatment/')

		if self.resultID[11]:
			imgui.text('\nEven low intensity smoking is associated with increased cancer risk.')
			imgui.text('See this website.')
			if imgui.button('nhs.uk##3'):
				webbrowser.open('https://www.nhs.uk/conditions/lung-cancer/causes/')
			imgui.text('If you need help to quit smoking, here is another website.')
			if imgui.button('nhs.uk##4'):
				webbrowser.open('https://www.nhs.uk/better-health/quit-smoking/')

		if self.resultID[11] and self.resultID[35]:
			imgui.text('\nEven low intensity smoking is associated with increased cancer risk.')
			imgui.text('See this website.')
			if imgui.button('nhs.uk##5'):
				webbrowser.open('https://www.nhs.uk/conditions/lung-cancer/causes/')
			imgui.text('If you need help to quit smoking, here is another website.')
			if imgui.button('nhs.uk##6'):
				webbrowser.open('https://www.nhs.uk/better-health/quit-smoking/')
			imgui.text('Beware! According to your or your family\'s medical history,')
			imgui.text('you are at an increased risk of lung cancer. Smoking does not help!')

		if self.resultID[15]:
			imgui.text('\nYour blood sugar levels are outside optimal parameters.')
			imgui.text('If this has been going on for a while, make an appointment with a doctor.')
			if imgui.button('maps.google.com##3'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

		if self.resultID[17]:
			imgui.text('\nYour blood pressure is slightly above optimal.')
			imgui.text('Consider taking steps to reduce it. Here\'s some advice. ')
			if imgui.button('nhs.uk##7'):
				webbrowser.open('https://www.nhs.uk/conditions/high-blood-pressure-hypertension/prevention/')

		if self.resultID[18] or self.resultID[19]:
			imgui.text('\nYour blood pressure indicates hypertension.')
			imgui.text('You should take steps to reduce it. Here\'s some advice.')
			if imgui.button('nhs.uk##8'):
				webbrowser.open('https://www.nhs.uk/conditions/high-blood-pressure-hypertension/prevention/')

		if self.resultID[38]:
			imgui.text('\nYou should make an appointment with a doctor for a regular medical checkup.')
			imgui.text('See this link for doctors nearby.')
			if imgui.button('maps.google.com##4'):
				webbrowser.open('https://www.google.com/maps/search/doctor/')

	def screen_furtherinfo(self):
		imgui.text('Did you know?\n')
		imgui.text('\n\"Low contents of omega-3 PUFAs in the mammary region')
		imgui.text('seem to contribute to breast cancer multifocality,')
		imgui.text('indicating that omega-3 PUFA supplementation')
		imgui.text('is important for cancer management and prevention\"')
		if imgui.button('PubMed'):
			webbrowser.open('https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6566772/')

		imgui.text('\nLow lean body mass acts as a poor')
		imgui.text('prognostic factor for cancer patients, regardless of age')
		if imgui.button('PubMed##1'):
			webbrowser.open('https://pubmed.ncbi.nlm.nih.gov/22898746/')

	def set_style(self):
		pass
		#rgb(232, 249, 253) 0.9098	, 0.9764	, 0.9921	
		#rgb(121, 218, 232) 0.4745	, 0.8549	, 0.9098	
		#rgb(10, 161, 221)  0.4745	, 0.8549	, 0.9098	
		#rgb(10, 180, 221)  0.0392,   0.7058, 	  0.8666	
		#rgb(33, 85, 205) 	0.1294	, 0.3333	, 0.8039	

		#rgb(73, 83, 113)	0.2862755, 0.325494, 0.44313
		#rgb(116, 149, 154)	0.454907, 0.584311, 0.60392
		#rgb(152, 180, 170)	0.59607, 0.705885, 0.666666
		#rgb(241, 224, 172)	0.945092, 0.878436, 0.674507



		imgui.push_style_var(imgui.STYLE_FRAME_ROUNDING, 10)
		imgui.push_style_color(imgui.COLOR_TEXT, 0, 0.0, 0.0)
		imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, 	0.4745	, 0.8549	, 0.9098)
		imgui.push_style_color(imgui.COLOR_MENUBAR_BACKGROUND ,	0.1294	, 0.3333	, 0.8039)
		imgui.push_style_color(imgui.COLOR_FRAME_BACKGROUND ,	0.9098	, 0.9764	, 0.9921)
		imgui.push_style_color(imgui.COLOR_BUTTON,				0.1294	, 0.3333	, 0.8039)
		imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED,		0.0392,   0.7058, 	  0.8666)
	def pop_style(self):
		pass
		imgui.pop_style_color(6)
		imgui.pop_style_var(1)








if __name__ == "__main__":
	tw= App_window()
	tw.start_loop()
	tw.terminate()
	cv.destroyAllWindows()

	
		
