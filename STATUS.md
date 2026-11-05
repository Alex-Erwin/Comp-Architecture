# Project Status

## Update 2: October 16, 2026

We have moved forward from the initial planning stage of our two-board multiplayer game. We have decided to build Pong, obtained the boards and screens, and successfully displayed letters on a screen connected to one board.

## Progress Since the September 30 Update

- Selected Pong as the final game.
- Obtained the boards, screens, and most of the materials we expect to need.
- Connected a PINE Ox64 board to a screen and displayed letters.
- Researched possible ways for the two boards to communicate.

## Documentation Completed for This Update

- Created README2.md with the current project description and a weekly timeline.
- Added DESIGN.md describing the proposed gameplay and division of work between the boards.
- Recorded the tested hardware progress and remaining tasks in this status update.

## What Has Been Tested

Basic text output has worked on a screen connected to one board. This is a first step toward displaying the game, but we have not displayed a moving object or tested Pong graphics yet.

## What Is Not Working Yet

- Game code has not been started.
- Communication between the two boards has not been implemented or tested.
- Buttons or joysticks still need to be chosen and purchased.
- Paddle movement, ball movement, collisions, and scoring have not been implemented.

## Current Communication Plan

We plan to have one board run the main game and maintain the ball position and score. The other board will send player input and receive game updates. We are still researching the connection method and have not selected or tested a final option.

## Next Steps

1. Draw a rectangle on one screen and make it move.
2. Choose and purchase the player controls.
3. Choose a connection method and test sending a simple message between the boards.
4. Begin implementing the basic Pong game.

## Schedule

We are using December 1, 2026 as a tentative completion date. The weekly timeline is in README2.md. We will revise it as we test the hardware and confirm the final due date.

## Update 3: October 19–November 1, 2026

### Code prepared

- Created a simplified `pong.py` with `move_ball()`, `wall_collision()`, `paddle_collision()`, and `update_game()`.
- Defined the playing field, ball velocity and size, and fixed test paddle positions.
- Added a small console demonstration that prints ball coordinates for 30 updates.
- Removed desktop graphics, keyboard controls, and game features outside this milestone's basic movement/collision scope.

### Verification status

| Item | Status |
| --- | --- |
| Basic movement and collision source code | Written; hardware gameplay not tested |
| Python syntax | Checked |
| Console position demonstration | Included; not a graphical game |
| Moving rectangle on PINE Ox64 screen | Not confirmed |
| Buttons or joystick selected/ordered | Not confirmed |
| Physical paddle input | Not implemented |
| Board-to-board communication | Not implemented |
| Scoring and ball reset after misses | Not implemented |

### Next steps

1. Run `python3 pong.py` and verify the position output and collision behavior.
2. Draw and animate a rectangle/ball on the PINE Ox64 display.
3. Confirm the control hardware and read its inputs.
4. Test communication between the boards and integrate the game logic.

This update records completed **source-code preparation**, not a completed playable game or successful hardware testing.

## Update 4: November 2–8, 2026

### Decisions and Code Prepared

- **Board-to-Board Connection Selected:** Confirmed that our PINE64 Ox64 carrier boards include built-in RJ45 Ethernet ports. Selected a direct point-to-point LAN (Ethernet) cable connection between the two boards.
- **Static IP Configuration (not set yet):** Plan to hard-set a static IP address on each board so they can connect directly anywhere (in class, in the lab, or at home) without relying on Wi-Fi networks, captive portals, or routers. The addresses have not been chosen or configured yet.
- **Player Controls Selected:** Chose joysticks over individual buttons for player up/down movement.
- **Paddle Movement Added to `pong.py`:** Implemented `move_paddles(left_dir, right_dir)` with `paddle_speed` and vertical boundary clamping so paddles stay within the `0` to `HEIGHT` screen limits. Updated `update_game()` and the console demonstration to test simulated joystick directions (`-1` for up, `1` for down, `0` for neutral).

### Verification Status

| Item | Status |
| --- | --- |
| Carrier board Ethernet hardware check | Confirmed (RJ45 port present on the carrier board) |
| Direct LAN and static IP architecture | Planned; physical ping test on hardware pending |
| Player control selection | Joysticks selected; physical GPIO wiring not tested |
| Dynamic paddle movement code (`pong.py`) | Written and verified in console simulation |
| Moving graphics on PINE Ox64 screen | Not confirmed |
| Live packet transmission between boards | Not implemented yet |
| Scoring and ball reset after misses | Planned for November 16–22 milestone |

### Next Steps

1. Choose and hard-set a static IP address on each PINE Ox64 board, then verify connectivity over the LAN cable.
2. Connect the joysticks to the 26-pin GPIO headers and read directional inputs in Python.
3. Write and test the socket scripts to send joystick input from Board 2 to Board 1 and return the updated game state.
4. Integrate screen drawing on the PINE Ox64 displays.
