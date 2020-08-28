import logging
from models import User
from flask import Flask,jsonify,render_template,make_response,request,session,redirect,url_for
import uuid
import datetime
from functools import wraps


logger = logging.getLogger("default")



def index():
    logger.info("Checking the flask scaffolding logger")
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('auth_token') is None:
            current_user = User.objects.filter(username=request.authorization.username).first()
            # return redirect(url_for('login', next=request.url))
        return f(current_user, *args, **kwargs)

    return decorated_function



@login_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.objects()

    output = []

    for user in users:
        user_data = {}
        # user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['first_name'] = user.first_name
        user_data['last_name'] = user.last_name
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        output.append(user_data)

    return jsonify({'users' : output})


@login_required
def get_one_user(current_user,username):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.objects.filter(username=username).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user_data = {}
    # user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user' : user_data})


@login_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    data = request.get_json()

    password = data['password']

    new_user = User(username=data["username"],first_name=data['first_name'],last_name=data['last_name'],email=data['email'],password=password)
    new_user.validate(clean='clean')
    new_user.save()
    return jsonify({'message' : 'New user created!'})


@login_required
def update_user(current_user,username):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.objects.filter(username=username).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.admin = True
    user.validate(clean='clean')
    user.save()

    return jsonify({'message' : 'The user has been promoted!'})


@login_required
def delete_user(current_user,username):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.objects.filter(username=username).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.delete()

    return jsonify({'message' : 'The user has been deleted!'})


def login():
    auth = request.authorization

    if auth and auth.username=="DX9807" and auth.password=="123425578":
        return jsonify({'User' : auth.username})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
