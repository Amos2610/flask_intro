from flask import Flask, render_template

# アプリケーションのインスタンスを作成
app = Flask(__name__)

bullets = [
    "箇条書き1",
    "箇条書き2",
    "箇条書き3",
    "箇条書き4",
    "箇条書き5",
    "箇条書き6",
    "箇条書き7",
    "箇条書き8",
    "箇条書き9",
]


# ルーティングの設定
@app.route("/")
def hello():
    return render_template("hello.html", bullets=bullets)


# 可変ルーティング
# @app.route("/japan/<city>")
# def japan(city):
#     return f"Hello, { city } in japan!"
