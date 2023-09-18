from collections import namedtuple

# function compares the drivers capcity with the capacity of the order


def can_take_order(driver, capacity):
    return driver.car_capacity >= capacity


def main():
    # create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    # an example you can use to practice: "Iris", "Toyota Prius", 7
    iris = Driver("Iris", "Prius", 7)
    # check if they can take a certain order, given their car's capacity.
    print(can_take_order(iris, 10))
    return

if __name__ == "__main__":
    main()
