from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from .serializers import UserSerializer, AccountSerializer
from .models import Account

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class SignupView(MethodView):
    def get(self):
        result = User.objects.all()
        all_users = UserSerializer(result, many=True)
        return jsonify(all_users.data)

    def post(self):
        data = request.json
        username = data["username"]
        password = data["password"]
        re_password = data["re_password"]

        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return jsonify({"error": "Username already exists"})
                else:
                    user = User(username=username, password=bcrypt.generate_password_hash(password))
                    user.save()
                    account = Account(user=user, username=username)
                    account.save()
                    access_token = create_access_token(identity=str(user.id))
                    return jsonify({
                        "success": "User created successfully",
                        "token": access_token
                    })
            else:
                return jsonify({"error": "Passwords do not match"})
        except:
            return jsonify({"error": "Something went wrong signing up"})

class LoginView(MethodView):
    def post(self):
        data = request.json
        username = data["username"]
        password = data["password"]

        try:
            user = User.objects.get(username=username)
            if bcrypt.check_password_hash(user.password, password):
                access_token = create_access_token(identity=str(user.id))
                return jsonify({
                    "success": "User authenticated",
                    "token": access_token
                })
            else:
                return jsonify({"error": "Error authenticating"})
        except:
            return jsonify({"error": "Something went wrong when logging in"})

class GrabProfile(MethodView):
    @jwt_required()
    def get(self):
        try:
            user_id = get_jwt_identity()
            user = User.objects.get(id=user_id)
            profile = Account.objects.get(user=user)
            profile_json = AccountSerializer(profile)
            return jsonify({"profile": profile_json.data})
        except:
            return jsonify({"error": "No user profile found"})

# Routes
signup_view = SignupView.as_view('signup_view')
login_view = LoginView.as_view('login_view')
grab_profile = GrabProfile.as_view('grab_profile')

app.add_url_rule('/signup', view_func=signup_view, methods=['POST'])
app.add_url_rule('/login', view_func=login_view, methods=['POST'])
app.add_url_rule('/profile', view_func=grab_profile, methods=['GET'])

if __name__ == '__main__':
    app.run()
