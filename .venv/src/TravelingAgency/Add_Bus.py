import json
import os

def login(func):
    def wrapper(*args, **kwargs):
        print("------------------------Login to add bus------------------------")
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
def Add_Bus():
    print("------------------------Add new bus------------------------")
    name = input("Enter your bus name: ").strip()
    while name.isdigit():
        name = input("Enter your valid bus name: ").strip()
    capacity=input("Enter number of seats: ").strip()
    while not capacity.isdigit():
        capacity = input("Enter number correct number of seats: ").strip()
    capacity=int(capacity)
    valid_classes = ['economy', 'first', 'business']
    bus_class = input("Enter bus class (Economy, First, Business): ").strip().lower()
    while bus_class not in valid_classes:
        bus_class = input("Enter bus class correctly (Economy, First, Business): ").strip().lower()
    new_bus = {
        "name": name,
        "capacity": capacity,
        "class": bus_class.capitalize()
    }
    file_path = "buses.json"
    # Read existing data
    if os.path.exists(file_path):
        rf= open(file_path, "r")
        try:
          buses = json.load(rf)
        except json.JSONDecodeError:
          buses = []
    else:
        buses = []
    # Write updated list back to the file
    buses.append(new_bus)
    wf=open(file_path, "w")
    x=json.dump(buses, wf, indent=4)
    wf.close()
    print("------------------------Bus added successfully------------------------")
    print(f"Bus Name: {name}")
    print(f"Number of Seats: {capacity}")
    print(f"Bus Class: {bus_class.capitalize()}")



