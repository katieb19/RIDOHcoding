from sklearn.metrics import cohen_kappa_score
import csv
import pandas as pd

####Q1

#list of the sorted respondent ids
Katie_sorted_ids = []

Muskaan_sorted_ids = []

#dictionary that maps id to q1 code responses
Katie_q1 = {}

Muskaan_q1 = {}

#Load in Katie dataframe and clean

df = pd.read_csv('Survey7Katie.csv')
    

df.fillna(0, inplace=True)
df.sort_values(by=['Respondent'], inplace=True)
df["why_not_booster_1"] = df["why_not_booster_1"].astype('float64')
df["why_not_booster_2"] = df["why_not_booster_2"].astype('float64')
df["why_not_booster_3"] = df["why_not_booster_3"].astype('float64')
df["why_scientists_reliable_unreliable_1"] = df["why_scientists_reliable_unreliable_1"].astype('float64')
df["why_scientists_reliable_unreliable_2"] = df["why_scientists_reliable_unreliable_2"].astype('float64')
df["why_scientists_reliable_unreliable_3"] = df["why_scientists_reliable_unreliable_3"].astype('float64')
df["why_isolation_change_1"] = df["why_isolation_change_1"].astype('float64')
df["why_isolation_change_2"] = df["why_isolation_change_2"].astype('float64')
df["why_isolation_change_3"] = df["why_isolation_change_3"].astype('float64')


#Load in Muskaan dataframe and clean

df2 = pd.read_csv('MuskaanSurvey7.csv')
    

df2.fillna(0, inplace=True)
df2.sort_values(by=['Respondent'], inplace= True)
df2["why_not_booster_1"] = df2["why_not_booster_1"].astype('float64')
df2["why_not_booster_2"] = df2["why_not_booster_2"].astype('float64')
df2["why_not_booster_3"] = df2["why_not_booster_3"].astype('float64')
df2["why_scientists_reliable_unreliable_1"] = df2["why_scientists_reliable_unreliable_1"].astype('float64')
df2["why_scientists_reliable_unreliable_2"] = df2["why_scientists_reliable_unreliable_2"].astype('float64')
df2["why_scientists_reliable_unreliable_3"] = df2["why_scientists_reliable_unreliable_3"].astype('float64')
df2["why_isolation_change_1"] = df2["why_isolation_change_1"].astype('float64')
df2["why_isolation_change_2"] = df2["why_isolation_change_2"].astype('float64')
df2["why_isolation_change_3"] = df2["why_isolation_change_3"].astype('float64')


#loop through Katie dataframe and populate Katie_sorted_ids and Katie_q1
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

#loop through Muskaan dataframe and populate Muskaan_sorted_ids and Muskaan_q1
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


#Sorted ids
Katie_sorted_ids.sort()
Muskaan_sorted_ids.sort()


#list of list of codes for each respondent
Katie_final = []
Muskaan_final = []

#function that checks if Katie and Muskaan share at least one code for a respondent
def is_in_list(num):
        KatieList = Katie_q1.get(num)
        KatieList.sort()
        Katie_final.append(KatieList)
        MuskaanList = Muskaan_q1.get(num)
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
            for i in range(0, len(KatieList)):
                if KatieList[i] in MuskaanList:
                    return "yes"
        return "no"

#final lists (yes mean at least one overlap, no mean just put in first value from each response)
MuskaanYN_q1 = []
KatieYN_q1 = []   
for i in range(0, len(Katie_sorted_ids)):
    if Katie_sorted_ids[i] in Muskaan_sorted_ids:
        inputVal = is_in_list(Katie_sorted_ids[i])
        if inputVal == "no":
            MuskaanYN_q1.append(Muskaan_final[i][0])
            KatieYN_q1.append(Katie_final[i][0])
        else:
            MuskaanYN_q1.append("yes")
            KatieYN_q1.append("yes")

print("Overlap q1 ids")
print(Katie_sorted_ids)


#Q1 cohen's kappa RI
print("Length of overlap")
print(len(KatieYN_q1))
print("")

yes_count_q1 = 0

for i in KatieYN_q1:
    if i == "yes":
        yes_count_q1 += 1


print("yes proportion question 1")
print(yes_count_q1/len(KatieYN_q1))
print("")


q1IR = cohen_kappa_score(KatieYN_q1, MuskaanYN_q1)
print("kappa for q1")
print(q1IR)




#Q2
Katie_sorted_ids_2 = []

Muskaan_sorted_ids_2 = []

Katie_q2 = {}

Muskaan_q2 = {}

for row in df.itertuples():
   if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[6] != "__NA__") and (row[7] != 0):
            inner_list.append(row[7])
        if (row[6] != "__NA__") and (row[8] != 0):
            inner_list.append(row[8])
        if (row[6] != "__NA__") and (row[9] != 0):
            inner_list.append(row[9])
        Katie_q2[row[1]] = inner_list
        Katie_sorted_ids_2.append(row[1])

for row in df2.itertuples():
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[6] != "__NA__") and (row[7] != 0):
            inner_list.append(row[7])
        if (row[6] != "__NA__") and (row[8] != 0):
            inner_list.append(row[8])
        if (row[6] != "__NA__") and (row[9] != 0):
            inner_list.append(row[9])
        Muskaan_q2[row[1]] = inner_list
        Muskaan_sorted_ids_2.append(row[1])

MuskaanYN_q2 = []
KatieYN_q2 = []
Katie_sorted_ids_2.sort()
Muskaan_sorted_ids_2.sort()

Katie_final_ids = []
Muskaan_final_ids = []

#keep only overlapping sorted ids
for i in range(0, len(Muskaan_sorted_ids_2)):
    if Muskaan_sorted_ids_2[i] in Katie_sorted_ids_2:
        Muskaan_final_ids.append(Muskaan_sorted_ids_2[i])

for i in range(0, len(Katie_sorted_ids_2)):
    if Katie_sorted_ids_2[i] in Muskaan_sorted_ids_2:
        Katie_final_ids.append(Katie_sorted_ids_2[i])


Katie_final_2 = []
Muskaan_final_2 = []

def is_in_list(num):
    KatieList = Katie_q2.get(num)
    KatieList.sort()
    Katie_final_2.append(KatieList)
    MuskaanList = Muskaan_q2.get(num)
    MuskaanList.sort()
    Muskaan_final_2.append(MuskaanList)
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
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    return "no"
    

for i in range(0, len(Muskaan_final_ids)):
        inputVal = is_in_list(Katie_final_ids[i])
        if inputVal == "no":
            MuskaanYN_q2.append(Muskaan_final_2[i][0])
            KatieYN_q2.append(Katie_final_2[i][0])
        else:
            MuskaanYN_q2.append("yes")
            KatieYN_q2.append("yes")




#Q2 cohen's kappa RI
print("")
print("Length of overlap")
print(len(KatieYN_q2))
print("")

yes_count_q2 = 0

for i in KatieYN_q2:
    if i == "yes":
        yes_count_q2 += 1


print("yes proportion question 2")
print(yes_count_q2/len(KatieYN_q2))


q2IR = cohen_kappa_score(KatieYN_q2, MuskaanYN_q2)
print("kappa for q2")
print(q2IR)


#Q3

Katie_sorted_ids_3 = []

Muskaan_sorted_ids_3 = []

Katie_q3 = {}

Muskaan_q3 = {}

for row in df.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Katie_q3[row[1]] = inner_list
        Katie_sorted_ids_3.append(row[1])

for row in df2.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Muskaan_q3[row[1]] = inner_list
        Muskaan_sorted_ids_3.append(row[1])

MuskaanYN_q3 = []
KatieYN_q3 = []
Katie_sorted_ids_3.sort()
Muskaan_sorted_ids_3.sort()

Katie_final_ids_3 = []
Muskaan_final_ids_3 = []

#keep only overlapping sorted ids
for i in range(0, len(Muskaan_sorted_ids_3)):
    if Muskaan_sorted_ids_3[i] in Katie_sorted_ids_3:
        Muskaan_final_ids_3.append(Muskaan_sorted_ids_3[i])

for i in range(0, len(Katie_sorted_ids_3)):
    if Katie_sorted_ids_3[i] in Muskaan_sorted_ids_3:
        Katie_final_ids_3.append(Katie_sorted_ids_3[i])


Katie_final_3 = []
Muskaan_final_3 = []

def is_in_list(num):
    KatieList = Katie_q3.get(num)
    KatieList.sort()
    Katie_final_3.append(KatieList)
    MuskaanList = Muskaan_q3.get(num)
    MuskaanList.sort()
    Muskaan_final_3.append(MuskaanList)
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
        for i in range(0, len(KatieList)):
            if KatieList[i] in MuskaanList:
                return "yes"
    return "no"
    

for i in range(0, len(Muskaan_final_ids_3)):
        inputVal = is_in_list(Katie_final_ids_3[i])
        if inputVal == "no":
            MuskaanYN_q3.append(Muskaan_final_2[i][0])
            KatieYN_q3.append(Katie_final_2[i][0])
        else:
            MuskaanYN_q3.append("yes")
            KatieYN_q3.append("yes")




#Q3 cohen's kappa RI
print("Length of overlap")
print(len(KatieYN_q3))
print("")

yes_count_q3 = 0

for i in KatieYN_q3:
    if i == "yes":
        yes_count_q3 += 1


print("yes proportion question 3")
print(yes_count_q3/len(KatieYN_q3))
print("")


q3IR = cohen_kappa_score(KatieYN_q3, MuskaanYN_q3)
print("kappa for q3")
print(q3IR)



