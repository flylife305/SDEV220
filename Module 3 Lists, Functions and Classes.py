class Vehicle: #parent class
    def __init__(self):
        self.type = input("Enter vehicle type: ")
        
class Automobile (Vehicle): #child class
    def __init__(self, year, make, model, doors, roof):
        super().__init__()
        self.year = year
        self.make = make
        self.doors = doors
        self.roof = roof
        self.model = model
        
    
    def display_info(self): #info template
        print(f"Vehicle type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def create_car(): #creates object of child class

    make = input("Enter make: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))

    while True: #validates input
        doors = int(input("2 or 4 doors? "))
        if doors in [2,4]:
            break
        else:
            print("Please enter either 2 or 4 doors.")
    
    roof = input("solid or sunroof? ")

    while roof not in ['solid', 'sunroof']:
        print("Please enter 'solid' or 'sunroof'!")
        roof = input("solid or sunroof?")
    
    car = Automobile (make, model, year, doors, roof)


    
    print("\nVehicle Information:")
    car.display_info()

def main(): # main logic
    create_car()

if __name__ =="__main__":
    main()