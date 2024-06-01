buses=[
    {
      "name":"ZK6890HG",
      "capacity":63,
      "class":"First"
    },
    {
        "name":"ZK6126HG",
        "capacity":40,
        "class":"Economy"
    },
    {
        "name":"E12PRO",
        "capacity":25,
        "class":"Business"
    }
]
def Buses_list():
    print("------------------------Buses Details------------------------")
    for index,bus in enumerate(buses):
        index=index+1
        print(f"------------------------Bus no  {index}------------------------")
        for key,value in bus.items():
            print(f"{key} => {value}")