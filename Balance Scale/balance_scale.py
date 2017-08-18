from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import math

if __init__=="main":
    decision_tree()

def calculate_entropy(data,attribute):
    #calculate the frequency of records that are associated with each value of the attribute
    frequency={}
    data_entropy=0
    for record in data:
        if (frequency.has_key(record[attribute])):
            frequency[record[attribute]]+=1
        else:
            frequency[record[attribute]]=1
    #caluculate the total entropy of the dataset with the chosen attribute
    for freq in frequency.values():
        data_entropy += (-freq/len(data)) *log(freq/len(data),2)

    return data_entropy

def information_gain(data,attribute,target_attribute):
    ig_attribute_list={}
    weight_list={}
    #calculate the weight of each value that the attribute can take in the attribute_list
    for record in data:
        if weight_list.has_key(record[attribute]):
            weight_list[record[attribute]]+=1
        else:
            weight_list[record[attribute]]=1

    #multiply each entropy by its weight and add all  of them
    for value in weight_list.keys():
        weight=weight_list[value]/sum(weight_list.values())
        data_subset=[record for record in data if record[attribute]==value]
        subset_entropy += calculate_entropy(data_subset,target_attribute)

    #calculate information gain
    return (calculate_entropy(data,target_attribute)-subset_entropy)

def create_decision_tree(data,attribute,target_attribute):
    #create a copy of the data
    data=data[:]
    #get the count of the values that the target_attribute takes
    vals=[record[target_attribute] for record in data]
    #find the default value for the classification
    vals_np=np.array(vals)
    default=np.max(vals_np)


def bank_note_authentication():
    data=pd.read_csv("")
