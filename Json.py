import json
# jsons valószínűleg nem szükséges már, amúgy jsons.dumps működik bárhol
#import jsons
import unittest
import os

class JSONTest():
	def __init__(self, egesz=5, lebego=3.1, szoveg='foo', lista=['1', 2, 3.1], szotar={'a': 'c', 'b': 2, 'c': [3.0]}, hamis=False, igaz=True):
		self.egesz = egesz
		self.lebego = lebego
		self.szoveg = szoveg
		self.lista = lista
		self.szotar = szotar
		self.hamis = hamis
		self.igaz = igaz
		self.la = 'lambda a : a*10 + 1'
		self.mb = 'lambda a : a + 10'
	
	def da(self, n):
		if n % 2:
			return self.la(n)
		else:
			return self.mb(n)

# Bementeknek egy objektumokból álló listát vár
# Ezt majd soronként kiírja, minden elemet egy külön sorba rakva
def toJSON(src, fname, mode='w'):
	fl = open(fname, mode)
	if isinstance(src, list):
		content = ''
		for o in src:
			content += json.dumps(o, default=vars)+'\n'
	else:
		content = json.dumps(src, default=vars)+'\n'
	if mode != "r":
		fl.write(content)
	fl.close()

# Soronként egy objektum/dictionary lesz beolvasva egy listába
def fromJSON(fname):
	objects = []
	fl = open(fname, 'r')
	for l in fl:
		# TODO: üres sor kezelése
		content = json.loads(l)
		objects.append(content)
	fl.close()
	return objects

# Egy dictionary értékeit átmásolja egy objektumra.
def fromDict(target, d):
	if isinstance(d, dict):
		for k in d.keys():
			#if callable(d[k]):
			if isinstance(d[k], str) and d[k].startswith('lambda'):
				setattr(target, k, eval(d[k]))
			else:
				setattr(target, k, d[k])

def findLambdas(target):
	for v in vars(target):
		if isinstance(getattr(target, v), str) and getattr(target, v).startswith('lambda'):
			setattr(target, v, eval(getattr(target, v)))

class Test_get_coin_methods(unittest.TestCase):
	def test_json_writesingle(self):
		obj = JSONTest()
		toJSON(obj, 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_writelist(self):
		obj = JSONTest()
		toJSON([obj], 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_readonce(self):
		obj = JSONTest()
		toJSON([obj, obj], 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		result = fromJSON('test.json')
		for o in result:
			#for k,v in o.__dict__.items():
			for k,v in o.items():
				self.assertEqual(getattr(obj, k), v)

		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_readappend(self):
		obj = JSONTest()
		fl = open('test.json', 'w')
		fl.close()
		toJSON(obj, 'test.json', 'a')
		self.assertTrue(os.path.exists('test.json'))
		toJSON([obj], 'test.json', 'a')
		self.assertTrue(os.path.exists('test.json'))
		toJSON([obj, obj], 'test.json', 'a')
		self.assertTrue(os.path.exists('test.json'))

		result = fromJSON('test.json')
		for o in result:
			#for k,v in o.__dict__.items():
			for k,v in o.items():
				self.assertEqual(getattr(obj, k), v)
		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_readmultiple(self):
		obj1 = JSONTest()
		obj2 = JSONTest(4, 2.2, 'bar', ['n', 4, 5.6], {'1': 2, '2': 1, 'e': ['mc']}, True, False)
		toJSON([obj1, obj2], 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		result = fromJSON("test.json")
		self.assertEqual(len(result), 2)
		for k,v in result[0].items():
			self.assertEqual(getattr(obj1, k), v)
		for k,v in result[1].items():
			self.assertEqual(getattr(obj2, k), v)
		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_castobject(self):
		obj_old = JSONTest(4, 2.2, 'bar', ['n', 4, 5.6], {'1': 2, '2': 1, 'e': ['mc']}, True, False)
		toJSON(obj_old, 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		result = fromJSON('test.json')
		self.assertEqual(len(result), 1)
		obj_new = JSONTest()
		fromDict(obj_new, result[0])
		toJSON(obj_new, 'test.json', 'a')
		result = fromJSON('test.json')
		self.assertEqual(len(result), 2)

		for o in result:
			#for k,v in o.__dict__.items():
			for k,v in o.items():
				if k != 'la' and k != 'mb':
					self.assertEqual(getattr(obj_old, k), v)
					self.assertEqual(getattr(obj_new, k), v)
		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_readlambda(self):
		obj_old = JSONTest()
		toJSON(obj_old, 'test.json')
		self.assertTrue(os.path.exists('test.json'))

		result = fromJSON('test.json')
		self.assertEqual(len(result), 1)
		for k,v in result[0].items():
			self.assertEqual(getattr(obj_old, k), v)
		
		obj_new = JSONTest()
		findLambdas(obj_old)
		fromDict(obj_new, result[0])
		for i in range(5):
			if i == 0:
				self.assertEqual(obj_new.da(i), 10)
				self.assertEqual(obj_new.da(i), obj_old.da(i))
			if i == 1:
				self.assertEqual(obj_new.da(i), 11)
				self.assertEqual(obj_new.da(i), obj_old.da(i))
			if i == 2:
				self.assertEqual(obj_new.da(i), 12)
				self.assertEqual(obj_new.da(i), obj_old.da(i))
			if i == 3:
				self.assertEqual(obj_new.da(i), 31)
				self.assertEqual(obj_new.da(i), obj_old.da(i))
			if i == 4:
				self.assertEqual(obj_new.da(i), 14)
				self.assertEqual(obj_new.da(i), obj_old.da(i))

		os.remove('test.json')
		self.assertFalse(os.path.exists('test.json'))

	def test_json_readfile(self):
		result = fromJSON('test_cancer.json')
		self.assertEqual(len(result), 5)

		class CancerTest():
			def __init__(self):
				self.cname = ''
				self.lethality = 0.0
				self.occurance = 0.0
				self.men = False
				self.women = False
				self.fun = ''
			
			def urgency():
				return self.lethality * self.occurance

		for i in range(5):
			obj = CancerTest()
			fromDict(obj, result[i])
			if i == 0:
			    self.assertEqual(obj.cname, 'Tüdő')
			    self.assertEqual(obj.fun(), 0)
			if i == 1:
			    self.assertEqual(obj.lethality, 0.6)
			    self.assertEqual(obj.fun(), 1)
			if i == 2:
			    self.assertEqual(obj.occurance, 0.001)
			    self.assertEqual(obj.fun(), 2)
			if i == 3:
			    self.assertEqual(obj.men, True)
			    self.assertEqual(obj.fun(), 3)
			if i == 4:
			    self.assertEqual(obj.women, True)
			    self.assertEqual(obj.fun(), 4)

# Tesztelés
if __name__ == "__main__":
	unittest.main()

