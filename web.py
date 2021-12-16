from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/
# HTMLを返す
@app.route('/')
def index():
    return render_template("upload.html")
    

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)