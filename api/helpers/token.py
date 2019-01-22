from flask import request, jsonify
import datetime
from config import Config
from functools import wraps
import jwt


secret_key = Config.SECRET_KEY

def generate_token(user_id, isAdmin=False):
    """Generate a token  """
    payload = {
        "userid": user_id,
        "isAdmin": isAdmin,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256").decode("utf-8")

    return token


def decode_token(token):
    """decode token  """
    decoded = jwt.decode(str(token), secret_key, algorithm="HS256")
    return decoded


def extract_token():
    """extract token  """
    authorizaton_header = request.headers.get("Authorization")
    if not authorizaton_header or "Bearer" not in authorizaton_header:
        return (
            jsonify({"error": "Bad authorization header", "status": 400}),
            400,
        )
    token = str(authorizaton_header).split(" ")[1]
    return token


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = None
        try:
            token = extract_token()
            decode_token(token)
            response = func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            response = (
                jsonify({"error": "Invalid Token, verification failed", "status": 401}),
                401,
            )
        except jwt.InvalidTokenError:
            response = (
                jsonify({"error": "invalid token message", "status": 401}),
                401,
            )
        return response

    return wrapper


def get_current_user_identity():
    return decode_token(extract_token())["userid"]


def get_current_user_role():
    return decode_token(extract_token())["isAdmin"]


def admin_required(func):
    """decorated function to admin token required  """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_current_user_role():
            return (
                jsonify(
                    {
                        "error": "Only Admin has access to this resource",
                        "status": 403,
                    }
                ),
                403,
            )
        return func(*args, **kwargs)

    return wrapper
