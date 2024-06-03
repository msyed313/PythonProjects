import json
import os
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
    print("------------------------Add driver------------------------")
    name=input("Enter driver name: ").strip()
    while name.isdigit():
        name = input("Enter driver name correctly: ").strip()
    age = input("Enter driver age: ").strip()
    while not age.isdigit() or not int(age)>=18:
        age = input("Enter driver age correctly: ").strip()
    age=int(age)
    exp = input("Enter driver experience(must be 2yrs): ").strip()
    while not exp.isdigit() or not int(exp)>=2:
        exp = input("Enter driver experience correctly(must be 2yrs): ").strip()
    exp=int(exp)
    phone=input("Enter contact number: ").strip()
    while not phone.isdigit() or len(phone)<11:
        phone = input("Enter contact number correctly: ").strip()

    file_name="drivers.json"
    driver={
        "name":name,
        "age":age,
        "experience":f"{exp} yrs",
        "contact":phone
    }
    if os.path.exists(file_name):
        rf=open(file_name,"r")
        try:
            drivers=json.load(rf)
        except json.JSONDecodeError:
            drivers=[]
    else:
        drivers=[]
    drivers.append(driver)
    wf=open(file_name,"w")
    x=json.dump(drivers,wf,indent=4)
    wf.close()
    print("------------------------Driver added successfully------------------------")
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"experience: {exp}")
    print(f"contact: {phone}")