# Pong Game in Python

This is a simple implementation of the classic Pong game in Python. The game is played by two players, each controlling a paddle, trying to hit a ball back and forth across the screen. The first player to reach a certain number of points wins the game.

## Project Structure

The project has the following files:

`src/main.py`: This file is the entry point of the application. It creates an instance of the `Game` class and starts the game loop.

`src/ball.py`: This file exports a `Ball` class which represents the ball in the game. It has properties `x`, `y`, `radius`, `color`, `dx`, and `dy` which represent the position, size, color, and velocity of the ball. It has methods `draw` and `update` which draw the ball on the screen and update its position based on its velocity.

`src/paddle.py`: This file exports a `Paddle` class which represents a paddle in the game. It has properties `x`, `y`, `width`, `height`, `color`, and `dy` which represent the position, size, color, and velocity of the paddle. It has methods `draw` and `update` which draw the paddle on the screen and update its position based on its velocity.

`src/game.py`: This file exports a `Game` class which represents the game. It has properties `width`, `height`, `screen`, `ball`, `paddle1`, `paddle2`, `score1`, `score2`, and `game_over` which represent the size of the game screen, the ball, the two paddles, the scores, and the game state. It has methods `draw`, `update`, `handle_events`, and `reset` which draw the game on the screen, update the game state, handle user input, and reset the game when it ends.

`requirements.txt`: This file lists the dependencies required by the project.

## How to Run the Game

To run the game, you need to have Python 3 installed on your computer. You also need to install the dependencies listed in `requirements.txt`. You can do this by running the following command in your terminal:

```
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the game by running the following command in your terminal:

```
python src/main.py
```

This will start the game and you can start playing by using the arrow keys to move your paddle up and down.

## Conclusion

This project is a simple implementation of the classic Pong game in Python. It demonstrates how to use object-oriented programming to create a game with multiple components.