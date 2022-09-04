import streamlit as st
import plotly.express as px
import pandas as pd
from firebase import Firebase

firebase = Firebase()
sentiments = firebase.getSentimentsFromDB()
print(type(sentiments))

st.title("User sentiments for Companies")
st.subheader(
    "A representation of the sentiments of Twitter user about some popular companies."
)


df = pd.DataFrame.from_dict(sentiments)
df = df.reset_index()
df = df.rename(columns={"index": "sentiments"})
print(df)
print(df.index)
fig = px.bar(df, x=df.sentiments, y=df.columns, barmode="group")


st.plotly_chart(
    figure_or_data=fig,
)
