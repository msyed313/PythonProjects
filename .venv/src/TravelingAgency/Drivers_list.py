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
def Drivers_list():
    print("------------------------Drivers Details------------------------")
    for index,driver in enumerate(drivers):
        index = index + 1
        print(f"------------------------Driver {index}------------------------")
        for key, value in driver.items():
            print(f"{key} => {value}")