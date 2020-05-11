from werkzeug.security import safe_str_cmp
from users import Users
users = [
    Users(1, 'GOPI', 'GOPI123')
]
# CREATING USER NAME MAPPING
# done via users find_by_name and find_by_id methods


def authenticate(name, password):
    user = Users.find_by_name(name)
    if user and safe_str_cmp(password, user.password):
        return user
    else:
        return "password mismatch"


def identity(payload):
    user_id = payload['identity']
    return Users.find_by_id(user_id)


