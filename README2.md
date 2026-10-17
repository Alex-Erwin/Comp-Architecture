# Two-Board Multiplayer Pong

## Project Update 2 — October 16, 2026

## Project Idea

Our project is to make a two-player Pong game using two PINE Ox64 boards. Each player will use their own board with a screen and controls. The boards will communicate so both players can play the same match against each other.

We have decided to use Pong as our final game. Each player will move a paddle up and down to hit the ball. The game will track the score when a player misses the ball.

## Planned Features

- Two players using separate PINE Ox64 boards.
- A screen and controls for each player.
- Moving paddles and a ball with basic collision detection.
- Communication between the boards to keep both screens updated.
- Score tracking and a way to restart the game.

## Hardware and Current Progress

We have obtained the boards, screens, and most of the materials we expect to need. We still need to choose and purchase buttons or joysticks for the controls.

We connected a board to a screen and successfully displayed letters. We have not tested moving objects or Pong graphics yet. We have not started writing the game code, but we have been researching how to connect the two boards to each other.

## Planned Board Communication

Our current plan is for one board to handle the main game, including ball movement, collisions, and the score. The second board will send its player's input to the first board and receive game updates to display on its screen.

We are researching connection options. Wi-Fi and wired Ethernet are possibilities, but we still need to confirm the available hardware support and test a connection before choosing the final method.

## Weekly Timeline

We are planning to finish by December 1, 2026. This is a tentative deadline and will be updated once the final due date is confirmed.

| Week | Planned Work |
| --- | --- |
| October 12–18 | Record the current hardware progress, document the Pong design, and continue researching board communication. Basic letter output has already been demonstrated. |
| October 19–25 | Draw and move a rectangle on one screen. Choose and order buttons or joysticks. |
| October 26–November 1 | Write basic Pong code for ball movement, wall bounces, and paddle collisions. |
| November 2–8 | Test sending simple messages between the boards. Connect and test the player controls once they arrive. |
| November 9–15 | Connect the Pong gameplay across both boards and update both screens from the same game state. |
| November 16–22 | Add scoring and restarting. Test complete two-player matches. |
| November 23–29 | Fix problems, finish documentation, and prepare the final demonstration. |
| November 30–December 1 | Complete final checks and submit the project. |

## Project Documents

- [STATUS2.md](STATUS2.md): Current progress, remaining work, and next steps.
- [DESIGN.md](DESIGN.md): Proposed gameplay, controls, and board communication.

This is the second project README. The original README.md is retained as the earlier project description.
