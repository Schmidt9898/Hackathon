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
        fl.write(contents)
    fl.close()

def fromJSON(fname):
    fl = open(fname, 'r')
    contents = json.load(fl)
    fl.close()
    return contents

if __name__ == "__main__":
    t = JSONTest()
    toJSON(t, 'test.json')
    print(fromJSON('test.json'))

