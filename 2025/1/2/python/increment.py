import sys


class Dial:
    def __init__(self):
        self.value = 50
        self.zeros = 0

    def left(self, val):
        # print(f"Turning left: {val}")
        zero_adds = 0
        while val > 0:
            self.value -= 1
            val -= 1
            if self.value == 0:
                zero_adds += 1
                self.zeros += 1
            elif self.value < 0:
                self.value = 99
        # if zero_adds > 0:
        #    print(
        #        f"Crossed zero {zero_adds} times, bringing the zero count to {self.zeros}"
        #    )

    def right(self, val):
        # print(f"Turning right: {val}")
        zero_adds = 0
        while val > 0:
            self.value += 1
            val -= 1
            if self.value == 100:
                zero_adds += 1
                self.zeros += 1
                self.value = 0
        # if zero_adds > 0:
        #    print(
        #        f"Crossed zero {zero_adds} times, bringing the zero count to {self.zeros}"
        #    )


if __name__ == "__main__":
    d = Dial()
    for mov in sys.stdin.readlines():
        if mov.strip() == "":
            break
        if mov[0] == "L":
            d.left(int(mov[1:]))
        else:
            d.right(int(mov[1:]))
        # print(f"The value is: {d.value}")
    print(f"The password is {d.zeros}")
