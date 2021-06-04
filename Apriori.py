import pandas as pd
import itertools


def sublst(lst1, lst2):
    return set(lst1).issubset(set(lst2))


print("Enter the Minimum Support:")
min_support = int(input())

df = pd.read_csv('marketdata.csv')
#df.drop('Index', axis=1)
print(df.head())
row,col = df.shape

records = []
for i in range(0, row):
    records.append([str(df.values[i,j]) for j in range(0, col)])
items = sorted([item for sublist in records for item in sublist if item != 'nan'])

candidate = {i:items.count(i) for i in items}
level = {}

for item, count in candidate.items():
    if count >= min_support:
        level[item] = count 
print('level 1 output:', level)
print('End of Level: 1')

level = sorted(list(level.keys()))
LEVEL = list(itertools.combinations(level, 2))
candidate = {}
level = {}
for iter1 in LEVEL:
    count = 0
    for iter2 in records:
        if sublst(iter1, iter2):
            count+=1
    candidate[iter1] = count
for item, cnt in candidate.items():
    if cnt >= min_support:
            level[item] = cnt 
print('level 2 output:',level)
print('End of Level: 2')

k =3
while (len(level) != 0):
    level = list(level.keys())
    LEVEL = sorted(list(set([item for t in level for item in t])))
    LEVEL = list(itertools.combinations(LEVEL, k))
    candidate = {}
    level = {}
    for iter1 in LEVEL:
        count = 0
        for iter2 in records:
            if sublst(iter1, iter2):
                count+=1
        candidate[iter1] = count
    for item, count2 in candidate.items():
        if count2 >= min_support:
                level[item] = count2 

    if(len(level) != 0):
        print('Level:', k)
        print('level', k, 'output', level)
        print('End of Level: ', k)
        k+=1
    else:
        print('Maximum Levels Obtained')
