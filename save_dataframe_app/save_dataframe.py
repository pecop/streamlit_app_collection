import base64
import os

import streamlit as st
import pandas as pd

st.title('データファイルダウンロード')

# Table
st.write('データフレーム')

df = pd.DataFrame({
    '値': [1, 2, 3],
    '色': ['red', 'white', 'blue']
    })

st.write(df)
if st.button('ダウンロードリンクを生成'):
    object_to_download = df.to_csv(index=False, encoding='utf_8_sig')
    # st.write(object_to_download)
    b64 = base64.b64encode(object_to_download.encode('UTF-8')).decode()
    # b64 = base64.b64encode(object_to_download.encode()).decode()
    tmp_download_link = f'<a href="data:file/csv;base64,{b64}" download="downloaded-data.csv">Download csv file</a>'
    st.markdown(tmp_download_link, unsafe_allow_html=True)