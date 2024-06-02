routes=["karachi-lahore","peshawar-karachi","lahore-peshawar",]
busclass=[
    {
        "route":"karachi-lahore",
        "class":"first",
        "price":2500
    },
    {
        "route":"karachi-lahore",
        "class":"Economy",
        "price":5000
    },
    {
        "route":"karachi-lahore",
        "class":"Business",
        "price":7500
    },
    {
        "route": "peshawar-karachi",
        "class": "First",
        "price": 2600
    },
    {
        "route": "peshawar-karachi",
        "class": "Economy",
        "price": 5100
    },
    {
        "route": "peshawar-karachi",
        "class": "Business",
        "price": 7600
    },
    {
        "route": "lahore-peshawar",
        "class": "First",
        "price": 2800
    },
    {
        "route": "lahore-peshawar",
        "class": "Economy",
        "price": 5300
    },
    {
        "route": "lahore-peshawar",
        "class": "Business",
        "price": 8100
    },
]
def Booking():
    print("------------------------Please fill these information------------------------")
    name=input("Enter your name: ").strip()
    while  name.isdigit():
        name = input("Enter your valid name: ").strip()
    phone=input("Enter your phone number: ").strip()
    while not phone.isdigit() or not len(phone)==11:
        phone = input("Enter your valid phone number: ").strip()
    print("Select your route!!!")
    for index,route in enumerate(routes):
        index=index+1
        print(f"press {index} to select {route}")
    r=input("your route: ").strip()
    while not r.isdigit() or not 1<=int(r)<=len(routes):
        r = input("select correct route: ")
    r=int(r)
    print("Select your bus class!!!")
    selected_route = routes[r - 1]
    bus_classes = [bus['class'] for bus in busclass if bus['route'] == selected_route]
    for index, bus_class in enumerate(bus_classes):
        index=index+1
        print(f"press {index} to book {bus_class} class")
    bc = input("your bus class: ").strip()
    while not bc.isdigit() or not 1 <= int(bc) <= len(busclass):
        bc = input("select correct bus class: ")
    bc = int(bc)
    seats=input("How many seats do you want: ")
    while not seats.isdigit():
        seats = input("How many seats do you want in numbers: ")
    seats=int(seats)
    print("------------------------You successfully booked your ride------------------------")
    print(f"your name => {name}")
    print(f"your phone number => {phone}")
    print(f"your route => {routes[r-1]}")
    print(f"your bus class =>  {bus_classes[bc-1]}")


    selected_class = bus_classes[bc - 1]
    selected_price = next(
    bus['price'] for bus in busclass if bus['route'] == selected_route and bus['class'] == selected_class)
    print(f"your tour price =>  {selected_price * seats}")
