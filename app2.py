from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import sys
sys.path.append(".")
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata
#import ecommbot
app2 = Flask(__name__)

load_dotenv()

vstore=ingestdata("done")
chain=generation(vstore)

@app2.route("/")
def index():
    return render_template('chat.html')

@app2.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app2.run(host="0:0:0:0")