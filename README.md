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

- [STATUS.md](STATUS.md): Current progress, remaining work, and next steps.
- [DESIGN.md](DESIGN.md): Proposed gameplay, controls, and board communication.

This is the second project README. The original README.md is retained as the earlier project description.

## Development Update 3 — October 19–November 1, 2026

For the October 26–November 1 milestone, we wrote a **small Python logic prototype** in `pong.py`. It defines the ball's position and velocity, moves the ball one step, reverses its vertical direction at the top/bottom walls, and reverses its horizontal direction when it overlaps a paddle. An `update_game()` function calls those three steps in order.

This version intentionally **does not** draw a game window, read keyboard or physical controls, keep score, reset after misses, or communicate between boards. The two paddle positions are fixed test values. The code runs on a computer using Python 3 without additional packages; it prints 30 ball positions to demonstrate updates. It is not yet integrated with the PINE Ox64 displays.

### Project files

- `pong.py` — basic movement and collision functions, plus a short console test.
- `DESIGN.md` — gameplay design and explanation of the simplified code.
- `STATUS.md` — completed code and unverified hardware tasks.

The October 19–25 tasks (moving a rectangle on the board's screen and choosing/ordering controls) still require confirmation. The next stage is testing graphics and input on the hardware, then board-to-board communication.

## Development Update 4 — November 2–8, 2026

For the November 2–8 milestone, we finalized our board-to-board connection architecture, selected our control hardware, and expanded `pong.py` to support paddle movement:

- **Direct LAN Connection with Static IPs:** After inspecting our PINE64 Ox64 carrier boards and confirming the integrated RJ45 Ethernet ports, we decided to connect the two boards directly with an Ethernet (LAN) cable using a hard-set static IP address on each board (addresses not set yet). This peer-to-peer setup is intended to work reliably across multiple locations (classroom, lab, and home) without requiring Wi-Fi logins or router setup.
- **Joystick Controls:** We selected joysticks for player input and updated the game logic to accept directional values (`-1` for up, `1` for down, `0` for neutral).
- **Paddle Movement in `pong.py`:** Added `move_paddles(left_dir, right_dir)` with boundary clamping so paddles move smoothly according to joystick input without leaving the top or bottom of the playing field.
