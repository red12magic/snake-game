import random
import curses

# Initialize the curses library to create our screen
screen = curses.initscr()

# Hide the cursor
curses.curs_set(0)
# Get the maximum screen height and width
screen_height, screen_width = screen.getmaxyx()
# Create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)
# Allow window to receive input from the keyboard
window.keypad(1)
# Set the delay for updating the screen
window.timeout(100)

# Set the initial position of the snake's head
snk_x = screen_width // 4
snk_y = screen_height // 2

# Define the initial position of the snake body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Create the food in the middle of the window
food = [screen_height // 2, screen_width // 2]

# Add the food using pi character from the curses module
window.addch(food[0], food[1], curses.ACS_PI)

# Set initial movement direction to right
key = curses.KEY_RIGHT

# Create game loop that loops forever until the player loses or quits the game
while True:
    # Get the next key that will be pressed by user
    next_key = window.getch()

  
    key = key if next_key == -1 else next_key

    # Check if the snake collided with the walls or itself
    if (snake[0][0] in [0, screen_height] or
        snake[0][1] in [0, screen_width] or
        snake[0] in snake[1:]):
        curses.endwin()  # Closing the window
        quit()  # Exit the program

    # Set the new position of the snake head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # Insert the new head to the first position of the snake
    snake.insert(0, new_head)

    # Check if the snake ate the food
    if snake[0] == food:
        food = None  # Remove the food after the snake eats it
        # While food is removed, generate a new food
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in snake else None
        # Set the food to new if new food generated is not in snake body and add it to screen
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Otherwise remove the last segment of snake body
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Update the position of the snake on screen
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
