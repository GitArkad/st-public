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

if 'show_text' not in st.session_state:
    st.session_state.show_text = False


def show_handler():
    st.session_state.show_text = not st.session_state.show_text

st.button("**Click for get text**", on_click=show_handler)

if st.session_state.show_text:
    st.write('Hidden message!')