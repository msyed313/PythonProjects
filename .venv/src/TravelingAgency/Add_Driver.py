
def login(func):
    def wrapper(*args, **kwargs):
        print("------------------------Login to add driver------------------------")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        # You can replace these with your actual username and password
        valid_username = "admin"
        valid_password = "password123"
        if username == valid_username and password == valid_password:
            return func(*args, **kwargs)
        else:
            print("Access Denied: Invalid username or password")
    return wrapper
@login
def Add_Driver():
    print("Add driver")