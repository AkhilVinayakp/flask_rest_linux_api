from werkzeug.security import safe_str_cmp
from users import Users
users = [
    Users(1, 'GOPI', 'GOPI123')
]
# CREATING USER NAME MAPPING
user_name_mapping = {u.name: u for u in users}
user_id_mapping = {u.id: u for u in users}


def authentication(name, password):
    user = user_name_mapping.get(name, None)
    if user and safe_str_cmp(password, user.password):
        return user
    else:
        return "password mismatch"


def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)


