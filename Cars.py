class Cars:

    #Output, name, color, price
    def __init__(self, cars):
        self.cars = cars

    def printcars(self, cars_):
        if (type(cars_) is not list):
            print("List expected..\n")
            return 

        print("{:<20} {:<15} {:<10}".format('Name', 'Color', 'Price'))
        for car in cars_:
            if (type(car) is not dict):
                print("Dict expected..\n")
                break
            name, color, price = car.values()
            print("{:<20} {:<15} {:<10}".format(name, color, price), sep="\n\n")
    
    def compareprices(self):
        cheapestcar = self.cars[0]

        for car in self.cars:
            if car['price'] < cheapestcar['price']:
                cheapestcar = car

        return [cheapestcar]




# Allow user to dynamically input cars
def interactiveInput():
    car_list = list()
    try:
        limit = int(input("How many cars do you want to add (default = 3): "))
        if not limit:
            limit = 3

        print("All fields are mandatory!!..") 
        for i in range(limit):
            car_instance = {}
            try: 
                name = input("Input brand of car {}: ".format(i + 1))
                color = input("Input color of car {}: ".format(i + 1))
                price = float(input("Input price of car {}: ".format(i + 1)))

            except ValueError:
                if (not name) or (not color) or (not price):
                    print("Some values were left blank and will not be added to the list")
                else:
                    print("Wrong value")
            except KeyboardInterrupt:
                print("Do you want to end program")
            
            if name and color and price:
                car_instance['name'] = name
                car_instance['color'] = color
                car_instance['price'] = price
                car_list.append(car_instance)
            print('\n')

    except ValueError:
        print("Invalid input.. Try again")
    except KeyboardInterrupt:
        print('Ending progam')
    
    return car_list


# Default car lists
def defaultOutput():
    return [
        {"name": "Toyota", "color": "Red", "price": 2233}, 
        {"name": "BMW", "color": "Silver", "price": 2600},
        {"name": "Benz", "color": "Blue", "price": 2003}]

# Cars class instance
def output(cars):
    car = Cars(cars)
    print("Below are the list of cars")
    car.printcars(cars)

    print("\nThis is the cheapest car")
    cheapestcar = car.compareprices()
    car.printcars(cheapestcar)
    print("\n")

def main():
        terminate = True
        while terminate:
            try:
                choice = int(input("Choose:\n1.To add cars dynamically\n2.To see default cars\n3.Quit\nEnter: > "))
                if choice == 1:
                    user_cars = interactiveInput()
                    output(user_cars)
                elif choice == 2:
                    user_cars = defaultOutput()
                    output(user_cars)
                else:
                    print("Ending program")
                    terminate = False
            except ValueError:
                print("Invalid input encountered")  
            except KeyboardInterrupt:
                print("\nEnding program. Good Bye.")


if __name__ == "__main__":
    main()


