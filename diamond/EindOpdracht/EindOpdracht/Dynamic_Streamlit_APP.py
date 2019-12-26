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


# In[5]:


for i in range(0, Aantal_Kolom):
    # print(i)
    # print(index_Output)
    if i == Index_Output:
        List1.append("output")
    else:
        List1.append("input")
        
print(List1)
st.write("Past 1st loop")


# In[6]:


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


# In[7]:


X_test = pd.DataFrame(InputList)
X_test = X_test.drop(Index_Output)

st.write(InputList)
st.write(type(InputList))
st.write(X_test)

Resultaat = PickleData.predict(X_test.T)
st.write(Resultaat)


# ## Write to Heroku

# In[8]:


get_ipython().system("jupyter nbconvert --output-dir='.\\EindOpdracht' --to script Dynamic_Streamlit_APP.ipynb")


# In[ ]:


#sed '757,759d' .\push\diamonds-in-depth-analysis.py
#tailer.head( -n -9 .\EindOpdracht\Dynamic_Streamlit_APP.py > .\push\pushreal\Dynamic_Streamlit_APP.py )
#tailer.head(open() -n -9 .\push\Dynamic_Streamlit_APP.py > .\push\pushreal\Dynamic_Streamlit_APP.py )


# In[14]:


readFile = open(".\EindOpdracht\Dynamic_Streamlit_APP.py")

lines = readFile.readlines()

readFile.close()
w = open(".\EindOpdracht\Dynamic_Streamlit_APP.py",'w')
w.writelines([item for item in lines[:-1]])
w.close()

