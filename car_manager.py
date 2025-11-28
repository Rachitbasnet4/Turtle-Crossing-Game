"""
car_manager.py
---------------

This module defines the `CarManager` class for the Turtle Crossing Game. 
The CarManager handles creating, moving, and speeding up cars that the player 
must avoid. Cars are generated randomly and move from the right to the left 
of the screen.

Constants:
----------
- COLORS: List[str] – Possible colors for the cars.
- STARTING_MOVE_DISTANCE: int – Initial speed of the cars.
- MOVE_INCREMENT: int – Speed increment after each level.

Classes:
--------
- CarManager: Manages car creation, movement, and speed increase.
"""
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """ 
    Manages cars in the Turtle Crossing Game.

    Attributes:
    -----------
    all_car: list[Turtle] - List containing all car instances on the screen.
    car_speed: int - Current speed of the cars.

    Methods:
    --------
    create_car(): Randomly creates a new car and adds it to the list.
    move_car(): Moves all cars across the screen based on current speed.
    increase_speed(): Increases the speed of all cars for higher levels.
    """
    def __init__(self):
        """ Initialize the CarManager with an empty car list and starting speed. """
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        """ 
        Randomly create a new car and place it on the right side of the screen.

        Cars are created with a 1 in 6 chance on each call and assigned a random color
        and vertical position.
        """
        random_chance = random.randint(1, 6)
        if random_chance ==1:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid= 1, stretch_len= 2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.all_car.append(car)

    def move_car(self):
        """Move all cars from right to left across the screen."""
        for car in self.all_car:
            car.backward(self.car_speed)

    def increse_speed(self):
        """Increase the movement speed of all cars for the next level."""
        self.car_speed += MOVE_INCREMENT
