import awsgi
from flask import (Flask, jsonify)

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return jsonify(status=200, message='hello world')


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
