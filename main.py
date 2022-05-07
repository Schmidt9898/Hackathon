

print("Start")


a= lambda n : str(n) if n<100 else "anyu" if n<150 else "asztarohadt"
if type(a) is str:
	a = eval(a)
print(a(10))
print(a(110))
print(a(160))


