import sys


class Dial:
    def __init__(self):
        self.value = 50
        self.zeros = 0

    def left(self, val):
        print(f"Turning left: {val}")
        if self.value - val <= 0:
            self.zeros += int(self.value != 0) + ((val - self.value) // 100)
            if int(self.value != 0) + ((val - self.value) // 100) > 0:
                print(
                    f"Crossed zero {int(self.value != 0) + ((val - self.value) // 100)} times, bringing the zero count to {self.zeros}"
                )
        self.value = (self.value - val) % 100

    def right(self, val):
        print(f"Turning right: {val}")
        if self.value + val >= 100:
            add_zeros = int(self.value != 0 or val >= 100) + (
                (val - (100 - self.value)) // 100
            )
            self.zeros += add_zeros
            if add_zeros > 0:
                print(
                    f"Crossed zero {add_zeros} times, bringing the zero count to {self.zeros}"
                )
        self.value = (self.value + val) % 100


if __name__ == "__main__":
    d = Dial()
    for mov in sys.stdin.readlines():
        if mov.strip() == "":
            break
        if mov[0] == "L":
            d.left(int(mov[1:]))
        else:
            d.right(int(mov[1:]))
        print(f"The value is: {d.value}")
    print(f"The password is {d.zeros}")
