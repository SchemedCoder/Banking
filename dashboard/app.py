import streamlit as st
import pandas as pd

st.title("🏦 Banking Audit Dashboard")

data = {
    "City": ["Delhi", "Mumbai", "Bangalore"],
    "Transactions": [120, 95, 80],
    "Suspicious": [2, 1, 5],
    "Total Amount": [2500000, 4200000, 9800000]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.bar_chart(df.set_index("City")["Transactions"])

st.bar_chart(df.set_index("City")["Suspicious"])

st.line_chart(df.set_index("City")["Total Amount"])
