import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


uploaded_file = st.file_uploader(
    'Load data CSV', 
    type=['csv']
)
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    dfs = {
        'male': df[df['customer_gender']=='male'], 
        'female': df[df['customer_gender']=='female']
        }
    
    for title, data in dfs.items():
        data.drop(columns=['customer_gender'], inplace=True)
        st.subheader(f'Data {title}')
        st.dataframe(data)

    st.subheader(f'Histogram male/customer_age')
    fig, ax = plt.subplots()
    ax.hist(dfs['male']['customer_age'])
    st.pyplot(fig)


    st.bar_chart(data=dfs['male'], x='country', y='customer_age')

    st.line_chart(data=dfs['female'][dfs['female']['revenue']> 500], x='customer_age', y='revenue')

    st.scatter_chart(data=dfs['female'][dfs['female']['revenue']> 500], x='customer_age', y='revenue')



    # st.subheader('Data male:')
    # st.dataframe(df)
    # st.subheader('Data male:')
    # st.dataframe(df)