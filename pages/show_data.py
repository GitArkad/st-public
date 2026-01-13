import streamlit as st
import pandas as pd
from pages.load_data import uploaded_file

st.title('Show data')

# # Проверяем, загружен ли файл
# if 'uploaded_file' in st.session_state:
#     uploaded_file = st.session_state.uploaded_file
#     df = pd.read_csv(uploaded_file)
    
#     # Разделяем по полу
#     dfs = {
#         'male': df[df['customer_gender'] == 'male'],
#         'female': df[df['customer_gender'] == 'female']
#     }

#     for title, data in dfs.items():
#         data.drop(columns=['customer_gender'], inplace=True)
#         st.subheader(f'Data {title}')
#         st.dataframe(data)
# else:
#     st.info("Сначала загрузите данные на странице 'Load Data'.")