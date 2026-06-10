from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to Flask CI/CD App",
        "status": "running"
    })


@main.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@main.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    }), 200
