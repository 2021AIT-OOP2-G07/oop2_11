import os
from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/
# HTMLを返す
@app.route('/')
def index():
    return render_template("web.html")

# アップロード
@app.route('/', methods=["POST"])
def upload_file():
    print("post")
    if request.method == 'POST':
        if 'file' not in request.files:
            print('no file')
            return render_template("web.html")
        file = request.files['file']
        if file.filename == '':
            print('no filename')
            return
        if file:
            print('exist file')
            filename = file.filename
            file.save(os.path.join('img/original', filename))
            return  render_template("web.html")
    return render_template("web.html")

def upload():
    print("posted")

    if 'file' not in request.files:
        return render_template("web.html")

    # fileの取得（FileStorage型で取れる）
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    fs = request.files['file']

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    fs.save('static/img/original/' + fs.filename)

    
    return render_template("web.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)