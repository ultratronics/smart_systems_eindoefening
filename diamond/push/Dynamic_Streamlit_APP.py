#!/usr/bin/env python
# coding: utf-8

# ## Voeg de Librarys toe.

# In[41]:


# Initialiseer de librarys
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import os


# In[2]:


# Controleer of er een lege string is
def CheckEmptyString(Variable):
    if Variable == "":
        return 0
    else:
        return Variable


# ## Selecteer een CSV file

# In[47]:


def file_selector(folder_path='.\EindOpdracht'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)


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


# ### slider om de range te bepalen

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


# In[34]:


X_test = pd.DataFrame(InputList)

# Halen we de output kolom uit de list omdat deze hier niet nodig is.
X_test = X_test.drop(Index_Output)

st.write(InputList)
st.write(type(InputList))
st.write(X_test)

Resultaat = PickleData.predict(X_test.T)
#st.write(Resultaat)


# ## Write to Heroku

# In[51]:


get_ipython().system("jupyter nbconvert --output-dir='.\\.\\push' --to script Dynamic_Streamlit_APP.ipynb")


# In[ ]:


#sed '757,759d' .\push\diamonds-in-depth-analysis.py
#tailer.head( -n -9 .\EindOpdracht\Dynamic_Streamlit_APP.py > .\push\pushreal\Dynamic_Streamlit_APP.py )
#tailer.head(open() -n -9 .\push\Dynamic_Streamlit_APP.py > .\push\pushreal\Dynamic_Streamlit_APP.py )


# In[36]:


readFile = open(".\.\push\pushreal\Dynamic_Streamlit_APP.py")

lines = readFile.readlines()

readFile.close()
w = open(".\.\push\pushreal\Dynamic_Streamlit_APP.py",'w')
w.writelines([item for item in lines[:-13]])
w.close()
