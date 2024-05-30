import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius


def produce_circle_results(diameter: float, circumference: float, area: float):
    print(f'The circle has the following attributes:\nDiameter: {diameter}\nCircumference: {circumference}\nArea: {area}')


def main():
    while True:
        provided_radius = float(input('Please provide a radius for the circle: '))
        if provided_radius <= 0.0:
            print('Sorry the number you provided is not valid. Please enter number greater than 0.')
        else:
            break
    new_circle = Circle(provided_radius)
    while True:
        produce_circle_results(new_circle.calculate_diameter(), new_circle.calculate_circumference(), new_circle.calculate_area())
        grow_circle = input('Do you want to grow the circle? yes or no: ')
        if grow_circle.lower() == 'yes':
            new_circle.grow()
        else:
            print(f'Thanks for playing. The final radius of the circle was {new_circle.get_radius()}')
            break


if __name__ == '__main__':
    main()
