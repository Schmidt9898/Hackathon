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
    contents = jsons.dumps(src)
    fl = open(fname, mode)
    if mode != "r":
        fl.write(contents)
    fl.close()

if __name__ == "__main__":
    t = JSONTest()
    toJSON(t, 'test.json')
    fl = open('test.json', 'r')
    print(json.load(fl))

