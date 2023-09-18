from collections import deque


def check_palindrome(word):
    d = deque(word)
    # don't need to have something incrementing thorugh the word, python alrady knows to do that
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


def main():
    word = "racecar"
    print(check_palindrome(word))
    return


if __name__ == "__main__":
    main()
