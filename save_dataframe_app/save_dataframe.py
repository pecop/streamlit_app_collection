import streamlit as st
import pandas as pd
import os

st.title('Streamlit　Basics')
# st.sidebar.title('Streamlit　Basics')

# Table
st.write('DataFrame')

df = pd.DataFrame({
	'column１': [1, 2, 3, 4],
	'column 2': [10, 20, 30, 40]
	})

df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']})

st.write(df)
if st.button('save dataframe'):
    directory_path = os.getcwd()
    file_name = 'df.csv'
    # file_name = 'df.xlsx'
    file_path = os.path.join(directory_path, file_name)
    st.write(f'ファイル保存先：{file_path}')
    # open(file_path, 'w').write(df.to_csv())
    df.to_csv(file_path)
    # df.to_excel(file_path)