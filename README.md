# Frogger Clone
Frogger Clone is a game in which the player seeks to gather as many coins as possible while avoiding cars. The game continues until the player is hit by a car.

Rules
Frogger Clone is played according to the following rules.

Coins (O) randomly appear on the screen.
Cars (C) randomly appear on the screen and move horizontally towards its opposite edge.
The player (F) can move according to the arrow keys.
If the player touches a coin they earn points and the coin reappears elsewhere.
If the player touches a car the game is over.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 frogger 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the frogger folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                     (project root folder)
+-- frogger               (source code for game)


## Required Technologies
* Python 3.8.0

## Authors
* George Blanchard
* Ricardo Rivas
* Alvaro Loran


TO - DO LIST

game.scripting.handle_collison_actions.py
    Add functionality for the cars hitting the frog
        The game stops detecting collisions
        A game over banner reappears
        Anything else we think of?

(Do we want to continue the game with some kind of "lives" system? Or if the player has enough points they can spend some for another life?
This could be done similar to how it was done in our last Cycle game)


constants.py
    Create a second subset of constants to facilitate larger cars


    
Anything else we deem cool/necessary