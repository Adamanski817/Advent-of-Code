f = open('lines.txt','r')
Colum1 = []
Colum2= []
for line in f.read().split('\n'):
    Colum1.append(int(line[0:5]))
    Colum2.append(int(line[8:13]))

Colum1.sort()
Colum2.sort()

TotalDistance = 0
for i in range(len(Colum1)):
    if Colum1[i]>Colum2[i]:
        distance = abs(Colum1[i]-Colum2[i])
        TotalDistance+=distance
    elif Colum2[i]>Colum1[i]:
        distance = abs(Colum2[i]-Colum1[i])
        TotalDistance+=distance

print (TotalDistance)
