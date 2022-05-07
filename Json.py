# 
# data = {"src": self.id, "dest": dest,"msg":obj}
# json_dump = json.dumps(data)
# msg = json.loads(msg)
import json
import jsons

class JSONTest():
	egesz = 5
	lebego = 3.1
	szoveg = "proba"
	lista = ["1", 2, 3.0]
	hamis = False
	igaz = True

def toJSON(src, fname, mode='w'):
    contents = jsons.dumps(src, default=vars)
    fl = open(fname, mode)
    if mode != "r":
        fl.write(contents + '\n')
    fl.close()

# Soronként egy objektum/dictionary
def fromJSON(fname):
    objects = []
    fl = open(fname, 'r')
    for l in fl:
        content = json.loads(l)
        objects.append(content)
    fl.close()
    return objects

if __name__ == "__main__":
	t = JSONTest()
	toJSON(t, 'test.json', 'w')
	fl = open('test.json', 'r')
	print(json.load(fl))




import unittest
import os
class Test_get_coin_methods(unittest.TestCase):
	def test_json_write(self):
		obj=JSONTest()
		toJSON([obj], "test.json", "w")
		self.assertTrue(os.path.exists("test.json"))
	def test_json_read(self):
		obj=JSONTest()
		toJSON([obj], "test.json", "w")
		self.assertTrue(os.path.exists("test.json"))
		objs=fromJSON("test.json")
		for o2 in objs:
			for k,v in o2.__dict__.items():
				self.assertEqual(getattr(obj, k),v)
	

if __name__ == "__main__":
	unittest.main()





    t = JSONTest()
    print('Írás')
    toJSON(t, 'test.json', 'a')
    print('Olvasás')
    print(fromJSON('test.json'))

