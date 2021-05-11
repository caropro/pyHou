#coding = utf-8
import shelve
data = {"a":1,"b":2}
db = shelve.open("data")
print db
for k,v in data.items():
    db[k] = v
db.close()

import glob
print(glob.glob("data"))