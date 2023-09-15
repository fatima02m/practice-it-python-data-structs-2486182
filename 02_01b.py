from collections import deque


def main():
    # creating a deque size 5
    foods = deque(maxlen=5)
    # appends to the right side of the deque
    foods.append("STA001")
    ordered_foods = ["DES003", "STA002", "ENT004", "ENT001"]
    foods.extend(ordered_foods)

    # adding the 6th food will remove the first move so you have max 5
    foods.append("DES002")

   # appending to the left
    foods.appendleft("DES005")

    print(foods)
    return


if __name__ == "__main__":
    main()
