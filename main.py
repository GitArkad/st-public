import streamlit as st

st.title("Калькулятор")

val_1 = st.number_input("Insert number 1:", key="val_1")
val_2 = st.number_input("Insert number 2:", key="val_2")

st.write(f"Результат = {val_1 + val_2}")

