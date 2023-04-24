from app.app import create_app
from app.models import db, Idea


app = create_app()
app.app_context().push()

ideas = Idea.query.all()

for idea in ideas:
    print(f"Idea: {idea.title}")
    print(f"Description: {idea.description}")
