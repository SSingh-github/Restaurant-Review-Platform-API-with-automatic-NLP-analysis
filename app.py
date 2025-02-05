from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()
    
    if not Restaurant.query.first():
        dummy_restaurants = [
            Restaurant(name='Pasta Palace'),
            Restaurant(name='Burger Haven'),
            Restaurant(name='Sushi Delight')
        ]
        db.session.add_all(dummy_restaurants)
        db.session.commit()

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    restaurant_id = data.get('restaurant_id')
    review_text = data.get('review_text')
    
    if not restaurant_id or not review_text:
        return jsonify({'error': 'Restaurant ID and review text are required'}), 400
    
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    new_review = Review(restaurant_id=restaurant_id, review_text=review_text)
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify({'message': 'Review submitted successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
