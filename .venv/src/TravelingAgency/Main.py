from Booking import Booking
from Buses_Fares import Buses_Fares
from Add_Driver import Add_Driver
from Drivers_list import Drivers_list
from Add_Bus import Add_Bus
from Buses_list import Buses_list
def main():
    print("------------------------Welcome to our agency------------------------")
    services=["Booking","Buses fares","Add driver","Drivers list","Add bus","Buses list"]
    service_functions = [Booking,Buses_Fares,Add_Driver,Drivers_list,Add_Bus,Buses_list]
    for index,item in enumerate(services):
        index=index+1
        print(f"press {index} for {item}")
    ser=input("What you want: ")
    while not ser.isdigit() or not 1<=int(ser)<=len(services):
        ser=input("What you want: ")
    ser=int(ser)
    for index,item in enumerate(services):
        while ser<=len(services):
            index=index+1
            if ser==index:
                service_functions[ser-1]()
                break
        break

if __name__=="__main__":
    main()