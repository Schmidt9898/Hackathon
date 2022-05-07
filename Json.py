import json
# jsons valószínűleg nem szükséges már, amúgy jsons.dumps működik bárhol
#import jsons
import unittest
import os

class JSONTest():
    def __init__(self, egesz=5, lebego=3.1, szoveg='foo', lista=['1', 2, 3.1], hamis=False, igaz=True):
        self.egesz = egesz
        self.lebego = lebego
        self.szoveg = szoveg
        self.lista = lista
        self.hamis = hamis
        self.igaz = igaz

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

# Soronként egy objektum/dictionary
def fromJSON(fname):
    objects = []
    fl = open(fname, 'r')
    for l in fl:
        content = json.loads(l)
        objects.append(content)
    fl.close()
    return objects

class Test_get_coin_methods(unittest.TestCase):
    def test_json_writesingle(self):
        obj = JSONTest()
        toJSON(obj, 'test.json', 'w')
        self.assertTrue(os.path.exists("test.json"))

    def test_json_writelist(self):
        obj = JSONTest()
        toJSON([obj], 'test.json', 'w')
        self.assertTrue(os.path.exists("test.json"))

    def test_json_readonce(self):
        obj = JSONTest()
        toJSON([obj, obj], 'test.json', 'w')
        self.assertTrue(os.path.exists("test.json"))
        result = fromJSON("test.json")
        for o in result:
            #for k,v in o.__dict__.items():
            for k,v in o.items():
                self.assertEqual(getattr(obj, k), v)

    def test_json_readappend(self):
        obj = JSONTest()
        fl = open('test.json', 'w')
        fl.close()
        toJSON(obj, 'test.json', 'a')
        self.assertTrue(os.path.exists("test.json"))
        toJSON([obj], 'test.json', 'a')
        self.assertTrue(os.path.exists("test.json"))
        toJSON([obj, obj], 'test.json', 'a')
        self.assertTrue(os.path.exists("test.json"))

        result = fromJSON("test.json")
        for o in result:
            #for k,v in o.__dict__.items():
            for k,v in o.items():
                self.assertEqual(getattr(obj, k), v)

    def test_json_readmultiple(self):
        obj1 = JSONTest()
        obj2 = JSONTest(4, 2.2, 'bar', ['n', 4, 5.6], True, False)
        toJSON([obj1, obj2], 'test.json', 'w')
        self.assertTrue(os.path.exists("test.json"))

        result = fromJSON("test.json")
        self.assertEqual(len(result), 2)
        for k,v in result[0].items():
            self.assertEqual(getattr(obj1, k), v)
        for k,v in result[1].items():
            self.assertEqual(getattr(obj2, k), v)

# Tesztelés
if __name__ == "__main__":
    unittest.main()

