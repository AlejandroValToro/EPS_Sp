from flask import Blueprint, request, jsonify
from app.utils.security import Security

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id')
    

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    token = Security.generate_jwt(user_id)
    return jsonify({'token': token})
