import json
import os
def login(func):
    def wrapper(*args, **kwargs):
        print("------------------------Login to see buses list------------------------")
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
def Show_Buses():
    file_path = "buses.json"

    if not os.path.exists(file_path):
        print("No buses found. Please add some buses first.")
        return

    with open(file_path, "r") as file:
        try:
            buses = json.load(file)
        except json.JSONDecodeError:
            print("Error reading bus data.")
            return

    if not buses:
        print("No buses found.")
        return

    print("------------------------List of Buses------------------------")
    for i, bus in enumerate(buses, 1):
        print(f"Bus {i}:")
        print(f"  Name: {bus['name']}")
        print(f"  Capacity: {bus['capacity']}")
        print(f"  Class: {bus['class']}")
        print("-----------------------------------------------------------")
