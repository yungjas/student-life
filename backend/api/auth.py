from flask import request, jsonify, Blueprint
from model.User import User
from model.Blacklist import BlacklistToken
from config import db, bcrypt
from middleware.middleware import token_required

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
            # for some reason decode is working in docker but not when running app.py locally, current workaround for now
            if isinstance(auth_token, str):
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token
                }
            else:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
            return jsonify(responseObject), 200
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
            if isinstance(auth_token, str):
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token
                }
            else:
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


@auth_blueprint.route("/api/logout", methods=["POST"])
@token_required
def logout(current_user):
    # get auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        # decode the token
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(token=auth_token)
            try:
                # insert the token
                db.session.add(blacklist_token)
                db.session.commit()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged out.'
                }
                return jsonify(responseObject), 200
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': e
                }
                return jsonify(responseObject), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return jsonify(responseObject), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return jsonify(responseObject), 403
