"""
1603. Design Parking System (Easy)

Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for
each size.

Implement the ParkingSystem class:
    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # initialize slot counts
        self.slots = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        # if there's an available slot of that type, park and return True
        if self.slots.get(carType, 0) > 0:
            self.slots[carType] -= 1
            return True
        return False


def main():
    parking = ParkingSystem(1, 1, 0)
    print(parking.addCar(1), "expected: True")
    print(parking.addCar(2), "expected: True")
    print(parking.addCar(3), "expected: False")
    print(parking.addCar(1), "expected: False")


if __name__ == "__main__":
    main()
