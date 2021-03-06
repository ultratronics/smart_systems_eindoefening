#!/usr/bin/env python
# coding: utf-8

# # DIAMONDS IN-DEPTH ANALYSIS
# * You can also view the notebook on the link below.
# * *Github Link* - **https://github.com/Chinmayrane16/Diamonds-In-Depth-Analysis**
# * **Do Upvote if you like it :)**

# # Topics
# 1. [**Exploring Dataset**](#there_you_go_1)
# 2. [**Correlation b/w Features**](#there_you_go_2)
# 3. [**Visualizations**](#there_you_go_3)
# 4. [**Feature Engineering**](#there_you_go_4)
# 5. [**Feature Encoding**](#there_you_go_5)
# 6. [**Feature Scaling**](#there_you_go_6)
# 7. [**Modelling Algorithms**](#there_you_go_7)
# 8. [**Comparing R2 Scores**](#there_you_go_8)

# ## What are Diamonds?
# * **Diamonds are the Precious stone consisting of a clear and colourless Crystalline form of pure carbon.**
# * **They are the hardest Gemstones known to man and can be scratched only by other Diamonds.**

# ![](https://i.imgur.com/blhMqmD.jpg)

# ## How Diamonds are formed?
# * **Diamonds are formed deep within the Earth about 100 miles or so below the surface in the upper mantle.**
# * **Obviously in that part of the Earth it’s very hot.** 
# * **There’s a lot of pressure, the weight of the overlying rock bearing down, so that combination of high temperature and high pressure is what’s necessary to grow diamond crystals in the Earth.**

# ## Why are Diamonds so Valuable?
# * **Whether it is a Rare book, a fine bottle of Scotch, or a Diamond, something that is Rare and Unique is often expensive.**
# * **But what makes it truly Valuable is that this Rarity coincides with the desire of many to possess it. ;)**
# * **Diamonds are Rare because of the Incredibly powerful forces needed to create them.**
# 
# 
# * **And therefore Diamonds are considered to be Very Costly.**

# <a id="there_you_go_1"></a>
# # 1) Explore Dataset & Examine what Features affect the Price of Diamonds.

# ## 1.1) Importing Libraries

# In[1]:


import streamlit as st
import plotly as px
from PIL import Image
import os
#import cv2
#print (cv2.__version__)
#st.text('hello test 123 does this work?')

# Ignore warnings :
#import warnings
#warnings.filterwarnings('ignore')


# Handle table-like data and matrices :
import numpy as np
import pandas as pd
import math 



# Modelling Algorithms :

# Classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis , QuadraticDiscriminantAnalysis

# Regression
from sklearn.linear_model import LinearRegression,Ridge,Lasso,RidgeCV, ElasticNet
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,GradientBoostingRegressor,AdaBoostRegressor 
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor




# Modelling Helpers :
from sklearn.preprocessing import Normalizer , scale
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.model_selection import GridSearchCV , KFold , cross_val_score



#preprocessing :
from sklearn.preprocessing import MinMaxScaler , StandardScaler, LabelEncoder



#evaluation metrics :

# Regression
from sklearn.metrics import mean_squared_log_error,mean_squared_error, r2_score,mean_absolute_error 

# Classification
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score  



# Visualisation
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
import missingno as msno 


# Configure visualisations
#%matplotlib inline
mpl.style.use( 'ggplot' )
plt.style.use('fivethirtyeight')
sns.set(context="notebook", palette="dark", style = 'whitegrid' , color_codes=True)
params = { 
    'axes.labelsize': "large",
    'xtick.labelsize': 'x-large',
    'legend.fontsize': 20,
    'figure.dpi': 150,
    'figure.figsize': [25, 7]
}
plt.rcParams.update(params)


# In[2]:


# Title van Diamenten
st.title('Data Analyse van Diamonds met Streamlit')


# In[ ]:





# ## 1.2) Extract Dataset
# * Specify the location to the Dataset and Import them.

# In[3]:


df = pd.read_csv('diamonds.csv')
#diamonds = df.copy()


# In[4]:


# How the data looks
df.head()


# ## Streamlit Code

# In[5]:


# printen de 5 eerste uit.
# st.title("Dataframe head")
# st.dataframe(df.head())


# In[ ]:





# ## 1.3) Features
# * **Carat : ** Carat weight of the Diamond.
# * **Cut : ** Describe cut quality of the diamond.
# > * Quality in increasing order Fair, Good, Very Good, Premium, Ideal .
# * **Color : ** Color of the Diamond.
# > * With D being the best and J the worst.
# * **Clarity : ** Diamond Clarity refers to the absence of the Inclusions and Blemishes.
# > * (In order from Best to Worst, FL = flawless, I3= level 3 inclusions) FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, I2, I3
# * **Depth : ** The Height of a Diamond, measured from the Culet to the table, divided by its average Girdle Diameter.
# * **Table : ** The Width of the Diamond's Table expressed as a Percentage of its Average Diameter.
# * **Price : ** the Price of the Diamond.
# * **X : ** Length of the Diamond in mm.
# * **Y : ** Width of the Diamond in mm.
# * **Z : ** Height of the Diamond in mm.
# 
# *Qualitative Features (Categorical) : Cut, Color, Clarity. *
# 
# *Quantitative Features (Numerical) : Carat, Depth , Table , Price , X , Y, Z.*
# 
# 
# ### Price is the Target Variable.

# ![](https://i.imgur.com/Bbf0GWk.jpg)

# In[6]:


# We'll Explore All the features in the Later Part, Now let's look for Null Values if any..


# ## 1.4) Drop the 'Unnamed: 0' column as we already have Index.

# In[7]:


df.drop(['Unnamed: 0'] , axis=1 , inplace=True)
df.head()


# In[8]:


df.tail()


# In[9]:


df.shape


# In[10]:


# So, We have 53,940 rows and 10 columns


# In[11]:


df.info()


# ## 1.5) Examine NaN Values

# In[12]:


# It seems there are no Null Values.
# Let's Confirm
df.isnull().sum()


# In[13]:


msno.matrix(df) # just to visualize. no missing values.


# ### Great, So there are no NaN values.

# In[14]:


df.describe()


# ### Wait
# * **Do you see the Min. Values of X, Y and Z. It can't be possible..!!**
# * **It doesn't make any sense to have either of Length or Width or Height to be zero..**

# ### Let's Have a look at them.

# In[15]:


df.loc[(df['x']==0) | (df['y']==0) | (df['z']==0)]


# In[16]:


len(df[(df['x']==0) | (df['y']==0) | (df['z']==0)])


# ### We can see there are 20 rows with Dimensions 'Zero'.
# * **We'll Drop them as it seems better choice instead of filling them with any of Mean or Median**

# ## Streamlit keuze menu voor data 

# In[17]:


# display data
Keuze = { "info": df.info(),
        "head": df.head(),
        "tail": df.tail(),
        "describe": df.describe(),
        "isnull": df.isnull().sum(),
        "loc": df.loc[(df['x']==0) | (df['y']==0) | (df['z']==0)] }

Selected = st.sidebar.selectbox("Kies Wat je wilt zien", list(Keuze.keys()),0)
st.write(Keuze[Selected], use_column_width= True, caption= Keuze[Selected])


# In[18]:


# if Selected == "loc":
#    st.slider("Range", df[0], df[-1])


# ## 1.6) Dropping Rows with Dimensions 'Zero'.

# In[19]:


df = df[(df[['x','y','z']] != 0).all(axis=1)]


# In[20]:


# Just to Confirm
df.loc[(df['x']==0) | (df['y']==0) | (df['z']==0)]


# In[21]:


# Nice and Clean. :


# ## 1.7) Scaling of all Features

# In[22]:


sns.factorplot(data=df , kind='box' , size=7, aspect=2.5)
st.pyplot()


# **The Values are Distributed over a Small Scale.**

# In[ ]:





# <a id="there_you_go_2"></a>
# # 2) Correlation Between Features

# In[23]:


# Correlation Map
corr = df.corr()
sns.heatmap(data=corr, square=True , annot=True, cbar=True)
st.pyplot()


# ## CONCLUSIONS :
# **1. Depth is inversely related to Price.**
# > * This is because if a Diamond's Depth percentage is too large or small the Diamond will become '__Dark__' in appearance because it will no longer return an Attractive amount of light.
# 
# **2. The Price of the Diamond is highly correlated to Carat, and its Dimensions.**
# 
# **3. The Weight (Carat) of a diamond has the most significant impact on its Price. **
# > * Since, the larger a stone is, the Rarer it is, one 2 carat diamond will be more '__Expensive__' than the total cost of two 1 Carat Diamonds of the same Quality.
# 
# **4. The Length(x) , Width(y) and Height(z) seems to be higly related to Price and even each other.**
# 
# **5. Self Relation ie. of a feature to itself is 1 as expected.**
# 
# **6. Some other Inferences can also be drawn.**

# In[ ]:





# <a id="there_you_go_3"></a>
# # 3. Visualization Of All Features

# ## 3.1) Carat
# 
# * **Carat refers to the Weight of the Stone, not the Size.**
# * **The Weight of a Diamond has the most significant Impact on its Price.**
# * **Since the larger a Stone is, the Rarer it is, one 2 Carat Diamond will be more Expensive than the Total cost of two 1 Carat Diamonds of the Same Quality.**
# * **The carat of a Diamond is often very Important to People when shopping But it is a Mistake to Sacrifice too much quality for sheer size.**
# 
# 
# [Click Here to Learn More about How Carat Affects the Price of Diamonds.](https://www.diamondlighthouse.com/blog/2014/10/23/how-carat-weight-affects-diamond-price/)

# ![](https://i.imgur.com/hA3oat5.png)

# In[24]:


# Visualize via kde plots


# In[25]:


sns.kdeplot(df['carat'], shade=True , color='r')


# In[26]:


# Select box for options
Options = st.selectbox("Select Your options:", df['carat'])
"You selected: ", Options

st.area_chart(df['carat'])


# ## Streamlit Code

# In[27]:


# display data
Value = { "carat": df['carat'],
        "price": df['price'],
        "depth": df['depth'],
        "table": df['table'] }

Selected2 = st.sidebar.selectbox("Kies Wat je wilt zien op de grafiek_1", list(Value.keys()),0)
#st.write(Value[Selected], use_column_width= True, caption= Value[Selected2])

st.area_chart(Value[Selected2])


# In[28]:


# display data
Value2 = { "carat": df['carat'],
        "price": df['price'],
        "depth": df['depth'],
        "table": df['table'] }

SelectedX = st.sidebar.selectbox("Kies Wat je wilt zien op de X-as", list(Value2.keys()),0)
#st.write(Value[Selected], use_column_width= True, caption= Value[Selected2])
SelectedY = st.sidebar.selectbox("Kies Wat je wilt zien op de Y-as", list(Value2.keys()),0)
#st.write(Value[Selected], use_column_width= True, caption= Value[Selected2])

st.text("Show Grafiek_2")
sns.jointplot(x= SelectedX , y= SelectedY , data=df , size=5)
st.pyplot()


# In[29]:


plt.hist('depth' , data=df , bins=25)

# display data
HistY = { "carat_": df['carat'],
        "price_": df['price'],
        "depth_": df['depth'],
        "table_": df['table'] }

HistValue = st.sidebar.selectbox("Histogtam Y-as", list(HistY.keys()),0)
#st.write(Value[Selected], use_column_width= True, caption= Value[Selected2])
BinsX = st.sidebar.number_input("Insert Nummer: ")
#st.write(Value[Selected], use_column_width= True, caption= Value[Selected2])

st.text("Show Histogram_2")
#plt.hist(HistValue , data= df , bins= (1 + BinsX) )
#st.bar_ch
#st.pyplot()


# ### Carat vs Price

# In[30]:


sns.jointplot(x='carat' , y='price' , data=df , size=5)


# ### It seems that Carat varies with Price Exponentially.

# In[ ]:





# ## 3.2) Cut
# 
# * **Although the Carat Weight of a Diamond has the Strongest Effect on Prices, the Cut can still Drastically Increase or Decrease its value.**
# * **With a Higher Cut Quality, the Diamond’s Cost per Carat Increases.**
# * **This is because there is a Higher Wastage of the Rough Stone as more Material needs to be Removed in order to achieve better Proportions and Symmetry.**
# 
# [Click Here to Lean More about How Cut Affects the Price.](https://www.lumeradiamonds.com/diamond-education/diamond-cut)

# ![](https://i.imgur.com/6PannTm.jpg)

# In[31]:


sns.factorplot(x='cut', data=df , kind='count',aspect=2.5 )


# ## Cut vs Price

# In[32]:


sns.factorplot(x='cut', y='price', data=df, kind='box' ,aspect=2.5 )


# In[33]:


# Understanding Box Plot :

# The bottom line indicates the min value of Age.
# The upper line indicates the max value.
# The middle line of the box is the median or the 50% percentile.
# The side lines of the box are the 25 and 75 percentiles respectively.


# ### Premium Cut on Diamonds as we can see are the most Expensive, followed by Excellent / Very Good Cut.

# In[ ]:





# ## 3.3) Color
# * **The Color of a Diamond refers to the Tone and Saturation of Color, or the Depth of Color in a Diamond.**
# * **The Color of a Diamond can Range from Colorless to a Yellow or a Faint Brownish Colored hue.**
# * **Colorless Diamonds are Rarer and more Valuable because they appear Whiter and Brighter.**
# 
# [Click Here to Learn More about How Color Affects the Price](https://enchanteddiamonds.com/education/understanding-diamond-color)

# ![](https://i.imgur.com/Ij090Kn.jpg)

# In[34]:


sns.factorplot(x='color', data=df , kind='count',aspect=2.5 )


# ### Color vs Price

# In[35]:


sns.factorplot(x='color', y='price' , data=df , kind='violin', aspect=2.5)


# In[ ]:





# ## 3.4) Clarity
# * **Diamond Clarity refers to the absence of the Inclusions and Blemishes.**
# * **An Inclusion is an Imperfection located within a Diamond. Inclusions can be Cracks or even Small Minerals or Crystals that have formed inside the Diamond.**
# * **Blemishing is a result of utting and polishing process than the environmental conditions in which the diamond was formed. It includes scratches, extra facets etc.**
# 
# [Click Here to Learn More about How Clarity Affects the Price of Diamonds.](https://www.diamondmansion.com/blog/understanding-how-diamond-clarity-affects-value/)

# ![](https://i.imgur.com/fLbAstc.jpg)

# In[36]:


labels = df.clarity.unique().tolist()
sizes = df.clarity.value_counts().tolist()
colors = ['#006400', '#E40E00', '#A00994', '#613205', '#FFED0D', '#16F5A7','#ff9999','#66b3ff']
explode = (0.1, 0.0, 0.1, 0, 0.1, 0, 0.1,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=0)
plt.axis('equal')
plt.title("Percentage of Clarity Categories")
plt.plot()
fig=plt.gcf()
fig.set_size_inches(6,6)
plt.show()


# In[37]:


sns.boxplot(x='clarity', y='price', data=df )


# ### It seems that VS1 and VS2 affect the Diamond's Price equally having quite high Price margin.

# In[ ]:





# ## 3.5) Depth
# * **The Depth of a Diamond is its Height (in millimeters) measured from the Culet to the Table.**
# * **If a Diamond's Depth Percentage is too large or small the Diamond will become Dark in appearance because it will no longer return an Attractive amount of light.**
# 
# [Click Here to Learn More about How Depth Affects the Price of Diamonds.](https://beyond4cs.com/grading/depth-and-table-values/)

# In[38]:


plt.hist('depth' , data=df , bins=25)


# In[39]:


sns.jointplot(x='depth', y='price' , data=df , kind='regplot', size=5)


# ### We can Infer from the plot that the Price can vary heavily for the same Depth.
# * **And the Pearson's Correlation shows that there's a slightly inverse relation between the two.**

# In[ ]:





# ## 3.6) Table
# * **Table is the Width of the Diamond's Table expressed as a Percentage of its Average Diameter.**
# * **If the Table (Upper Flat Facet) is too Large then light will not play off of any of the Crown's angles or facets and will not create the Sparkly Rainbow Colors.**
# * **If it is too Small then the light will get Trapped and that Attention grabbing shaft of light will never come out but will “leak” from other places in the Diamond.**
# 
# [Click Here to Learn More about How Table Affects the Price of Diamonds.](https://beyond4cs.com/grading/depth-and-table-values/)

# In[40]:


sns.kdeplot(df['table'] ,shade=True , color='orange')


# In[41]:


sns.jointplot(x='table', y='price', data=df , size=5)


# In[ ]:





# ## 3.7) Dimensions

# * **As the Dimensions increases, Obviously the Prices Rises as more and more Natural Resources are Utilised.**

# In[42]:


sns.kdeplot(df['x'] ,shade=True , color='r' )
sns.kdeplot(df['y'] , shade=True , color='g' )
sns.kdeplot(df['z'] , shade= True , color='b')
plt.xlim(2,10)


# **We'll Create a New Feature based on the Dimensions in the Next Section called 'Volume' and Visualize how it affects the Price.**

# In[ ]:





# <a id="there_you_go_4"></a>
# # 4) Feature Engineering

# ## 4.1) Create New Feature 'Volume'

# In[43]:


df['volume'] = df['x']*df['y']*df['z']
df.head()


# In[44]:


plt.figure(figsize=(5,5))
plt.hist( x=df['volume'] , bins=30 ,color='g')
plt.xlabel('Volume in mm^3')
plt.ylabel('Frequency')
plt.title('Distribution of Diamond\'s Volume')
plt.xlim(0,1000)
plt.ylim(0,50000)


# In[45]:


sns.jointplot(x='volume', y='price' , data=df, size=5)


# ### It seems that there is Linear Relationship between Price and Volume (x \* y \* z).

# ## 4.2) Drop X, Y, Z

# In[46]:


df.drop(['x','y','z'], axis=1, inplace= True)
#df.head()


# In[ ]:





# <a id="there_you_go_5"></a>
# # 5) Feature Encoding

# * **Label the Categorical Features with digits to Distinguish.**
# * **As we can't feed String data for Modelling.**

# In[47]:


label_cut = LabelEncoder()
label_color = LabelEncoder()
label_clarity = LabelEncoder()


df['cut'] = label_cut.fit_transform(df['cut'])
df['color'] = label_color.fit_transform(df['color'])
df['clarity'] = label_clarity.fit_transform(df['clarity'])


# In[48]:


#df.head()


# <a id="there_you_go_6"></a>
# # 6) Feature Scaling

# * **Divide the Dataset into Train and Test, So that we can fit the Train for Modelling Algos and Predict on Test.**
# * **Then Apply Feature Scaling although it's not neccessary in this case. But it surely helps.**

# In[49]:


# Split the data into train and test.


# In[50]:


X = df.drop(['price'], axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=66)


# In[51]:


# Applying Feature Scaling ( StandardScaler )
# You can also Apply MinMaxScaler.


# In[52]:


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[ ]:





# <a id="there_you_go_7"></a>
# # 7) Modelling Algos

# In[53]:


# Collect all R2 Scores.
R2_Scores = []
models = ['Linear Regression' , 'Lasso Regression' , 'AdaBoost Regression' , 'Ridge Regression' , 'GradientBoosting Regression',
          'RandomForest Regression' ,
         'KNeighbours Regression']


# ## 7.1) Linear Regression

# ## 7.2) Lasso Regression

# ## 7.3) AdaBosst Regression

# ## 7.4) Ridge Regression

# ## 7.5) GradientBoosting Regression

# In[54]:


clf_rf = RandomForestRegressor()
#clf_rf.fit(X_train , y_train)
import pickle
clf_rf = pickle.load(open("Model.pkl", "+rb"))


accuracies = cross_val_score(estimator = clf_rf, X = X_train, y = y_train, cv = 5,verbose = 1)
y_pred = clf_rf.predict(X_test)
print('')
print('###### Random Forest ######')
print('Score : %.4f' % clf_rf.score(X_test, y_test))
print(accuracies)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred)**0.5
r2 = r2_score(y_test, y_pred)

print('')
print('MSE    : %0.2f ' % mse)
print('MAE    : %0.2f ' % mae)
print('RMSE   : %0.2f ' % rmse)
print('R2     : %0.2f ' % r2)


# In[55]:


# wat zit in de variable
print(clf_rf)
print(clf_rf.n_estimators)


# In[56]:


print(X_test[0])


# ## Streamit Code Lego DataSet

# In[57]:


# wat zit in de variable
#LegoX = pickle.load(open("x.pickle", "+rb"))
#print(LegoX)


# In[58]:


# wat zit in de variable
#LegoY = pickle.load(open("y.pickle", "+rb"))
#print(LegoY)


# In[ ]:





# In[59]:


if st.sidebar.checkbox("Show LijnGrafiek clf_rf"):
    st.text("Lijngrafiek van Pickle file")
    st.line_chart(clf_rf)


# In[60]:


# titel van de pagina
st.title('Data Analyse van Lego met Streamlit')


# In[61]:


# display picture
Fotos = { "02300BL": "http://11500991.pxl-ea-ict.be/SmartSys/02300%20BLUE/02300_BLUE_1.jpg",
        "3198LG": "http://11500991.pxl-ea-ict.be/SmartSys/3198%20LIGHTGREEN/3198_lightgreen_3.jpg",
        "3437BR": "http://11500991.pxl-ea-ict.be/SmartSys/3437%20BROWN/3437_brown_2.jpg",
        "3437GR": "http://11500991.pxl-ea-ict.be/SmartSys/3437%20GREEN/3437_green_1.jpg",
        "3437LB": "http://11500991.pxl-ea-ict.be/SmartSys/3437%20LIGHTBLUE/jason/3437_lightblue_5.jpg",
        "6437YE": "http://11500991.pxl-ea-ict.be/SmartSys/6474%20YELLOW/3437_yellow_3.jpg"}

Foto = st.sidebar.selectbox("Kies Foto", list(Fotos.keys()),0)
st.image(Fotos[Foto], use_column_width= True, caption= Fotos[Foto])


# In[62]:


if Foto == "02300BL":
    st.write("Selected: 02300BL")
if Foto == "3198LG":
    st.write("Selected: 3198LG")
if Foto == "3437BR":
    st.write("Selected: 3437BR")
if Foto == "3437GR":
    st.write("Selected: 3437GR")
if Foto == "3437LB":
    st.write("Selected: 3437LB")
if Foto == "6437YE":
    st.write("Selected: 6437YE")


# In[ ]:





# In[ ]:





# ### Tuning Parameters

# In[63]:


#test


# In[64]:


get_ipython().system("jupyter nbconvert --output-dir='.\\push' --to script diamonds-in-depth-analysis.ipynb")


# In[65]:


#sed '757,759d' .\push\diamonds-in-depth-analysis.py
#tailer.head( -n -9 .\push\diamonds-in-depth-analysis.py > .\push\pushreal\diamonds-in-depth-analysis2.py )
#tailer.head(open() -n -9 .\push\diamonds-in-depth-analysis.py > .\push\pushreal\diamonds-in-depth-analysis2.py )


# ## Delete last lines from de python file 

# In[66]:


readFile = open(".\push\pushreal\diamonds-in-depth-analysis2.py")

lines = readFile.readlines()

readFile.close()
w = open(".\push\pushreal\diamonds-in-depth-analysis2.py",'w')
w.writelines([item for item in lines[:-40]])
w.close()


# ### Moet 2 keer omdat hij anders niet update.

# In[ ]:


get_ipython().system('git -C ./push/pushreal commit -am "Nieuw commit" | git -C ./push/pushreal push heroku master')


# In[ ]:


#!git -C ./push/pushreal commit -am "Nieuw commit" | git -C ./push/pushreal push heroku master

