drivers=[
    {
      "name":"Syed Mohsin Ali Shah",
      "age":25,
      "experience":"3 yrs",
      "phone":'03155126260'
    },
    {
        "name":"Shoaib Ahmed",
        "age":31,
        "experience":"5 yrs",
        "phone":'03135124360'
    }
]
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
def Drivers_list():
    print("------------------------Drivers Details------------------------")
    for index,driver in enumerate(drivers):
        index = index + 1
        print(f"------------------------Driver {index}------------------------")
        for key, value in driver.items():
            print(f"{key} => {value}")