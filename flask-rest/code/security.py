from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'admin', 'admin'),
    User(2, 'bob', '1234')
]

usernmae_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = usernmae_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(pyload):
    user_id = pyload["identity"]
    return userid_mapping.get(user_id, None)
