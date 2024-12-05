from app.database import SessionLocal
from app.models import Profile

def seed_data():
    db = SessionLocal()
    profiles = [
        Profile(name="John Doe", age=25, bio="Enjoys hiking and outdoor activities."),
        Profile(name="Jane Smith", age=30, bio="Loves art and painting."),
        Profile(name="Alex Brown", age=28, bio="Tech enthusiast and coder."),
        Profile(name="Emily Carter", age=26, bio="Passionate about cooking and trying new recipes."),
        Profile(name="Sophia Martinez", age=29, bio="Enjoys yoga and traveling to exotic destinations."),
        Profile(name="Olivia Johnson", age=24, bio="Avid reader and aspiring novelist."),
        Profile(name="Ava Williams", age=27, bio="Loves photography and exploring nature."),
        Profile(name="Isabella Davis", age=31, bio="Enjoys gardening and volunteering in the community."),
        Profile(name="Mia Anderson", age=28, bio="Fitness enthusiast and marathon runner."),
        Profile(name="Charlotte Wilson", age=25, bio="Art lover who spends weekends at galleries."),
        Profile(name="Amelia Thompson", age=30, bio="Enjoys knitting and designing handmade crafts."),
        Profile(name="Harper Lewis", age=26, bio="Loves dancing and attending live music events."),
        Profile(name="Evelyn Hall", age=29, bio="Tech geek with a passion for coding and robotics.")
    ]
    db.add_all(profiles)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
    print("Test data seeded!")