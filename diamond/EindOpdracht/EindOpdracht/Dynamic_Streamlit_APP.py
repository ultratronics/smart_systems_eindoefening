#!/usr/bin/env python
# coding: utf-8

# ## Voeg de Librarys toe.

# In[1]:


# Initialiseer de librarys
import pickle
import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


# Controleer of er een lege string is
def CheckEmptyString(Variable):
    if Variable == "":
        return 0
    else:
        return Variable


# ## Get Data from de files

# In[3]:


PicklePath = "BreastCancerPickle.pkl"
PickleData = pickle.load(open(PicklePath, "+rb"))

CsvPath = "wisc_bc_data.csv"
CsvData = pd.read_csv(CsvPath)

st.write(CsvData.dtypes)

Aantal_Kolom = len(CsvData.columns)
Output_Categorie = "diagnosis"
Index_Output = CsvData.columns.get_loc(Output_Categorie)


# In[4]:


InputList = []
List1 = [] # np.empty((0,aantal_kolommen-1))
OutputNaam = ""


# In[21]:


number1 = st.sidebar.number_input('Insert a MIN-number')
st.write('The current number is ', number1)

number2 = st.sidebar.number_input('Insert a MAX-number')
st.write('The current number is ', number2)

# Range met slider bepalen
values = st.sidebar.slider('Select a range', 0, Aantal_Kolom, number1, number2)
st.write('Values:', values)


# In[ ]:





# In[22]:


for i in range(0, Aantal_Kolom):
    # print(i)
    # print(index_Output)
    if i == Index_Output:
        List1.append("output")
    else:
        List1.append("input")
        
print(List1)
st.write("Past 1st loop")


# In[23]:


for j in range(0, Aantal_Kolom):
    # print(j)
    if List1[j] == "input":
        if CsvData.dtypes[j] == "float64":
            temp = st.text_input(CsvData.columns[j], key = j)
            InputList.insert(j, float(CheckEmptyString(temp)) )
            
        if CsvData.dtypes[j] == "int64":
            temp = st.text_input(CsvData.columns[j], key = j)
            InputList.insert(j, float(CheckEmptyString(temp)) )
            
        if List1[j] == "output":
            OutputNaam = CsvData.columns[j]
            InputList.insert(j, "output")
st.write("Past 2nd loop")


# In[33]:


X_test = pd.DataFrame(InputList)

# Halen we de output kolom uit de list omdat deze hier niet nodig is.
X_test = X_test.drop(Index_Output)

st.write(InputList)
st.write(type(InputList))
st.write(X_test2)

Resultaat = PickleData.predict(X_test2.T)
#st.write(Resultaat)


