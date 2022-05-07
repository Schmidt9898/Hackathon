class Question():
    def __init__(self):
        self.label = ""
        self.value = ""
        self.tooltip = 'pass'
        self.isdone = ""
        self.iscombo = ""
        self.combochoices = ""
        self.state = ""
        self.resultID = 'pass'



if __name__ == "__main__":

    questions = []

    S1 = Question()

    S1.label = "Weight (kg)"
    S1.value = 0
    S1.tooltip = 'lambda input, height: "Your BMI suggests you should increase your caloric intake" if input/(height)^2 < 18.5 else "Your BMI is optimal, keep it up!" if input/(height)^2 >= 18.5 and input/(height)^2 < 25.0 else "Your BMI is slightly above optimal" if input/(height)^2 >= 25.0 and input/(height)^2 < 30.0 else "Your BMI suggests an unhealthy lifestyle. You should work out more!" if input/(height)^2 >= 30.0 and input/(height)^2 < 40 else "You should start working on decreasing your weight as soon as possible!" if input/(height)^2 >= 40 else ""'
    S1.isdone = 'lambda input: True if input else False' # S1.value-t nézze
    S1.iscombo = False
    S1.combochoices = []
    S1.state = 1
    S1.resultID = 'lambda input, height: 0 if input/(height)^2 < 18.5 else 1 if input/(height)^2 >= 18.5 and input/(height)^2 < 25.0 else 2 if input/(height)^2 >= 25.0 and input/(height)^2 < 30.0 else 3 if input/(height)^2 >= 30.0 and input/(height)^2 < 40 else 5 if input/(height)^2 >= 40 else ""'

    questions.append(S1)

    S2 = Question()

    S2.label = "Have you or any of your family members had any of these cancers in the past?"
    S2.value = None
    S2.tooltip = 'lambda input: "Be sure to have a medical checkup frequently!" if input != "None" else "Good to hear!"'
    S2.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S2.value-t nézze
    S2.iscombo = True
    S2.combochoices = ["Select an item from the list", "None", "Breast", "Melanoma", "Lung"]
    S2.state = 2
    S2.resultID = 'lambda input: 33 if input == "Breast" else 34 if input == "Melanoma" else 35 if input == "Lung" else -1'

    questions.append(S2)

    S3 = Question()

    S3.label = "How often do you consume alcohol?"
    S3.value = None
    S3.tooltip = 'lambda input: "You are doing very well! Keep it up!" if input == "None" else "Even low consumption modestly increases the risk of cancer. Watch your intake!" if input == "Once per day or less" else "Alcohol consumption increases the risk of melanoma and prostate cancer in men. Try lowering your alcohol intake!" if input == "Regular or heavier consumer" else ""'
    S3.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S3.value-t nézze
    S3.iscombo = True
    S3.combochoices = ["Select an item from the list", "None", "Once per day or less", "Regular or heavier consumer"]
    S3.state = 3
    S3.resultID = 'lambda input: 7 if input == "None" else 8 if input == "Once per day or less" else 9 if input == "Regular or heavier consumer" else ""'

    questions.append(S3)

    S4 = Question()

    S4.label = "How would you describe yourself in terms of smoking habits?"
    S4.value = None
    S4.tooltip = 'lambda input: "Good job! You are striving towards a healthy lifestyle!" if input == "Does not smoke" else "Even low intensity smoking significantly increases cancer risk! You should consider abandoning smoking!" if input == "Active smoker" else "Try avoiding smoking people and crowds! You are at risk as well!" if input == "Passive smoker" else ""'
    S4.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S4.value-t nézze
    S4.iscombo = True
    S4.combochoices = ["Select an item from the list", "Does not smoke", "Passive smoker", "Active smoker"]
    S4.state = 4
    S4.resultID = 'lambda input: 12 if input == "Does not smoke" else 11 if input == "Active smoker" else 10 if input == "Passive smoker" else ""'

    questions.append(S4)

    preS5 = Question()

    preS5.label = "Are you a diabetic?"
    preS5.value = None
    preS5.tooltip = 'pass'
    preS5.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # preS5.value-t nézze
    preS5.iscombo = True
    preS5.combochoices = ["Select an item from the list", "Yes", "No"]
    preS5.state = -5
    preS5.resultID = 'lambda input: 36 if input == "Yes" else 37 if input == "No" else ""'

    questions.append(preS5)

    S5 = Question()

    S5.label = "Blood sugar (mmol/L)"
    S5.value = 0
    S5.tooltip = 'lambda input, diabeticinput: "Your blood sugar levels are within acceptable parameters" if input >= 4.4 and input <= 6.1 and diabeticinput==37 else "Your blood sugar levels are within acceptable parameters" if input >= 5.0 and input <= 7.2 and diabeticinput==36 else "Both low and high blood sugar levels may indicate different types of cancer. If your levels are frequently outside optimal ranges, consult with a healthcare professional!" '
    S5.isdone = 'lambda input: False if input else True' # S5.value-t nézze
    S5.iscombo = False
    S5.combochoices = []
    S5.state = 5
    S5.resultID = 'lambda input, diabeticinput: 13 if input >= 4.4 and input <= 6.1 and diabeticinput==37 else 14 if input >= 5.0 and input <= 7.2 and diabeticinput==36 else 15'

    questions.append(S5)

    S6 = Question()

    S6.label = "Blood pressure (mmHg)"
    S6.value = (-1, -1)
    S6.tooltip = 'lambda input: "Your blood pressure values are well within healthy range" if input[0] < 120 and input[1] < 80 else "Your blood pressure is slightly above optimal range" if 120 <= input[0] < 130 and input[1] < 80 else "You are suffering from stage one hypertension. Hypertension is associated with elevated risks of cancer!" if 130 <= input[0] < 140 or 80 <= input[1] < 90 else "You are suffering from stage two hypertension! Hypertension is associated with elevated risks of cancer!" if input[0] >= 140 or input[1] >= 90 else ""'
    S6.isdone = 'lambda input: False if input == (-1, -1) else True' # S6.value-t nézze
    S6.iscombo = False
    S6.combochoices = []
    S6.state = 6
    S6.resultID = 'lambda input: 16 if input[0] < 120 and input[1] < 80 else 17 if 120 <= input[0] < 130 and input[1] < 80 else 18 if 130 <= input[0] < 140 or 80 <= input[1] < 90 else 19 if input[0] >= 140 or input[1] >= 90 else ""'

    questions.append(S6)

    S7 = Question()

    S7.label = "How many months ago did you have your last checkup?"
    S7.value = -1
    S7.tooltip = 'lambda input, hadcancer: "You should plan for your next medical checkup" if (hadcancer==-1 and input > 12) or (hadcancer != -1 and input > 3) else ""'
    S7.isdone = 'lambda input: False if input == -1 else True' # S7.value-t nézze
    S7.iscombo = False
    S7.combochoices = []
    S7.state = 7
    S7.resultID = 'lambda input, hadcancer: 38 if (hadcancer==-1 and input > 12) or (hadcancer != -1 and input > 3) else 39'

    questions.append(S7)

    S8 = Question()

    S8.label = "Have you had any of these symptomps lately?"
    S8.value = None
    S8.tooltip = 'pass'
    S8.isdone = 'lambda input: True if input != "Select an item from the list" or not None else False' # S8.value-t nézze
    S8.iscombo = True
    S8.combochoices = ["Select an item from the list", "Sudden weight loss", "Swelling, visible lumps", "Thickening of skin", "Persisting cough", "Coughing up blood", "Unusual bleeding", "Increased fatigue, even with a proper sleeping schedule"]
    S8.state = 8
    S8.resultID = 'lambda input: 26 if input == "Sudden weight loss" else 27 if input == "Swelling, visible lumps" else 28 if input == "Thickening of skin" else 29 if input == "Persisting cough" else 30 if input == "Coughing up blood" else 31 if input == "Unusual bleeding" else 32 if input == "Increased fatigue, even with a proper sleeping schedule" else ""'

    questions.append(S8)

    from Json import*
    toJSON(questions,"questions.json")
    questions=[]
    questions=fromJSON("questions.json",Question)



    q = [x.resultID(x.value) for x in questions]
    results = [False]*39

    for i in range(len(q)):
        print(q[i])
        #results[int(q[i])] = True

