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
    print('Írás')
    toJSON(t, 'test.json', 'a')
    print('Olvasás')
    print(fromJSON('test.json'))

