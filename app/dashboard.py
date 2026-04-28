import streamlit as st
import sqlite3
import pandas as pd

st.title("ML Batch Prediction Dashboard")

conn=sqlite3.connect("ml_pipeline.db")

preds = pd.read_sql(
"SELECT * FROM predictions",
conn
)

inputs = pd.read_sql(
"SELECT * FROM input_data",
conn
)

st.subheader("Input Data")
st.dataframe(inputs)

st.subheader("Predictions")
st.dataframe(preds)

st.metric(
"Total Predictions",
len(preds)
)

if len(preds)>0:
    st.subheader("Prediction Distribution")
    st.bar_chart(
       preds["prediction"].value_counts()
    )