import streamlit as st

st.title("Medication name analyzer.")
st.write("This is a sample application.")

user_input = st.text_input("Medication name")

st.write(user_input)
