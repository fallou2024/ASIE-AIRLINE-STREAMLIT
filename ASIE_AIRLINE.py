import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import streamlit as st


from os import sep
st.title(" Indian Domestic Airline Data Analysis")
path=("Indian_Domestic_Airline.xlsx")
df=pd.read_excel(path)
#df.head()
st.dataframe(df)

#l'information du base de donnees
df.info()

#une analyse descriptive
df.describe()

#the tail
df.tail()

#le nombre de ligne et colonne
df.shape

#les diferrents types dans la base de donnees
df.dtypes

#les valeurs manquantes
df.isnull().sum()
import matplotlib.pyplot as plt
import seaborn as sns

# Group data by airline and calculate the average rating
airline_ratings = df.groupby('AirLine_Name')['Rating - 10'].mean()

# Create a bar plot of average ratings
plt.figure(figsize=(10, 6))
fig = plt.bar(airline_ratings.index, airline_ratings.values)
plt.xlabel('Airline Name')
plt.ylabel('Average Rating')
plt.title('Average Airline Ratings')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

#plt.show()
st.pyplot(plt.gcf()) # instead of plt.show()
st.write("Donc ici on a la moyenne de notation  (Average Rating) des differents compagnies aeriens.On constate que 'Go First' a plus petite note avec une moyenne de notation de 1,7 et 'Vistara' a plus grande moyenne de notation 6,8. Les autres compagnies comme 'Air India Express, AirAsie India,Spicejet' tourne autour d'une moyenne de 2 et 'Indigo' qui a une de 5,8.")


# Create the histogram of the rating mean
plt.figure(figsize=(10,6))
df["Rating - 10"].plot(kind="hist", title="Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
#plt.show()

st.pyplot(plt.gcf()) # instead of plt.show()
st.write("on constate que la frequence de notation moyenne est eleve entre  1 et 2 avec une freauence de 1000 et une dimninution apres le 2 jusqu'a 8 et une legere augmentation apres le 8.")

#the recommondation
df.groupby('Recommond').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
#plt.show()
st.pyplot(plt.gcf()) # instead of plt.show()
st.write("on constate ici il y'a moins de recommandation avec une frequence de 1400 avec le 'NO' contre '700' pour le 'Yes'.")

#la frequence de recommandation avec les compagnies aeriens
df.groupby('AirLine_Name')['Recommond'].value_counts().unstack().plot(kind='bar', stacked=True)
plt.gca().spines[['top', 'right',]].set_visible(False)
#plt.show
st.pyplot(plt.gcf()) # instead of plt.show()
st.write("on constate ici que seul la compagnie 'Vistara' a plus de frequence de recommandation 'Yes' depassant le'No' et Indigo et a moitie egal entre Yes' et 'No' mais tout les autres compagnies n'ont une  pas beuacoup de recommandation les frenquence de 'NO' dominant sur le 'yes', ")

import streamlit as st
import streamlit_option_menu
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar:
   selected = option_menu("Main Menu", ["code","graphique","texte"],
icons=["app","flight","letters"])

   
if selected=="graphique":
    st.subheader("# Create a bar plot of average ratings")
    plt.figure(figsize=(10, 6))
    fig = plt.bar(airline_ratings.index, airline_ratings.values)
    plt.xlabel('Airline Name')
    plt.ylabel('Average Rating')
    plt.title('Average Airline Ratings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    #plt.show()
    st.pyplot(plt.gcf()) # instead of plt.show()

    st.subheader("# Create the histogram of the rating mean")
    plt.figure(figsize=(10,6))
    df["Rating - 10"].plot(kind="hist", title="Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency") 
    #plt.show()
    st.pyplot(plt.gcf()) # instead of plt.show()

    #the recommondation
    st.subheader
    df.groupby('Recommond').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
    plt.gca().spines[['top', 'right',]].set_visible(False)
    st.pyplot(plt.gcf()) # instead of plt.show()

    #la frequence de recommandation avec les compagnies aeriens
    st.subheader
    df.groupby('AirLine_Name')['Recommond'].value_counts().unstack().plot(kind='bar', stacked=True)
    plt.gca().spines[['top', 'right',]].set_visible(False)
    #plt.show
    st.pyplot(plt.gcf()) # instead of plt.show()

if selected=="code":
    st.write("# Create a bar plot of average ratings")
    plt.figure(figsize=(10, 6))
    fig = plt.bar(airline_ratings.index, airline_ratings.values)
    plt.xlabel('Airline Name')
    plt.ylabel('Average Rating')
    plt.title('Average Airline Ratings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    #plt.show()
    st.pyplot(plt.gcf()) # instead of plt.show() 



    
if selected=="texte":
    st.write( "Donc ici on a la moyenne de notation 'Average Rating' des differents compagnies aeriens.On constate que 'Go First' a plus petite note avec une moyenne de notation de 1,7 et 'Vistara' a plus grande moyenne de notation 6,8. Les autres compagnies comme 'Air India Express', 'AirAsie India','Spicejet' tourne autour d'une moyenne de 2 et 'Indigo' qui a une de 5,8")    
    st.write("on constate que la frequence de notation moyenne est eleve entre 1 et 2 avec une frequence de 1000 et une dimninution apres le 2 jusqu'a 8 et une legere augmentation apres le 8.")
    st.write("on constate ici il y'a moins de recommandation avec une frequence de 1400 avec le 'NO' contre '700' pour le 'Yes'.")
    st.write("on constate ici que seul la compagnie 'Vistara' a plus de frequence de recommandation 'Yes' depassant le'No' et Indigo et a moitie egal entre Yes' et 'No' mais tout les autres compagnies n'ont une pas beuacoup de recommandation les frenquence de 'NO' dominant sur le 'yes',")  
