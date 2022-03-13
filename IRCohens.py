from sklearn.metrics import cohen_kappa_score
import csv
import pandas as pd

sorted_ids = []

Katie_q1 = {}

Muskaan_q1 = {}

df = pd.read_csv('Survey7Katie.csv')
    

df.fillna(0, inplace=True)
df.sort_values(by=['Respondent'], inplace=True)
print(df)

for row in df.itertuples():
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        inner_list = []
        if (row[2] != "__NA__") and (row[3] != 0):
            inner_list.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            inner_list.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            inner_list.append(row[5])
        Katie_q1[row[1]] = inner_list
        sorted_ids.append(row[1])

print(Katie_q1)

df2 = pd.read_csv('MuskaanSurvey7.csv')
    

df2.fillna(0, inplace=True)
df2.sort_values(by=['Respondent'], inplace= True)
print(df2)

for row in df2.itertuples():
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        inner_list = []
        if (row[2] != "__NA__") and (row[3] != 0):
            inner_list.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            inner_list.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            inner_list.append(row[5])
        Muskaan_q1[row[1]] = inner_list


MuskaanYN_q1 = []
KatieYN_q1 = []
sorted_ids.sort()
print(sorted_ids)


def is_in_list(num):
    print("in list")
    print(num)
    KatieList = Katie_q1.get(num)
    print(KatieList)
    KatieList.sort()
    MuskaanList = Muskaan_q1.get(num)
    print(MuskaanList)
    MuskaanList.sort()
    #If both inner lists are the same length
    if len(KatieList) == len(MuskaanList):
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return True
    elif len(KatieList) > len(MuskaanList):
        for i in range(0, len(MuskaanList)):
            if MuskaanList[i] in KatieList:
                return True
    else:
        for i in range(0, len(MuskaanList)):
            if KatieList[i] in MuskaanList:
                return True
    return False
    
for i in range(0, len(sorted_ids)):
    inputVal = is_in_list(sorted_ids[i])
    if inputVal == False:
        MuskaanYN_q1.append(True)
        KatieYN_q1.append(False)
    else:
        MuskaanYN_q1.append(True)
        KatieYN_q1.append(True)


print(Katie_q1)
print(Muskaan_q1)
print(KatieYN_q1)
print(MuskaanYN_q1)

print(len(KatieYN_q1))
print(len(MuskaanYN_q1))

#Q1 cohen's kappa RI
q1IR = cohen_kappa_score(KatieYN_q1, MuskaanYN_q1)
print(q1IR)