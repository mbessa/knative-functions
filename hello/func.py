from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return b'Hello Cloud Days!!'


if __name__ == '__main__':
    application.run()
