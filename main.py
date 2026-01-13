import streamlit as st

st.title("Congratulations!!")

# val_1 = st.number_input("Insert number 1:", key="val_1")
# val_2 = st.number_input("Insert number 2:", key="val_2")

# st.write(f"Результат = {val_1 + val_2}")

first_name = st.text_input("Input first_name:", key="first_name")
last_name = st.text_input("Input last_name:", key="last_name")

st.write(f"Hello, {first_name} {last_name}!")