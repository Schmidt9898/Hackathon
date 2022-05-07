

class Data_obj():
	def __init__(self):
		self.int_val=1
		self.float_val=3.141516
		self.test_val="Burnout - Voltam aki voltam."
		self.test_val2="Burnout - Voltam aki voltam."


if __name__ == "__main__":
	d=Data_obj()
	for k,v in d.__dict__.items():
		print(k,type(v))
		if type(v) is int:
			setattr(d,k,2)
	#d=Data_obj()
	for k,v in d.__dict__.items():
		print(k,v)



class qa():
	def __init__(self):
		self.label="qa1"
		self.imput=3.141516
		self.multi=True
		self.choises=[]
		self.tooltip="Burnout - Voltam aki voltam."
		self.isdone=False