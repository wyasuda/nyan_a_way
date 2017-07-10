# coding: UTF-8
gr = ["cat", "dog", "person", "yard"]

f = open('~/list_train.txt', 'w')
gc = 0
for grp in gr:
    for i in range(9000):
        tmpstr = "images/train/" + str(grp) + "." + str(i) + ".jpg " + str(gc) + "\n"
        f.write(tmpstr)
    gc = gc + 1
f.close()

f = open('~/list_test.txt', 'w')
gc = 0
for grp in gr:
    for i in range(9000, 10000):
        tmpstr = "images/test/" + str(grp) + "." + str(i) + ".jpg " + str(gc) + "\n"
        f.write(tmpstr)
    gc = gc + 1
f.close()
