from random import random


def generate_random_point():
    return random(), random()


def generate_multiple_random_point(how_many):
    list_random_number = []
    for i in range(how_many):
        list_random_number.append(generate_random_point())

    return list_random_number


def is_in_circle(point):
    distance = pow(point[0], 2) + pow(point[1], 2)
    return distance <= 1


def generate_pi(number_of_random_point):
    list_random_point = generate_multiple_random_point(number_of_random_point)
    count_in_square = number_of_random_point
    count_in_circle = 0

    for point in list_random_point:
        if is_in_circle(point):
            count_in_circle += 1
    print(count_in_circle.__str__() + ' in circle of ' + number_of_random_point.__str__())
    return 4 * count_in_circle/count_in_square


if __name__ == '__main__':
    print(generate_pi(100000000))

