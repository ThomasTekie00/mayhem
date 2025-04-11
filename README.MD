# Mayhem Clone
- Python implementation of Amiga game Mayhem, made for the INF_1400 Assignment 3

# Game:
Mayhem is a two-player space combat game where each player controls a spaceship using keyboard controls. The objective is to shoot down
your opponent while cruising between the rocks or just shooting down the rocks to score points. You also have to manage your fuel supply
otherwise its game-over.

## Features:
- Two spaceships with physics based movement with gravity and thrust for movement
- Four controls for each of the ships: Turn left, turn right, thrust and shoot
- Obstacles can be shot down and crashed into
- Health and fuel packs spread around
- Scoring point with winning conditions
- Game over screen with a restart option

# Controls:
### Player 1:
- W - Thrust
- A - Turn left
- D - Turn right
- SPACE - Shoot


### Player 2:
- Up ARROW: Thrust
- Left ARROW: Turn left
- Right ARROW: Turn right
- Right SHIFT: Shoot


# Install
- Python and pygame installed
- Clone the repo
- Run the game with python main.py

# Project structure:
- Main file got the game loop and game management
- Starships.py: Implements the ships with controls and physics
- Gameobject.py: Implements pickups, rock shower and bullets
- config.py: Game configuration
 


