import json
import os
def login(func):
    def wrapper(*args, **kwargs):
        print("------------------------Login to see drivers list------------------------")
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
def show_drivers():
    print("------------------------Drivers Details------------------------")
    file_path="drivers.json"
    if not os.path.exists(file_path):
        print("No driver found")
        return
    rf=open(file_path,"r")
    try:
      drivers=json.load(rf)
    except json.JSONDecodeError:
        print("Error reading drivers data.")
        return
    if not drivers:
        print("No driver found.")
        return

    print("------------------------List of Drivers------------------------")
    for i, driver in enumerate(drivers, 1):
        print(f"Driver {i}:")
        print(f"  Name: {driver['name']}")
        print(f"  Age: {driver['age']}")
        print(f"  Experience: {driver['experience']}")
        print(f"  Contact: {driver['contact']}")

        print("-----------------------------------------------------------")

