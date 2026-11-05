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

## Development Update — October 19–November 1, 2026

### Current Python implementation (`pong.py`)

The first gameplay implementation is a **logic-only prototype**, not a playable Pong game. It uses a 640-by-400 coordinate system, a 10-by-10 ball, and two stationary 12-by-80 paddles. The ball starts at `(320, 200)` and moves by `(4, 3)` on each update.

- `move_ball()` adds `ball_dx` and `ball_dy` to the ball coordinates.
- `wall_collision()` checks the top and bottom boundaries, corrects the ball's position, and reverses vertical movement.
- `paddle_collision()` checks whether the ball overlaps a paddle while moving toward it, then reverses horizontal movement.
- `update_game()` runs movement, wall detection, and paddle detection once.

The `__main__` section runs 30 updates and prints positions to the terminal. No drawing library is used. Paddle positions are placeholders; they do not respond to player input yet. The prototype does not implement scores, serves, or two-board communication. These remain part of the planned final design described above.

### Integration still required

Display the moving ball and paddles on the PINE Ox64 screen, connect physical controls, add scoring and reset behavior, and send player input/game state between the boards. Test actual ball movement and collisions on the target hardware before marking them complete.

## Development Update — November 2–8, 2026

### Network Architecture and Portability

We inspected our PINE64 Ox64 carrier boards and verified that each board includes an onboard 10/100 RJ45 Ethernet port alongside a 26-pin GPIO header and MIPI LCD connector.

To ensure the setup works anywhere (classroom, lab, or home) without changing Wi-Fi passwords or dealing with school network restrictions, we selected a **direct Ethernet (LAN) cable connection** between the two boards. Each board will be given a hard-set static IP address on the same subnet:

- **Board 1 (Main Game Host):** static IP to be assigned
- **Board 2 (Player 2 Client):** static IP to be assigned

The addresses have not been chosen or configured yet.

### Planned Message Format

- **Board 2 to Board 1:** Sends player 2's joystick direction on each update (`-1` for up, `1` for down, `0` for neutral), e.g., `{"dir": -1}`.
- **Board 1 to Board 2:** Sends the authoritative positions (`ball_x`, `ball_y`, `left_paddle_y`, `right_paddle_y`) so Board 2 can render the matching frame.

### Joystick Input and Paddle Movement (`pong.py`)

We selected joysticks for the player controls and added `move_paddles(left_dir=0, right_dir=0)` to `pong.py`:

- Moves each paddle vertically by `direction * paddle_speed` (`6` pixels per update).
- Clamps `left_paddle_y` and `right_paddle_y` between `0` and `HEIGHT - paddle_height` (`320`) so paddles cannot move off-screen.
- `update_game(left_dir, right_dir)` now runs `move_paddles()` before updating the ball and checking collisions.
