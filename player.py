""" 
player.py
---------

This module defines the `Player` class for the Turtle Crossing Game. 
The Player class represents the turtle controlled by the user and provides 
methods for movement, detecting when the finish line is reached, and 
resetting the player position.

Constants:
----------
- STARTING_POSITION: Tuple[int, int] – Initial coordinates where the player starts.
- MOVE_DISTANCE: int – Distance the player moves with each "move" action.
- FINISH_LINE_Y: int – Y-coordinate representing the finish line.

Classes:
--------
- Player: Represents the game player turtle.
"""
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """ Represents the player turtle in the game, inherits from Turtle.

    Methods:
    --------
    player_move(): Moves the turtle forward by MOVE_DISTANCE.
    go_to_start(): Resets the turtle's position to the starting point.
    is_at_finish_line(): Returns True if the turtle has crossed the finish line. 
    """
    def __init__(self):
        """Initialize the player turtle at the starting position, facing up."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def player_move(self):
        """ Move the player turtle forward by a fixed distance. """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """ Return the player turtle to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """ 
        Check if the player turtle has reached or crossed the finish line.
        Returns:
            bool: True if the player's y-coordinate is greater than FINISH_LINE_Y, else False.
        """
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False
