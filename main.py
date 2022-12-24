import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pydoku")

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


class Cell:
    def __init__(
        self,
        r,
        c,
        width=cell_size,
        height=cell_size,
        kind=None,
        a_value=None,  # Answer value
        c_value=None,  # Corner value
        m_value=None,  # Middle value
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
        self.a_value = a_value
        self.c_value = c_value
        self.m_value = m_value
        self.selected = False
        self.number_color = number_color

    def draw(self, surface):
        # Draw the cell outline
        pygame.draw.rect(
            surface,
            grid_color,
            (self.x, self.y, self.width, self.height),
            line_width,
        )

        # Draw the number - answer value takes priority over corner/middle
        if self.a_value != None:
            # Render the text
            text = font.render(str(self.a_value), True, self.number_color)
            # Calculate the position of the text
            text_x = self.x + (self.width - text.get_width()) / 2
            text_y = self.y + (self.height - text.get_height()) / 2
            # Draw the text
            screen.blit(text, (text_x, text_y))

        else:
            if self.c_value != None:
                # Render the text
                text = font.render(str(self.c_value), True, number_color)
                # Calculate the position of the text
                text_x = self.x + (self.width - text.get_width()) / 2
                text_y = self.y + (self.height - text.get_height()) / 2
                # Draw the text
                screen.blit(text, (text_x, text_y))
            if self.m_value != None:
                # Render the text
                text = font.render(str(self.m_value), True, number_color)
                # Calculate the position of the text
                text_x = self.x + (self.width - text.get_width()) / 2
                text_y = self.y + (self.height - text.get_height()) / 2
                # Draw the text
                screen.blit(text, (text_x, text_y))

    def check_valid(self):
        self.box_c = (self.c - 1) // 3
        self.box_r = (self.r - 1) // 3
        box_values = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}
        print(f"Box C: {self.box_c}, Box R: {self.box_r}")
        # Find the cells that make up the box, row, and col
        self.full_box = []
        self.full_row = []
        self.full_col = []
        for col in box_values[self.box_c]:
            for row in box_values[self.box_r]:
                if (
                    col != self.c or row != self.r
                ):  # shouldnt this be an 'and'?
                    self.full_box.append((col - 1, row - 1))
        # print(f"box: {self.full_box}")
        for col in range(1, 10):
            if col != self.c:
                self.full_row.append((col - 1, self.r - 1))
        # print(f"row: {self.full_row}")
        for row in range(1, 10):
            if row != self.r:
                self.full_col.append((self.c - 1, row - 1))
        # print(f"col: {self.full_col}")
        cells_to_check = set(self.full_box + self.full_row + self.full_col)
        for cell in cells_to_check:
            if full_grid[cell[0]][cell[1]].a_value == self.a_value:
                self.number_color = (255, 0, 0)
                return "ERROR! Cell clashes!"
            else:
                self.number_color = number_color
        return None


class Button:
    def __init__(
        self, x, y, width=cell_size, height=cell_size, kind="Number", label="X"
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kind = kind
        self.label = label
        self.selected = False
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        if self.kind == "Number":
            if self.selected:
                pygame.draw.rect(surface, selected_button_color, self.button)
                text_color = selected_button_text_color
            else:
                pygame.draw.rect(surface, button_color, self.button)
                text_color = button_text_color

            # Draw the button value text
            self.text_surface = font.render(str(self.label), True, text_color)
            self.text_rect = self.text_surface.get_rect(
                center=self.button.center
            )
            screen.blit(self.text_surface, self.text_rect)


# Create the buttons
buttons = []
for value in button_values:
    buttons.append(
        Button(
            x=button_x,
            y=button_y,
            width=cell_size,
            height=cell_size,
            kind="Number",
            label=value,
        )
    )
    # Update the x coordinate for the next button
    button_x += button_size[0] + 10

# # Create the buttons
# buttons = []
# for value in button_values:
#     # Create the button
#     button = pygame.Rect(button_x, button_y, button_size[0], button_size[1])
#     buttons.append(button)

#     # Update the x coordinate for the next button
#     button_x += button_size[0] + 10

#     # Set the selected button
#     selected_button = None

# button_x = 50
# button_y += cell_size + margin

# mode_button_values = ["A", "C", "M"]
# mode_buttons = []
# for value in mode_button_values:
#     button = pygame.Rect(button_x, button_y, button_size[0], button_size[1])
#     mode_buttons.append(button)

# # Update the x coordinate for the next button
# button_x += button_size[0] + 10

# # Set the selected button
# selected_button = None

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
                if button.button.collidepoint(event.pos):
                    # Set the selected button
                    # selected_button = button
                    if button.selected == True:
                        button.selected = False
                        value = None
                    else:
                        for other_button in buttons:
                            other_button.selected = (
                                False  # Deselect all buttons
                            )
                        button.selected = True  # Select this button
                        value = button.label
                    break
            # Get the mouse position
            mouse_x, mouse_y = event.pos
            # Calculate the cell that was clicked
            cell_x = mouse_x // (cell_size + margin)
            cell_y = mouse_y // (cell_size + margin)
            if cell_x < 10 and cell_y < 10:
                print(cell_x + 1, cell_y + 1)
                # Update the cell with a value
                # update_cell(cell_x, cell_y, 5)
                full_grid[cell_x][cell_y].a_value = value
                print(full_grid[cell_x][cell_y].check_valid())

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background
    screen.fill(bg_color)

    # Draw the grid
    for col in range(1, 10):
        for row in range(1, 10):
            full_grid[row - 1][col - 1].draw(screen)

    # Draw the buttons
    for button in buttons:
        button.draw(screen)

    # for button in mode_buttons:
    #     if button == selected_button:
    #         pygame.draw.rect(screen, selected_button_color, button)
    #         text_color = selected_button_text_color
    #     else:
    #         pygame.draw.rect(screen, button_color, button)
    #         text_color = button_text_color

    #     # Draw the button value text
    #     text_surface = font.render(
    #         str(mode_button_values[mode_buttons.index(button)]),
    #         True,
    #         text_color,
    #     )
    #     text_rect = text_surface.get_rect(center=button.center)
    #     screen.blit(text_surface, text_rect)

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
