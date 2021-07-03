import datetime
import io

from PIL import Image
import pytz
import requests
import streamlit as st

TOKEN = st.secrets['YOUR_TOKEN']
api_url = 'https://notify-api.line.me/api/notify'

st.title('LINE通知アプリ')
txt_msg = st.text_input('LINEに送信したいメッセージを入力してください。')
img_file = st.file_uploader('LINEに送信画像ファイルをアップロードしてください。（対応ファイル形式：.png、.jpg）')
send_click = st.button('LINEへ送付')

if send_click:
    # パラメーター設定
    time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    time = time.strftime('%Y年%m月%d日 %H:%M:%S')
    send_contents = f'[{time}]\n{txt_msg}'
    img = Image.open(img_file)
    with io.BytesIO() as output:
        img.save(output, format='JPEG')
        binary_img = output.getvalue()
    TOKEN_dic = {
        'Authorization': 'Bearer' + ' ' + TOKEN
    }
    send_dic = {
        'message': send_contents
    }
    image_dic = {'imageFile': binary_img}

    # メッセージ送信
    requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
    st.success('LINEへの通知が完了しました。')
    st.write(send_contents)
    st.image(
        img, caption='送信画像',
        use_column_width=True
    )