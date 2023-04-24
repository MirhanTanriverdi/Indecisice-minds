from app.app import create_app

app = create_app()

# def add_good_ideas():
#     with app.app_context():
#         idea_count = Idea.query.count()
#         if idea_count == 0:
#             for idea_text in good_website_ideas:
#                 idea = Idea(title=idea_text, description="")
#                 db.session.add(idea)
#             db.session.commit()
#             print("Good website ideas added to the database.")
#         else:
#             print("Ideas already in the database. Skipping.")


if __name__ == '__main__':
    # add_good_ideas()
    app.run(debug=True, port=8080)
