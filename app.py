from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
from redis import Redis
import os
load_dotenv()
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

redis_client = Redis(
    host='redis-18856.c124.us-central1-1.gce.redns.redis-cloud.com',
    port=18856,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Integer, nullable=False)

def update_leaderboard(restaurant_id, sentiment_score):
    redis_client.zincrby("restaurant_leaderboard", sentiment_score, restaurant_id)

def seed_restaurants():
    if Restaurant.query.count() == 0:
        dummy_data = [
            Restaurant(name="Pasta Heaven"),
            Restaurant(name="Burger King"),
            Restaurant(name="Sushi World")
        ]
        db.session.bulk_save_objects(dummy_data)
        db.session.commit()
with app.app_context():
    db.create_all() 
    seed_restaurants()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    return 1 if score >= 0 else -1

@app.route('/add_review', methods=['POST'])
def add_review():
    data = request.json
    restaurant_id = data.get('restaurant_id')
    review_text = data.get('review_text')

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    sentiment = analyze_sentiment(review_text)
    print(sentiment) 

    new_review = Review(restaurant_id=restaurant_id, review_text=review_text, sentiment=sentiment)
    db.session.add(new_review)
    db.session.commit()
    update_leaderboard(restaurant_id, sentiment)
    return jsonify({'message': 'Review added successfully', 'sentiment': sentiment}), 201


@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    top_restaurants = redis_client.zrevrange("restaurant_leaderboard", 0, 9, withscores=True)
    leaderboard = []

    for restaurant_id, score in top_restaurants:
        restaurant = Restaurant.query.get(int(restaurant_id))
        if restaurant:
            leaderboard.append({"restaurant_name": restaurant.name, "score": score})

    return jsonify({"leaderboard": leaderboard})

if __name__ == '__main__':
    app.run(debug=True)
