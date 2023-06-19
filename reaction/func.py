from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:82PmVWUZSk@mariadb.mariadb.svc.cluster.local/my_database'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
migrate = Migrate(application, db)


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    emoji = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    team = db.Column(db.String(100), nullable=False, default='Your Team')



@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        emoji = request.form['emoji']
        timestamp = datetime.utcnow()

        new_rating = Rating(name=name, emoji=emoji, timestamp=timestamp)
        db.session.add(new_rating)
        db.session.commit()

    return render_template('index.html')



if __name__ == '__main__':
    application.run()
