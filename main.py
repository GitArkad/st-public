import streamlit as st

st.title("Congratulations!!")

# val_1 = st.number_input("Insert number 1:", key="val_1")
# val_2 = st.number_input("Insert number 2:", key="val_2")

# st.write(f"Результат = {val_1 + val_2}")

first_name = st.text_input("Input first_name:", key="first_name")
last_name = st.text_input("Input last_name:", key="last_name")

if first_name == '' and last_name == '':
    message = 'Hello!'
else:

    message = f"Hello, {first_name} {last_name}!"

st.write(message)

show_text = st.button('Click fot text')

if show_text:
    st.write('Hidden message!')