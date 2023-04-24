from app.models import db, Idea

def add_idea(description):
    try:
        idea = Idea(description=description)
        db.session.add(idea)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error adding idea to database: {e}")
        db.session.rollback()
        return False
