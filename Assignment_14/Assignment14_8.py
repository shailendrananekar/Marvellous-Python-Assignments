class Vehicle:

    def __init__(self):

        print("I am in class Vehicle...")

    def start(self):
        print("Vehicle is starting...")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        print("I am in class Car...")

    def start(self, a):

        print("Car is starting... : ", a)


def main():
    vehicle = Vehicle()
    vehicle.start()

    car = Car()
    car.start(20)


if __name__ == "__main__":
    main()
