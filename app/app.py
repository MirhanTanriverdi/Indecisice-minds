from flask import Flask, render_template, Blueprint, redirect, url_for, request, flash
import random
from app.extensions.database import db, migrate
from app.scripts.seed import seeding

from .models import Idea, User

def create_app():

    app = Flask(__name__)
    app.config.from_object("app.config")

    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    migrate.init_app(app, db, compare_type=True)

    # Home page
    @app.route('/')
    def index():
        return render_template('index.html')

    idea_gen_bp = Blueprint('idea_gen', __name__, template_folder='templates')

    @idea_gen_bp.route('/idea-gen', methods=['GET', 'POST'])
    def idea_generator():
        ideas = []
        if request.method == "POST":
            idea = request.form.get('description')
            new_idea = Idea(description=idea)
        
            db.session.add(new_idea)
            db.session.commit()
        elif request.method == 'GET':
            ideas = Idea.query.all() 
            ideas = random.sample(ideas, min(1, len(ideas)))

        return render_template('idea-gen.html', ideas=ideas)


    @idea_gen_bp.route('/idea-gen-delete', methods=['GET', 'POST'])
    def delete_idea():
        if request.method == "POST":
            id = request.form.get("idea_id")
            idea = Idea.query.filter_by(id=id).first()
            db.session.delete(idea)
            db.session.commit()
            
        return redirect(url_for('idea_gen.idea_generator'))

    @idea_gen_bp.route('/idea-gen-edit', methods=['GET', 'POST'])
    def edit_idea():
        if request.method == "POST":
            id = request.form.get("idea_id")
            idea = Idea.query.filter_by(id=id).first()
            idea.description = request.form.get("description")
            
            db.session.add(idea)
            db.session.commit()
            
        return redirect(url_for('idea_gen.idea_generator'))

    app.register_blueprint(idea_gen_bp)

    @app.route('/idea-list', methods=['GET'])
    def idea_list_2():
        ideas = Idea.query.all()
        return render_template('idea-list.html', ideas=ideas)

    # Brainstorming tools page
    @app.route('/brainstorming-tools')
    def brainstorming_tools():
        return render_template('brain.html')

    # Route to display a specific idea based on its ID
    @app.route('/idea-list/<int:idea_id>')
    def idea_detail(idea_id):
        print(idea_id)
        idea = Idea.query.filter_by(id=idea_id).first()
        return render_template('ideas_detail.html', idea=idea)

    @app.route('/run-seed')
    def run_seed():
        seeding()
        return "Ran seed"

    return app
