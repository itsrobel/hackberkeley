from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from agents.ManagerAgent import *
from agents.chatbot import *
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route("/realtime")
def realtime():
    return render_template("time_heatmap.html")


@app.route("/overlay")
def overlay():
    return render_template("demo_colormap.html")


@app.route("/temp")
def demo():
    return render_template("demo.html")


@app.route("/llm_call")
def llm():
    message = request.args.get('message')
    res = example()
    print(res)
    # [{'agent' : ..., 'message', ...}, {...}, ...]
    return jsonify(res)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
