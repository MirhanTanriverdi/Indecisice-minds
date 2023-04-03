from flask import Flask, render_template, redirect, url_for, request
import random


app = Flask(__name__)

app.config.from_object('app.config')

# Idea dixtionary
idea_gen = [
    'An online marketplace for local artists to sell their art',
    'A recipe sharing and meal planning website',
    'A platform for booking and managing vacation rentals',
    'A job search engine for remote work opportunities',
    'A news aggregator with a personalized feed based on user interests',
    'A platform for connecting volunteers with local non-profits',
    'An online course marketplace for learning new skills',
    'A social network for pet owners to connect and share advice',
    'A platform for booking and managing appointments with health practitioners',
    'A website for buying and selling secondhand clothing'
]


# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Idea generator page
@app.route('/idea-gen', methods=['GET', 'POST'])
def idea_generator():
    idea = None
    if request.method == "POST":
        idea = random.choice(idea_gen)
    return render_template('idea-gen.html', idea=idea)

# Brainstorming tools page
@app.route('/brainstorming-tools')
def brainstorming_tools():
    return render_template('brain.html')


