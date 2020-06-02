dicta = {"1: 10 , 2:20 "}
dictb = {"3:30, 4:40"}
dictc = {"5:50 , 6:60"}

dictd = {}

for d in (dicta,dictb,dictc): dictd.update(d)
print(dictd)