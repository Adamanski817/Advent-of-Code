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

SimilarityScore = 0
for i in range(len(Colum1)):
    AmountNum= 0
    for j in range(len(Colum2)):
         if Colum1[i] == Colum2[j]:
             AmountNum+= 1
    SimilarityScore+= AmountNum * Colum1[i]

print (f'Answer to 1 is{totaldistance}')
print(f' Answer to 2 is{SimilarityScore}')
             
