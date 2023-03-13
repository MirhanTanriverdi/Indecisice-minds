from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/brainstorming')
def brainstorming_tools():
    return render_template('brainstorming.html')