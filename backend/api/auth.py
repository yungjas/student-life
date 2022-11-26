from flask import request, jsonify, Blueprint
from model.User import User
from config import db, bcrypt

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/api/register", methods=["POST"])
def register():
    # get the post data
    post_data = request.get_json()
    print(f"email: {post_data.get('email')}")
    print(f"password: {post_data.get('password')}" )
    # check if user already exists
    user = User.query.filter_by(email=post_data.get('email')).first()
    if not user:
        try:
            user = User(email=post_data.get('email'), password=post_data.get('password'))
            # insert the user
            db.session.add(user)
            db.session.commit()
            
            # generate the auth token
            auth_token = user.encode_auth_token(user.user_id)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            
            return jsonify(responseObject), 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': e
            }
            return jsonify(responseObject), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return jsonify(responseObject), 202


@auth_blueprint.route("/api/login", methods=["POST"])
def login():
    # get the post data
    post_data = request.get_json()
    try:
        # fetch the user data
        user = User.query.filter_by(email=post_data.get('email')).first()
        if user and bcrypt.check_password_hash(
            user.password, post_data.get('password')
        ):
            auth_token = user.encode_auth_token(user.user_id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return jsonify(responseObject), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return jsonify(responseObject), 404
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': e
        }
        return jsonify(responseObject), 500