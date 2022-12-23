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

# Set the button size
button_size = (50, 50)

# Set the button colors
button_color = (135, 135, 135)
selected_button_color = (200, 200, 200)

# Set the button value text colors
button_text_color = (0, 0, 0)
selected_button_text_color = (255, 255, 255)

# Set the value for each button
button_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Set the starting x and y coordinates for the buttons
button_x = 50
button_y = 9 * (cell_size + margin) + 50

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


class Cell:
    def __init__(
        self,
        r,
        c,
        width=cell_size,
        height=cell_size,
        kind=None,
        value=None,
        selected=False,
    ):
        self.r = r
        self.c = c
        self.x = (c - 1) * (cell_size + margin) + margin
        self.y = (r - 1) * (cell_size + margin) + margin
        self.width = width
        self.height = height
        self.kind = kind
        # self.value = value
        self.value = 8
        self.selected = False

    def draw(self, surface):
        # Draw the cell outline
        pygame.draw.rect(
            surface,
            grid_color,
            (self.x, self.y, self.width, self.height),
            line_width,
        )

        # Draw the number if necessary
        if self.value != None:
            # Render the text
            text = font.render(str(self.value), True, number_color)
            # Calculate the position of the text
            text_x = self.x + (self.width - text.get_width()) / 2
            text_y = self.y + (self.height - text.get_height()) / 2
            # Draw the text
            screen.blit(text, (text_x, text_y))


# Create the buttons
buttons = []
for value in button_values:
    # Create the button
    button = pygame.Rect(button_x, button_y, button_size[0], button_size[1])
    buttons.append(button)

    # Update the x coordinate for the next button
    button_x += button_size[0] + 10

    # Set the selected button
    selected_button = None

# build an array of cells
full_grid = [
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

for col in range(1, 10):
    for row in range(1, 10):
        full_grid[row - 1][col - 1] = Cell(col, row)


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            for button in buttons:
                if button.collidepoint(event.pos):
                    # Set the selected button
                    selected_button = button
                    value = str(button_values[buttons.index(button)])
                    break
            # Get the mouse position
            mouse_x, mouse_y = event.pos
            # Calculate the cell that was clicked
            cell_x = mouse_x // (cell_size + margin)
            cell_y = mouse_y // (cell_size + margin)
            if cell_x < 10 and cell_y < 10:
                print(cell_x, cell_y)
                # Update the cell with a value
                update_cell(cell_x, cell_y, 5)
                full_grid[cell_x][cell_y].value = value

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background
    screen.fill(bg_color)

    # Draw the grid
    # for row in range(9):
    #     for col in range(9):
    for col in range(1, 10):
        for row in range(1, 10):
            full_grid[row - 1][col - 1].draw(screen)

    # Draw the grid
    # for x in range(9):
    #     for y in range(9):
    #         # Calculate the top left position of the cell
    #         top_left_x = x * (cell_size + margin) + margin
    #         top_left_y = y * (cell_size + margin) + margin

    #         # Draw the cell outline
    #         pygame.draw.rect(
    #             screen,
    #             grid_color,
    #             (top_left_x, top_left_y, cell_size, cell_size),
    #             line_width,
    #         )

    #         # Get the value of the cell
    #         value = grid[x][y]

    #         # Draw the center marks if necessary
    #         if value == "c":
    #             for i in range(1, 10):
    #                 # Calculate the position of the mark
    #                 mark_x = top_left_x + cell_size / 2
    #                 mark_y = top_left_y + cell_size / 2
    #                 # Draw the mark
    #                 pygame.draw.circle(
    #                     screen,
    #                     center_mark_color,
    #                     (int(mark_x), int(mark_y)),
    #                     center_mark_size,
    #                 )
    #                 # Rotate the mark
    #                 mark_x, mark_y = rotate(
    #                     mark_x,
    #                     mark_y,
    #                     top_left_x + cell_size / 2,
    #                     top_left_y + cell_size / 2,
    #                     10,
    #                 )

    #         # Draw the corner marks if necessary
    #         elif value == "b":
    #             for i in range(1, 10):
    #                 # Calculate the position of the mark
    #                 mark_x, top_left_y + cell_size / 2
    #                 # Draw the mark
    #                 pygame.draw.circle(
    #                     screen,
    #                     corner_mark_color,
    #                     (int(mark_x), int(mark_y)),
    #                     corner_mark_size,
    #                 )
    #                 # Rotate the mark
    #                 mark_x, mark_y = rotate(
    #                     mark_x,
    #                     mark_y,
    #                     top_left_x + cell_size / 2,
    #                     top_left_y + cell_size / 2,
    #                     45,
    #                 )

    #         # Draw the number if necessary
    #         elif value != 0:
    #             # Render the text
    #             text = font.render(str(value), True, number_color)
    #             # Calculate the position of the text
    #             text_x = top_left_x + (cell_size - text.get_width()) / 2
    #             text_y = top_left_y + (cell_size - text.get_height()) / 2
    #             # Draw the text
    #             screen.blit(text, (text_x, text_y))

    # Draw the buttons
    for button in buttons:
        if button == selected_button:
            pygame.draw.rect(screen, selected_button_color, button)
            text_color = selected_button_text_color
        else:
            pygame.draw.rect(screen, button_color, button)
            text_color = button_text_color

        # Draw the button value text
        text_surface = font.render(
            str(button_values[buttons.index(button)]), True, text_color
        )
        text_rect = text_surface.get_rect(center=button.center)
        screen.blit(text_surface, text_rect)

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
