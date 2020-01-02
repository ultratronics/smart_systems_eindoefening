#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle

import streamlit as st

import pandas as pd
import numpy as np


def checkIfStringEmpty(var):
    if var == "":
        return 0
    else:
        return var

model =pickle.load(open("./BreastCancerPickle.pkl","+rb"))
test = pd.read_csv("./wisc_bc_data(1).csv")
st.write(test.dtypes)
aantal_kolommen = len(test.columns)
output_categorie = "diagnosis"
index_output = test.columns.get_loc(output_categorie)
inputlist = []
list1 = []  # np.empty((0,aantal_kolommen-1))
outputnaam = ""
for i in range(0, aantal_kolommen):
    # print(i)
    # print(index_output)
    if i == index_output:
        list1.append("output")
    else:
        list1.append("input")
print(list1)

st.write("hallo")


for j in range(0, aantal_kolommen):
    print(j)
    # print(index_output)
    if list1[j] == "input":
        if test.dtypes[j] == "float64":
            # inputlist.insert(j, st.text_input(test.columns[j], key=j))
            temp = st.text_input(test.columns[j], key=j)
            inputlist.insert(j, float(checkIfStringEmpty(temp)))
        if test.dtypes[j] == "int64":
            temp = st.text_input(test.columns[j], key=j)
            inputlist.insert(j, int(checkIfStringEmpty(temp)))
    if list1[j] == "output":
        outputnaam = test.columns[j]
        inputlist.insert(j, "output")



X_test = pd.DataFrame(inputlist)
X_test = X_test.drop(index_output)
st.write(inputlist)
st.write(type(inputlist))

st.write(X_test)

resultaat = model.predict(X_test.T)
st.write(resultaat)


get_ipython().system("jupyter nbconvert --output-dir='./push' --to script autopickl.ipynb")
get_ipython().system('head -n -7 ./push/autopickl.py > ../automatisch_pickle/autopickl.py')
 get_ipython().system('git -C ../automatisch_pickle commit -am "Nieuw commit" | git -C ./push/pushreal push heroku master')
# !git -C ./automatisch_pc commit -am "Nieuw commit" | git -C ./push/pushreal push heroku master

