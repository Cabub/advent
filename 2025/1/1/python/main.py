import sys


class Dial:
    def __init__(self):
        self.value = 50
        self.zeros = 0

    def left(self, val):
        self.value = (self.value - val) % 100
        if self.value == 0:
            self.zeros += 1

    def right(self, val):
        self.value = (self.value + val) % 100
        if self.value == 0:
            self.zeros += 1


if __name__ == "__main__":
    d = Dial()
    for mov in sys.stdin.readlines():
        if mov.strip() == "":
            break
        if mov[0] == "L":
            d.left(int(mov[1:]))
        else:
            d.right(int(mov[1:]))
    print(f"The password is {d.zeros}")
