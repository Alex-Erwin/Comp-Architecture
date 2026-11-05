"""Basic Pong movement, paddle input, and collision logic (no graphics or hardware controls yet)."""

WIDTH = 640
HEIGHT = 400

ball_x = 320
ball_y = 200
ball_dx = 4
ball_dy = 3
ball_size = 10

left_paddle_y = 160
right_paddle_y = 160
paddle_height = 80
paddle_width = 12
paddle_speed = 6
left_paddle_x = 20
right_paddle_x = WIDTH - 20 - paddle_width


def move_paddles(left_dir=0, right_dir=0):
    """Moves paddles vertically based on joystick direction (-1 up, 1 down, 0 neutral)."""
    global left_paddle_y, right_paddle_y
    left_paddle_y += left_dir * paddle_speed
    right_paddle_y += right_dir * paddle_speed

    # Clamp paddles inside the top and bottom screen boundaries
    if left_paddle_y < 0:
        left_paddle_y = 0
    elif left_paddle_y + paddle_height > HEIGHT:
        left_paddle_y = HEIGHT - paddle_height

    if right_paddle_y < 0:
        right_paddle_y = 0
    elif right_paddle_y + paddle_height > HEIGHT:
        right_paddle_y = HEIGHT - paddle_height


def move_ball():
    global ball_x, ball_y
    ball_x += ball_dx
    ball_y += ball_dy


def wall_collision():
    global ball_y, ball_dy
    if ball_y <= 0:
        ball_y = 0
        ball_dy = abs(ball_dy)
    elif ball_y + ball_size >= HEIGHT:
        ball_y = HEIGHT - ball_size
        ball_dy = -abs(ball_dy)


def paddle_collision():
    global ball_x, ball_dx
    if ball_dx < 0 and left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if ball_y + ball_size >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_dx = abs(ball_dx)
    elif ball_dx > 0 and right_paddle_x - ball_size <= ball_x <= right_paddle_x:
        if ball_y + ball_size >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x - ball_size
            ball_dx = -abs(ball_dx)


def update_game(left_dir=0, right_dir=0):
    move_paddles(left_dir, right_dir)
    move_ball()
    wall_collision()
    paddle_collision()


if __name__ == "__main__":
    for frame in range(30):
        # Simulate joystick input: left moves up for 15 frames then down; right moves down then up
        sim_left = -1 if frame < 15 else 1
        sim_right = 1 if frame < 15 else -1
        update_game(sim_left, sim_right)
        print(
            f"Frame {frame + 1}: ball=({ball_x}, {ball_y}), "
            f"paddles=({left_paddle_y}, {right_paddle_y})"
        )
