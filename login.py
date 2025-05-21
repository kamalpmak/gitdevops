def login(username, password):
    users = {
        "user1": "pass1",
        "user2": "pass2",
        "user3": "pass3"
    }
    if username in users and users[username] == password:
        return True
    else:
        return False

username = input("Username: ")
password = input("Password: ")

if login(username, password):
    print("Login successful.")
else:
    print("Login failed.")
