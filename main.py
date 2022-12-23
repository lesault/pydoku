import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the background color
bg_color = (255, 255, 255)

# Set the cell size
cell_size = 50

# Set the font for the numbers
font = pygame.font.Font(None, 36)

# Set the margin between cells
margin = 0

# Set the line width for the grid
line_width = 1

# Set the line width for the thick grid lines
thick_line_width = 3

# Set the grid color
grid_color = (0, 0, 0)

# Set the color of the numbers
number_color = (0, 0, 0)

# Set the color of the center marks
center_mark_color = (0, 0, 255)

# Set the color of the corner marks
corner_mark_color = (255, 0, 0)

# Set the size of the center marks
center_mark_size = 15

# Set the size of the corner marks
corner_mark_size = 10

# Set the initial grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def update_cell(x, y, value):
    """Updates the value of the cell at (x, y) with the given value."""
    grid[x][y] = value


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = event.pos
            # Calculate the cell that was clicked
            cell_x = mouse_x // (cell_size + margin)
            cell_y = mouse_y // (cell_size + margin)
            # Update the cell with a value
            update_cell(cell_x, cell_y, 5)

    # Draw the background
    screen.fill(bg_color)

    # Draw the grid
    for x in range(9):
        for y in range(9):
            # Calculate the top left position of the cell
            top_left_x = x * (cell_size + margin) + margin
            top_left_y = y * (cell_size + margin) + margin

            # Draw the cell outline
            pygame.draw.rect(
                screen,
                grid_color,
                (top_left_x, top_left_y, cell_size, cell_size),
                line_width,
            )

            # Get the value of the cell
            value = grid[x][y]

            # Draw the center marks if necessary
            if value == "c":
                for i in range(1, 10):
                    # Calculate the position of the mark
                    mark_x = top_left_x + cell_size / 2
                    mark_y = top_left_y + cell_size / 2
                    # Draw the mark
                    pygame.draw.circle(
                        screen,
                        center_mark_color,
                        (int(mark_x), int(mark_y)),
                        center_mark_size,
                    )
                    # Rotate the mark
                    mark_x, mark_y = rotate(
                        mark_x,
                        mark_y,
                        top_left_x + cell_size / 2,
                        top_left_y + cell_size / 2,
                        10,
                    )

            # Draw the corner marks if necessary
            elif value == "b":
                for i in range(1, 10):
                    # Calculate the position of the mark
                    mark_x, top_left_y + cell_size / 2
                    # Draw the mark
                    pygame.draw.circle(
                        screen,
                        corner_mark_color,
                        (int(mark_x), int(mark_y)),
                        corner_mark_size,
                    )
                    # Rotate the mark
                    mark_x, mark_y = rotate(
                        mark_x,
                        mark_y,
                        top_left_x + cell_size / 2,
                        top_left_y + cell_size / 2,
                        45,
                    )

            # Draw the number if necessary
            elif value != 0:
                # Render the text
                text = font.render(str(value), True, number_color)
                # Calculate the position of the text
                text_x = top_left_x + (cell_size - text.get_width()) / 2
                text_y = top_left_y + (cell_size - text.get_height()) / 2
                # Draw the text
                screen.blit(text, (text_x, text_y))
    # Draw the box borders
    tic_tac_endpoints = [
        ((0, (3 * cell_size)), ((9 * cell_size), (3 * cell_size))),
        ((0, (6 * cell_size)), ((9 * cell_size), (6 * cell_size))),
        (((3 * cell_size), 0), ((3 * cell_size), (9 * cell_size))),
        (((6 * cell_size), 0), ((6 * cell_size), (9 * cell_size))),
    ]

    for end in tic_tac_endpoints:
        pygame.draw.line(
            screen,
            grid_color,
            (end[0][0], end[0][1]),
            (end[1][0], end[1][1]),
            5 * line_width,
        )

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
