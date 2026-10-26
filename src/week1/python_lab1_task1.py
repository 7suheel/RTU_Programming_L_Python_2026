import math


def circle_area(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    print("Area:", format(area, ".2f"))