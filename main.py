from flask import Flask, jsonify, render_template
from flask_cors import CORS
from agents.ManagerAgent import *
from agents.chatbot import *
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route("/realtime")
def home():
    return render_template("time_heatmap.html")


@app.route("/overlay")
def demo():
    return render_template("demo_colormap.html")


@app.route("/llm_call")
def llm(data):
    res = example()
    # [{'agent' : ..., 'message', ...}, {...}, ...]
    return jsonify(res)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

