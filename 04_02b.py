from collections import namedtuple, defaultdict
from csv import reader
from pprint import pprint


def main():
    # creatind default dict
    res = defaultdict(int)
    # opening and reading the file
    with open("data/OrderItems.csv", "r") as open_csv:
        read = reader(open_csv)
        # creating a tuple to store the items
        # using next(read) to read the first line and store the identifiers
        Item = namedtuple("Item", next(read))

        for line in read:
            item = Item(*line)
            # increments through the productID
            # adding the items together for each productID
            # each productID is a
            res[item.ProductID] += int(item.Quantity)
    pprint(dict(res))

    return


if __name__ == "__main__":
    main()
