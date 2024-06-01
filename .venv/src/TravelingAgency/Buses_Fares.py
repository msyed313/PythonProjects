busesfare=[
    {
      "class":"First",
      "price":2500,
      "route":"Karachi-Lahore"
    },
    {
        "class":"Economy",
        "price":5000,
        "route":"Karachi-Lahore"
    },
    {
        "class":"Business",
        "price":7500,
        "route":"Karachi-Lahore"
    }
]
def Buses_Fares():
    print("------------------------Buses Fares Details------------------------")
    for index,bus in enumerate(busesfare):
        index=index+1
        print(f"------------------------Bus no  {index}------------------------")
        for key,value in bus.items():
            print(f"{key} => {value}")