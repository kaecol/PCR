import csv
import re
import numpy as np

x = list(csv.reader(open('C:/Users/Ying Wei/Desktop/Raw File.csv')))

for index, line in enumerate(x):
    del(x[index][-7:])
    del(x[index][-7:-1])
    del(x[index][0])
    
header=x[0]
x.remove(header)

y = []
for index, line in enumerate(x):
    z = list(re.findall(r'[A-Ha-h]|[0-9]+',x[index][0]))
    z += x[index][1:]
    y.append(z)

mat=np.zeros((9,13)).tolist()
for i, j in enumerate(y):
    for a1, a2 in enumerate(['','A','B','C','D','E','F','G','H']):
        for b1, b2 in enumerate(['','01','02','03','04','05','06','07','08','09','10','11','12']):
            if b2 == '' and mat[a1][0] == 0.0 :
                mat[a1][0]=a2
            if a2 == '' and mat[0][b1] == 0.0 :
                mat[0][b1]=b2
            if y[i][0]==a2 and y[i][1]==b2:
                mat[a1][b1]=y[i][2]
print(mat)

with open('C:/Users/Ying Wei/Desktop/PCR.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for p in enumerate(mat):
         wr.writerow(p[1])

# =============================================================================
# with open('C:/Users/Ying Wei/Desktop/PCR.csv', 'w', newline='') as csvfile:
#      filewriter = csv.writer(csvfile, delimiter=',',
#                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
#      filewriter.writerow(['','01','02','03','04','05','06','07','08','09','10','11','12'])
#      filewriter.writerow(['A'])
#      filewriter.writerow(['B'])
#      filewriter.writerow(['C'])
#      filewriter.writerow(['D'])
#      filewriter.writerow(['E'])
#      filewriter.writerow(['F'])
#      filewriter.writerow(['G'])
#      filewriter.writerow(['H'])
# 
# 
# =============================================================================

