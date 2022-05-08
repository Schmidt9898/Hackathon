class Question():
	def __init__(self):
		self.label = ""
		self.value = ""
		self.tooltip = 'lambda : ""' # ??
		self.isdone = False # ??
		self.combochoices = []
		self.state = 0 # ??
		self.resultID = 'lambda : None'
		self.ischeckbox = False # Only with combi choices
		self.target = '' # Target attribute set to value TODO ignored for checkboxes
		self.min = 0
		self.max = 0
		self.boomer = 1

class BasicInfo():
	def __init__(self):
		self.uname = ''
		self.advanced = 0
		self.gender = 0
		self.age = 18
		self.height = 180.0
		self.weight = 80.0
		self.history = [False, False, False]
		self.alcohol = 0
		self.smoking = 0
		self.diabetic = 0
		self.bloodsugar = 4.5
		self.bloodpressure = (100.0, 60,0)
		self.checkup = 0
		self.symptoms = [False, False, False, False, False, False, False]

def get_questions():
    questions = []

    SN = Question()
    SN.label = "Name"
    SN.value = ""
    SN.tooltip = 'lambda : "hm"'
    SN.resultID = 'lambda : ""'
    SN.target = 'uname'
    questions.append(SN)

    SO = Question()
    SO.label = "Gender"
    SO.value = 0
    SO.tooltip = 'lambda : "hm"'
    SO.combochoices = ["Male", "Female"]
    SO.resultID = 'lambda : ""'
    SO.target = 'gender'
    questions.append(SO)

    SP = Question()
    SP.label = "Age"
    SP.value = 18
    SP.tooltip = 'lambda : "hm"'
    SP.resultID = 'lambda : ""'
    SP.target = 'age'
    SP.min = 18
    SP.max = 99
    questions.append(SP)

    SA = Question()
    SA.label = "Advanced mode"
    SA.value = 0
    SA.tooltip = 'lambda : "hm"'
    SA.combochoices = ["Disabled", "Enabled"]
    SA.resultID = 'lambda : ""'
    SA.target = 'advanced'
    questions.append(SA)

    S0 = Question()
    S0.label = "Height (cm)"
    S0.value = 180
    S0.tooltip = 'lambda : "hm"'
    S0.resultID = 'lambda : ""'
    S0.target = 'height'
    S0.min = 100
    S0.max = 300
    questions.append(S0)

    S1 = Question()
    S1.label = "Weight (kg)"
    S1.value = 80
    S1.tooltip = 'lambda input, height: "Your BMI suggests you should increase your caloric intake" if input/(height)^2 < 18.5 else "Your BMI is optimal, keep it up!" if input/(height)^2 >= 18.5 and input/(height)^2 < 25.0 else "Your BMI is slightly above optimal" if input/(height)^2 >= 25.0 and input/(height)^2 < 30.0 else "Your BMI suggests an unhealthy lifestyle. You should work out more!" if input/(height)^2 >= 30.0 and input/(height)^2 < 40 else "You should start working on decreasing your weight as soon as possible!" if input/(height)^2 >= 40 else ""'
    S1.isdone = 'lambda input: True if input else False' # S1.value-t nézze
    S1.iscombo = True
    S1.combochoices = []
    S1.state = 1
    S1.resultID = 'lambda input, height: 0 if input/(height)^2 < 18.5 else 1 if input/(height)^2 >= 18.5 and input/(height)^2 < 25.0 else 2 if input/(height)^2 >= 25.0 and input/(height)^2 < 30.0 else 3 if input/(height)^2 >= 30.0 and input/(height)^2 < 40 else 5 if input/(height)^2 >= 40 else ""'
    S1.target = 'weight'
    S1.min = 40
    S1.max = 200
    questions.append(S1)

    S2 = Question()
    S2.label = "Have you or any of your family members had any of these cancers in the past?"
    S2.value = [False, False, False, False]
    S2.tooltip = 'lambda input: "Be sure to have a medical checkup frequently!" if input != "None" else "Good to hear!"'
    S2.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S2.value-t nézze
    S2.iscombo = True
    S2.ischeckbox = True
    S2.combochoices = ["Breast", "Melanoma", "Lung"]
    S2.state = 2
    S2.resultID = 'lambda input: 33 if input == "Breast" else 34 if input == "Melanoma" else 35 if input == "Lung" else -1'
    S2.target = 'history'
    questions.append(S2)

    S3 = Question()
    S3.label = "How often do you consume alcohol?"
    S3.value = 0
    S3.tooltip = 'lambda input: "You are doing very well! Keep it up!" if input == "None" else "Even low consumption modestly increases the risk of cancer. Watch your intake!" if input == "Once per day or less" else "Alcohol consumption increases the risk of melanoma and prostate cancer in men. Try lowering your alcohol intake!" if input == "Regular or heavier consumer" else ""'
    S3.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S3.value-t nézze
    S3.iscombo = True
    S3.combochoices = ["None ", "Once per day or less", "Regular or heavier consumer"]
    S3.state = 3
    S3.resultID = 'lambda input: 7 if input == "None" else 8 if input == "Once per day or less" else 9 if input == "Regular or heavier consumer" else ""'
    S3.target = 'alcohol'
    questions.append(S3)

    S4 = Question()
    S4.label = "How would you describe yourself in terms of smoking habits?"
    S4.value = 0
    S4.tooltip = 'lambda input: "Good job! You are striving towards a healthy lifestyle!" if input == "Does not smoke" else "Even low intensity smoking significantly increases cancer risk! You should consider abandoning smoking!" if input == "Active smoker" else "Try avoiding smoking people and crowds! You are at risk as well!" if input == "Passive smoker" else ""'
    S4.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S4.value-t nézze
    S4.iscombo = True
    S4.combochoices = ["Does not smoke", "Passive smoker", "Active smoker"]
    S4.state = 4
    S4.resultID = 'lambda input: 12 if input == "Does not smoke" else 11 if input == "Active smoker" else 10 if input == "Passive smoker" else ""'
    S4.target = 'smoking'
    questions.append(S4)

    S5a = Question()
    S5a.label = "Are you diabetic?"
    S5a.value = 0
    S5a.tooltip = 'lambda : "hm"'
    S5a.combochoices = ["No", "Yes"]
    S5a.resultID = 'lambda : ""'
    S5a.target = 'diabetic'
    questions.append(S5a)

    S5 = Question()
    S5.label = "Blood sugar (mmol/L)"
    S5.value = 4.5
    S5.tooltip = 'lambda input: "Your blood sugar levels are within acceptable parameters" if input >= 4.4 and input <= 6.1 else "Both low and high blood sugar levels may indicate different types of cancer. If your levels are frequently outside optimal ranges, consult with a healthcare professional!" '
    S5.isdone = 'lambda input: False if input else True' # S5.value-t nézze
    S5.iscombo = False
    S5.combochoices = []
    S5.state = 5
    S5.resultID = 'lambda input, diabeticinput: 13 if input >= 4.4 and input <= 6.1 and diabeticinput==37 else 14 if input >= 5.0 and input <= 7.2 and diabeticinput==36 else 15'
    S5.target = 'bloodsugar'
    S5.min = 2.0
    S5.max = 10.0
    S5.boomer = 0
    questions.append(S5)

    S6 = Question()
    S6.label = "Blood pressure (mmHg)"
    S6.value = (100, 60)
    S6.tooltip = 'lambda input: "Your blood pressure values are well within healthy range" if input[0] < 120 and input[1] < 80 else "Your blood pressure is slightly above optimal range" if 120 <= input[0] < 130 and input[1] < 80 else "You are suffering from stage one hypertension. Hypertension is associated with elevated risks of cancer!" if 130 <= input[0] < 140 or 80 <= input[1] < 90 else "You are suffering from stage two hypertension! Hypertension is associated with elevated risks of cancer!" if input[0] >= 140 or input[1] >= 90 else ""'
    S6.isdone = 'lambda input: False if input == (-1, -1) else True' # S6.value-t nézze
    S6.iscombo = False
    S6.combochoices = []
    S6.state = 6
    S6.resultID = 'lambda input: 16 if input[0] < 120 and input[1] < 80 else 17 if 120 <= input[0] < 130 and input[1] < 80 else 18 if 130 <= input[0] < 140 or 80 <= input[1] < 90 else 19 if input[0] >= 140 or input[1] >= 90 else ""'
    S6.target = 'bloodpressure'
    S6.min = 0
    S6.max = 200
    S6.boomer = 0
    questions.append(S6)

    S7 = Question()
    S7.label = "How many months ago did you have your last checkup?"
    S7.value = 0
    S7.tooltip = 'lambda input: "You should plan for your next medical checkup" if input > 12 else ""'
    S7.isdone = 'lambda input: False if input == -1 else True' # S7.value-t nézze
    S7.iscombo = False
    S7.combochoices = []
    S7.state = 7
    S7.resultID = 'lambda input 38 if input > 12 else 39'
    S7.target = 'checkup'
    S7.min = 0
    S7.max = 300
    S7.boomer = 0
    questions.append(S7)

    S8 = Question()
    S8.label = "Have you had any of these symptomps lately?"
    S8.value = [False, False, False, False, False, False, False]
    S8.tooltip = 'lambda : ""'
    S8.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S8.value-t nézze
    S8.iscombo = True
    S8.combochoices = ["Sudden weight loss", "Swelling, visible lumps", "Thickening of skin", "Persisting cough", "Coughing up blood", "Unusual bleeding", "Increased fatigue, even with a proper sleeping schedule"]
    S8.state = 8
    S8.ischeckbox = True
    S8.resultID = 'lambda input: 26 if input == "Sudden weight loss" else 27 if input == "Swelling, visible lumps" else 28 if input == "Thickening of skin" else 29 if input == "Persisting cough" else 30 if input == "Coughing up blood" else 31 if input == "Unusual bleeding" else 32 if input == "Increased fatigue, even with a proper sleeping schedule" else ""'
    S8.target = 'symptoms'
    questions.append(S8)

    return questions

#   #from Json import*
#   #toJSON(questions,"questions.json")
#   #questions=[]
#   #questions=fromJSON("questions.json",Question)
#
#
#
#   q = [x.resultID(x.value) for x in questions]
#   results = [False]*39
#
#   for i in range(len(q)):
#      print(q[i])
#      #results[int(q[i])] = True

