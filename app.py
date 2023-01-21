from flask import Flask, request, redirect, url_for ,render_template 
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload'

@app.route('/', methods=['GET', 'POST'])
def index():
    print(0)
    return render_template('index.html')
"""     if request.method == 'POST':
        print(1)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(2)
            return redirect(url_for('uploaded_file', filename=filename)) """


@app.route('/upload', methods=['POST'])
def upload():
    print(1)
    try:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('圖片已成功上傳')
            return '圖片已成功上傳'
        else:
            print('檔案格式不正確')
            return "檔案格式不正確"
    except Exception as e:
        print(e)
        print('發生未知錯誤')
        return "發生未知錯誤"

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run()