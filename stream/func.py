from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:82PmVWUZSk@mariadb.mariadb.svc.cluster.local/my_database'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    emoji = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    team = db.Column(db.String(100), nullable=False, default='Your Team')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/ratings', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    ratings_data = [{'name': rating.name, 'emoji': rating.emoji, 'team': rating.team} for rating in ratings]
    return jsonify({'ratings': ratings_data})


def get_ratings():
    # Get ratings within the last 10 seconds
    time_threshold = datetime.utcnow() - timedelta(seconds=10)
    ratings = Rating.query.filter(Rating.timestamp >= time_threshold).all()
    ratings_data = [{'name': rating.name, 'emoji': rating.emoji, 'team': rating.team} for rating in ratings]
    return jsonify({'ratings': ratings_data})

@application.route('/health/readiness')
def readiness_check():
    # Perform any readiness checks here
    return jsonify({'status': 'ready'})

@application.route('/health/liveness')
def liveness_check():
    # Perform any liveness checks here
    return jsonify({'status': 'alive'})


if __name__ == '__main__':
    application.run()
