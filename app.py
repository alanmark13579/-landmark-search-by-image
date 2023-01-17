from flask import Flask, request, render_template, send_file 
from PIL import Image
from io import BytesIO
import google.cloud.logging
import logging
import os

#建立GCP logging api
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"./.credentials\client_secret.json"
client = google.cloud.logging.Client()
client.setup_logging()

app  = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    # 如果是 POST 請求，則回傳使用者輸入的訊息
    if request.method == 'POST':
        return request.form['message']
    # 否則回傳網頁
    return render_template('index.html')

@app.route('/send_imgLW', methods=['POST'])
def send_imgHL():

    if request.method == 'POST':
        
        # 回傳使用者輸入的訊息(width、length、color)
        width = int(request.form['width'])
        length = int(request.form['length'])
        color = request.form['color-type']
       
        # 建立空白圖片
        image = Image.new('RGB', (width, length), color)

        # 將圖片轉成二進位資料
        image_bytes = BytesIO()
        image.save(image_bytes, format='png')
        image_bytes.seek(0)

        # 回傳圖片
        return send_file(
            image_bytes,
            mimetype='image/png'
        )


if __name__ == '__main__':
    app.run(debug=True)