from bcrypt import gensalt, hashpw

# Mock users table, in lieu of a DB. Obviously not acceptable for production but useful for demo purposes.
users = {}

def create_user(form):
    username = form.username.data
    password = form.password.data
    # In reality, this would be a DB call
    if (username in users):
        # TODO: this should be done at the form validation step...
        return (f"{username} already exists", 409)
    # Salt and hash the password
    password_encoded = password.encode("UTF-8")
    password_salt = gensalt()
    password_hashed = hashpw(password_encoded, password_salt)
    # Mock DB persistence
    users[username] = {
        "password": password_hashed,
    }
    return users[username]

def is_valid_user(username):
    return username in users