from sklearn.metrics import cohen_kappa_score
import csv
import pandas as pd

Katie_sorted_ids = []

Muskaan_sorted_ids = []

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
        Katie_sorted_ids.append(row[1])

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
        Muskaan_sorted_ids.append(row[1])


MuskaanYN_q1 = []
KatieYN_q1 = []
Katie_sorted_ids.sort()
Muskaan_sorted_ids.sort()


Katie_final = []
Muskaan_final = []

def is_in_list(num):
        print("in list")
        print(num)
        KatieList = Katie_q1.get(num)
        print(KatieList)
        KatieList.sort()
        Katie_final.append(KatieList)
        MuskaanList = Muskaan_q1.get(num)
        print(MuskaanList)
        MuskaanList.sort()
        Muskaan_final.append(MuskaanList)
        #If both inner lists are the same length
        if len(KatieList) == len(MuskaanList):
            for i in range(0, len(KatieList)):
                if KatieList[i] in MuskaanList:
                    return "yes"
        elif len(KatieList) > len(MuskaanList):
            for i in range(0, len(MuskaanList)):
                if MuskaanList[i] in KatieList:
                    return "yes"
        else:
            for i in range(0, len(MuskaanList)):
                if KatieList[i] in MuskaanList:
                    return "yes"
        return "no"
        
for i in range(0, len(Katie_sorted_ids)):
    if Katie_sorted_ids[i] in Muskaan_sorted_ids:
        inputVal = is_in_list(Katie_sorted_ids[i])
        if inputVal == "no":
            MuskaanYN_q1.append("yes")
            KatieYN_q1.append("no")
        else:
            MuskaanYN_q1.append("yes")
            KatieYN_q1.append("yes")


print(Katie_q1)
print(Muskaan_q1)
print(KatieYN_q1)
print(MuskaanYN_q1)

print(Katie_final)
print(len(Katie_final))
print(Muskaan_final)
print(len(Muskaan_final))
print(len(KatieYN_q1))
print(len(MuskaanYN_q1))

#Q1 cohen's kappa RI
q1IR = cohen_kappa_score(KatieYN_q1, MuskaanYN_q1)


r1=['yes','yes','yes','yes','yes','yes','yes','yes','yes']

r2=['yes','yes','yes','no','no','no','yes','yes','yes']

pq = cohen_kappa_score(r1, r2)
print(q1IR)
print(pq)

#Manual
filteredK = list(filter(lambda ans: ans == 'yes', KatieYN_q1))
po = len(filteredK) / len(KatieYN_q1)

filteredM = list(filter(lambda ans: ans == 'yes', MuskaanYN_q1))
pe = (len(filteredK) /len(KatieYN_q1)) * (len(filteredM) / len(MuskaanYN_q1))

print(pe)
print(po)
kappa = (po - pe) / (1 - pe)

print(kappa)

#issue currently is that im creating one measure of whether something is equal and putting yes as a default; this is creating a value of 0 in the equation for cohen's kappa