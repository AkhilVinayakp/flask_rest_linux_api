from users import Users
from werkzeug.security import safe_str_cmp
users = [
    Users(2, 'ravi', 'ravi')
]
# creating mapping for user name and the elements in the list of users
user_name_mapping = {u.name: u for u in users}
# creating mapping for the user id and the elements in the list of the users
user_id_mapping = {u.uid: u for u in users}


# user name password cross check
def authenticate(name, password):
    user = user_name_mapping.get(name, None)  # searching the index for suitable match of the object
    if user and safe_str_cmp(user.password, password):
        return user  # returning the object that we got a proper match


# cross checking of token and identify the proper user via token provided
def identity(payload):  # payload holds the jwt data
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)
