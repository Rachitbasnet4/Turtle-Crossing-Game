""" 
Turtle Crossing Game
-------------------
This is a simple arcade-style game built using Python's `turtle` module. 
The objective of the game is to safely guide a turtle across a busy road 
without colliding with moving cars. The game increases in difficulty as 
the player progresses.

Modules:
--------
- `player`: Contains the `Player` class which handles the turtle character, 
  its movement, and tracking if it has reached the finish line.
- `car_manager`: Contains the `CarManager` class which manages car creation, 
  movement, and speed increment as the player advances levels.
- `scoreboard`: Contains the `Scoreboard` class which tracks the player's 
  current level and displays the "Game Over" message when the game ends.

Gameplay:
---------
- The player controls the turtle using the "Up" arrow key.
- Cars move horizontally across the screen from right to left.
- Collision with a car ends the game.
- Successfully reaching the top of the screen increases the level and car speed.

Classes:
--------
- Player: Handles the turtle's position, movement, and finish line detection.
- CarManager: Manages car creation, movement, and dynamic speed adjustment.
- Scoreboard: Tracks levels and displays game status.

Main Loop:
----------
1. Listens for player input (turtle movement).
2. Continuously updates the screen and moves cars.
3. Checks for collisions between the turtle and cars.
4. Checks if the turtle successfully crosses the road and updates level and speed.

Usage:
------
Run this script to start the game. The game window will display the turtle, 
moving cars, and current level. Use the Up arrow key to navigate the turtle 
across the road safely.
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

SCREEN.listen()
SCREEN.onkey(player.player_move,"Up")

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    SCREEN.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision and game over method
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            GAME_IS_ON = False
            score.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        score.increase_level()
        car_manager.increse_speed()



SCREEN.exitonclick()
