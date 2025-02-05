# Restaurant-Review-Platform-API-with-automatic-NLP-analysis
RESTful API, In-memory database (for live leaderboard), SQL, Natural Language Processing to auto-label positive and negative comments.

![Badge](https://img.shields.io/badge/python-3.8%2B-blue)
![Badge](https://img.shields.io/badge/flask-2.0%2B-green)
![Badge](https://img.shields.io/badge/redis-in--memory%20database-orange)
![Badge](https://img.shields.io/badge/nlp-natural%20language%20processing-purple)

A Flask-based API that allows users to submit restaurant reviews, automatically analyzes the sentiment of the reviews using NLP, and maintains a live leaderboard of restaurants based on their positive or negative scores. This project integrates RESTful API design, in-memory database (Redis) for real-time leaderboard updates, and NLP for sentiment analysis.

---

## About the Project

### Problem Solved
Managing and analyzing user-generated reviews for restaurants can be challenging, especially when trying to provide real-time insights. This project solves these challenges by:
1. **Review Submission**: Allowing users to submit reviews for specific restaurants.
2. **Sentiment Analysis**: Using NLP to automatically classify reviews as positive or negative.
3. **Live Leaderboard**: Maintaining a real-time leaderboard of restaurants based on their review scores using Redis.
4. **Efficient Data Storage**: Using Redis for fast leaderboard updates and SQL for persistent review storage.

---

## Features
- **Review Submission**: Users can submit reviews for restaurants, including a text review and a restaurant ID.
- **Sentiment Analysis**: Automatically analyzes the sentiment of reviews using NLP (e.g., positive or negative).
- **Live Leaderboard**: Displays a real-time leaderboard of restaurants ranked by their review scores.
- **RESTful API**: Provides endpoints for submitting reviews, fetching leaderboard data, and more.

---

## Technologies and Skills Used
- **Backend Framework**: Flask (Python)
- **Database**: SQL (e.g., MySQL, PostgreSQL) for persistent review storage
- **In-Memory Database**: Redis for real-time leaderboard updates
- **Natural Language Processing (NLP)**: Libraries like `TextBlob` or `spaCy` for sentiment analysis
- **Other Tools**: Git, Docker (optional for containerization)

---

## How It Works
1. **Review Submission**: Users submit reviews for restaurants via the API.
2. **Sentiment Analysis**: The API uses NLP to classify the review as positive or negative.
3. **Leaderboard Update**: The restaurant's score is updated in the Redis leaderboard based on the review sentiment.
4. **Leaderboard Query**: Users can query the leaderboard to see the top-ranked restaurants in real time.

---

## Steps to Clone and Run the Project

### Prerequisites
- Python 3.8+
- Redis server (locally or via Docker)
- SQL database (e.g., MySQL, PostgreSQL)
- NLP library (e.g., `TextBlob` or `spaCy`)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/restaurant-review-platform.git
cd restaurant-review-platform
```