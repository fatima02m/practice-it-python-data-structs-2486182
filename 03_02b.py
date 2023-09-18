from collections import namedtuple
from csv import reader


def main():
    # add code here
    # read data/Customer.csv
    with open("data/Customer.csv", "r") as open_csv:
        read = reader(open_csv)  # puts data in 'read'
        # creates a tuple, reads the first line which has the field names for the tuple
        Person = namedtuple("person", next(read))
        for line in read:
            person = Person(*line)
            print(person)

    # Create workable objects with each line

    return


if __name__ == "__main__":
    main()
