from collections import OrderedDict
import readline
import matplotlib.pyplot as plt


def split(s):
    if '"' not in s:
        return s.split(',')
    ck = True
    l = []
    pre = 0
    for i in range(len(s)):
        if ck and s[i] == ',':
            l.append(s[pre:i])
            pre = i+1
        elif s[i] == '"':
            ck = not ck
    l.append(s[pre::])
    return l

f = open("D:\Downloads\export.csv", "r")
names = split(f.readline()[0:-1])[5::]
print(names)
line = f.readline()


l = {}

while True:
    try:
        line = f.readline()
        if line == '\n':
            break
        col = split(line[0:-1])
        if col[0] not in l:
            l[col[0]] = [0] * len(names)
        for i in range(5, len(col)):
            l[col[0]][i-5] += float(col[i])
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)
        print(col)
        print(len(col))
        break
xs = [[]] in range(len(names))
#ys = range(len(l)+1)
ys = ["0"]
for i in l.keys():
    ys.append(i)
l = OrderedDict(sorted(l.items()))

v = [[]]*(len(l)+1)
v[0] = [0]*len(names)
j = 0
for i in l.keys():
    j += 1
    v[j] = v[j-1].copy()
    for k in range(len(v[j])):
        v[j][k] += l[i][k]
        v[j][k] = round(v[j][k], 2)
xs = [[0 for x in range(len(l)+1)] for y in range(len(names))]
for i in range(len(v)):
    for j in range(len(names)):
        xs[j][i] = v[i][j]

for i in range(len(names)):
    plt.plot(ys, xs[i], label=names[i], linewidth=3)
plt.plot(ys, len(xs[0])*[0], linewidth=1)
plt.legend()
plt.show()