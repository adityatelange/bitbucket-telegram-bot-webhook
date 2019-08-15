from flask import Flask, request

from EventHandler import event_handler

application = Flask(__name__)


@application.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return '.'


# could also use the POST body instead of query string: http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
@application.route('/bitbucket', methods=['POST', 'GET'])
def post_bitbucket():
    if request.method == 'POST':
        event_handler(x_event_key=request.headers.get('X-Event-Key'), data_json=request.json)
        return 'OK'
    elif request.method == 'GET':
        return '.'


# listen for requests :)
if __name__ == "__main__":
    from os import environ

    application.run(host='0.0.0.0', port=int(environ['PORT']))
