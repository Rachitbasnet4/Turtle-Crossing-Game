""" 
scoreboard.py
-------------

This module defines the `Scoreboard` class for the Turtle Crossing Game. 
The Scoreboard keeps track of the player's current level and displays 
it on the screen. It also shows a "Game Over" message when the player collides 
with a car.

Constants:
----------
- FONT: Tuple[str, int, str] – Font settings used for displaying text on screen.

Classes:
--------
- Scoreboard: Manages the game level display and game over message.
"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Represents the scoreboard for the Turtle Crossing Game.

    Inherits from the Turtle class to display text on the screen.

    Attributes:
    -----------
    level: int - Tracks the current level of the game.

    Methods:
    --------
    update_level(): Clears and updates the level display.
    increase_level(): Increments the level and updates the display.
    game_over(): Displays a "Game Over" message along with the final level.
    """
    def __init__(self):
        """ Initialize the scoreboard at the top-left corner of the screen. """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,250)
        self.update_level()

    def update_level(self):
        """ Clear the previous display and show the current level. """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1 and update the display."""
        self.level += 1
        self.update_level()

    def game_over(self):
        """DDisplay the 'Game Over' message at the center of the screen."""
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER\nYour total level is: {self.level}", align="center", font=FONT)
