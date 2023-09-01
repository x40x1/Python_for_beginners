# Pong Game

This is a simple Pong game built using HTML5 canvas and JavaScript. The game has two paddles and a ball, and the objective is to score points by hitting the ball past the opponent's paddle.

## Project Structure

The project has the following file structure:

```
pong-game
├── src
│   ├── index.html
│   ├── index.js
│   ├── styles.css
│   ├── ball.js
│   ├── paddle.js
│   └── game.js
├── package.json
└── README.md
```

- `src/index.html`: This file is the main HTML file for the game. It contains the canvas element and links to the CSS and JavaScript files.
- `src/index.js`: This file is the entry point of the game. It creates an instance of the `Game` class and starts the game loop.
- `src/styles.css`: This file contains the styles for the game.
- `src/ball.js`: This file exports a class `Ball` which represents the ball in the game. It has properties `x`, `y`, `radius`, `dx`, and `dy`, and methods `draw` and `update`.
- `src/paddle.js`: This file exports a class `Paddle` which represents the paddles in the game. It has properties `x`, `y`, `width`, `height`, and methods `draw` and `update`.
- `src/game.js`: This file exports a class `Game` which represents the game itself. It has properties `canvas`, `ctx`, `ball`, `paddle1`, `paddle2`, `score1`, `score2`, and methods `start`, `draw`, `update`, `reset`, `handleCollision`, `handlePaddleCollision`, `handleScore`, `handleKeyDown`, and `handleKeyUp`.

## How to Play

- Use the up and down arrow keys to move the left paddle.
- Use the W and S keys to move the right paddle.
- The game ends when one player reaches 10 points.
- Press the spacebar to restart the game.

## Acknowledgements

This game was built following the tutorial by Chris DeLeon on [CodePen](https://codepen.io/chrisdleon/pen/ExjJQvM).