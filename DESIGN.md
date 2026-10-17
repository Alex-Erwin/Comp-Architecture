# Two-Board Pong Design

## Initial Design — October 16, 2026

This document describes our proposed design. The gameplay and communication described below have not been implemented or tested yet. So far, we have successfully displayed letters on a screen connected to one board.

## Gameplay

Each player will control one paddle that moves up and down. A ball will move across the screen and bounce off the top and bottom edges and the paddles. If the ball passes a paddle, the other player will receive a point. After each point, the ball will reset for the next serve.

Both screens will show the same playing field and score. We plan to include a way to restart a match. The winning score and restart control still need to be decided.

## Hardware Setup

- Two PINE Ox64 boards.
- A screen connected to each board.
- Buttons or a joystick for each player, still to be selected and purchased.
- A connection between the boards, with the method still to be selected and tested.

## Controls

Each player needs an up input and a down input. We are considering either two buttons or a joystick for each player. We will choose the controls after checking how to connect and read them on the boards.

## Responsibilities of Each Board

| Board | Planned Responsibilities |
| --- | --- |
| Board 1: Main game board | Read player 1's controls, receive player 2's input, update both paddles and the ball, check collisions, track the score, draw the game, and send game updates to board 2. |
| Board 2: Second player board | Read player 2's controls, send that input to board 1, receive the current game state, and draw it on its screen. |

Using one board to calculate the game state should help prevent the boards from calculating different ball positions or scores.

## Information Sent Between Boards

The second board will send whether its player is pressing up, pressing down, or not moving. The main board will send the ball position, both paddle positions, the score, and whether the game is playing or waiting to restart.

We are considering Wi-Fi or wired Ethernet. We still need to verify hardware support and test a simple connection before choosing the final method. The message format and update rate will be decided during implementation.

## Planned Development and Testing

1. Draw a stationary rectangle on one screen.
2. Move the rectangle repeatedly to test animation and screen clearing.
3. Add the ball, paddles, and basic collision detection on one board.
4. Read and test the chosen player controls.
5. Send a simple message between the boards and confirm it is received.
6. Send player input and game state between the boards.
7. Test that both screens show matching positions and scores during a match.
8. Test scoring, restarting, and what happens if the connection is interrupted.

## Open Decisions

- Buttons or joysticks for player controls.
- Final board connection method and communication protocol.
- Programming language and display interface to use for the game.
- Display update rate and game speed.
- Winning score and restart behavior.
- How the game will pause or recover if the boards lose connection.
