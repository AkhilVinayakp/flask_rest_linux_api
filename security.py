from users import Users
users = [
    Users(1, 'bob', 'bob123')
]
# creating mapping for user name and the elements in the list of users
user_name_mapping = {u.name: u for u in users}
# creating mapping for the user id and the elements in the list of the users
user_id_mapping = {u.uid: u for u in users}

# user name password cross check
def authenticat(name, passwword):
    user_name = user_name_mapping.get(name, None)