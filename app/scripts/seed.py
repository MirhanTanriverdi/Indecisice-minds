# from app.app import create_ap
from app.models import Idea
from app.extensions.database import db

# if __name__ == '__main__':
#     app = create_app()
#     app.app_context().push()


good_website_ideas = [
    'A platform for learning and practicing programming languages through interactive exercises',
    'A community-driven marketplace for homemade and handcrafted goods',
    'A subscription service for curated monthly book recommendations',
    'A platform for connecting freelance professionals with potential clients',
    'A language learning app with conversation practice and native speaker tutors',
    'A niche social network for people who share a specific hobby or interest',
    'A website for sharing and discovering travel itineraries and experiences',
    'A tool for comparing and booking eco-friendly accommodations worldwide',
    'An online platform for organizing and participating in local sports leagues and tournaments',
    'A website for personalized meal planning and grocery shopping based on dietary preferences',
    'A platform for renting and sharing outdoor gear and equipment',
    'A website for discovering and supporting local independent businesses',
    'A virtual event platform for hosting and attending conferences, workshops, and meetups',
    'An online tool for creating and sharing digital mood boards and design inspiration',
    'A website for finding and adopting pets from shelters and rescue organizations',
    'A platform for connecting mentors and mentees in various professional fields',
    'An online resource for learning about sustainable living and eco-friendly practices',
    'A website for tracking and managing personal finance goals and expenses',
    'A platform for hosting and sharing user-generated educational content',
    'A website for discovering and supporting crowdfunding campaigns and projects'
]

def seeding():
    for item in good_website_ideas:
        idea = Idea(description=item)

        db.session.add(idea)

    db.session.commit()


