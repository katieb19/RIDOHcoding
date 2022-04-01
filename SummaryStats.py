import csv
from os import remove
import pandas as pd

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


#Q1 summary stats

#list of responses for q 1
Katie_q1 = []

Muskaan_q1 = []

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
        Katie_q1.append(inner_list)

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
        Muskaan_q1.append(inner_list)


#Generates summary for only one
def summary_gen(code: int, name1: bool, name2: bool, list1: list, list2: list):
    if (name1 == True) and (name2 == False):
        count = 0
        for i in list1:
            if code in i:
                count += 1
        return count/len(list1)
    elif (name2 == True) and (name1 == False):
        count = 0
        for i in list2:
            if code in i:
                count += 1
        return count/len(list2)
    else:
        return 0

# generating combined summary stats

# Q1
combined_dict_mremove = {}
combined_dict_kremove = {}


# stats with katie's values for overlap
for row in df2.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_mremove[id] = values

for row in df.itertuples():
    id = row[1]
    values = []
    if (row[3] != 0 or row[4] != 0 or row[5] != 0):
        if (row[2] != "__NA__") and (row[3] != 0):
            values.append(row[3])
        if (row[2] != "__NA__") and (row[4] != 0):
            values.append(row[4])
        if (row[2] != "__NA__") and (row[5] != 0):
            values.append(row[5])
        combined_dict_mremove[id] = values

mremove_freq = {}

for id in combined_dict_mremove:
    values = combined_dict_mremove[id]
    for value in values:
        if (value not in mremove_freq.keys()):
            mremove_freq[value] = 1
        else:
            mremove_freq[value] += 1

print("Combined summary q1 Katie overlap")
print(mremove_freq)

print("Combined dataset with Muskaan overlap removed")
print(combined_dict_mremove)

print("freq of code 2 for Muskaan")
print(summary_gen(2, False, True, Katie_q1, Muskaan_q1))

print("freq of code 2 for both")
print(summary_gen(2, True, True, Katie_q1, Muskaan_q1))


#Testing

test_list_1 = [[1], [1], [2, 1], [3]]
test_list_2 = [[2], [2], [1], [3, 2]]

#freq for code 1 in test list 1 should be .75; in both should be .5

print("test 1 freq code 1")
print(summary_gen(1, True, False, test_list_1, test_list_2))

print("test 1 + 2 freq code 1")
print(summary_gen(1, True, True, test_list_1, test_list_2))


#Q2 (NOTE: This is for all codes not just the overlapping ones)

Katie_q2 = []

Muskaan_q2 = []

for row in df.itertuples():
   if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[6] != "__NA__") and (row[7] != 0):
            inner_list.append(row[7])
        if (row[6] != "__NA__") and (row[8] != 0):
            inner_list.append(row[8])
        if (row[6] != "__NA__") and (row[9] != 0):
            inner_list.append(row[9])
        Katie_q2.append(inner_list)

for row in df2.itertuples():
    if (row[7] != 0 or row[8] != 0 or row[9] != 0):
        inner_list = []
        if (row[6] != "__NA__") and (row[7] != 0):
            inner_list.append(row[7])
        if (row[6] != "__NA__") and (row[8] != 0):
            inner_list.append(row[8])
        if (row[6] != "__NA__") and (row[9] != 0):
            inner_list.append(row[9])
        Muskaan_q2.append(inner_list)


#Q3 (NOTE: This is for all codes not just the overlapping ones)

Katie_q3 = []

Muskaan_q3 = []

for row in df.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Katie_q3.append(inner_list)

for row in df2.itertuples():
    if (row[11] != 0 or row[12] != 0 or row[13] != 0):
        inner_list = []
        if (row[10] != "__NA__") and (row[11] != 0):
            inner_list.append(row[11])
        if (row[10] != "__NA__") and (row[12] != 0):
            inner_list.append(row[12])
        if (row[10] != "__NA__") and (row[13] != 0):
            inner_list.append(row[13])
        Muskaan_q3.append(inner_list)

#print(summary_gen(2, True, False, Katie_q3, Muskaan_q3))