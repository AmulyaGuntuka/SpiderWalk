import pygame
import sys
import turtle
import math
from collections import deque, defaultdict

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('final_spider_sound.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
screen = pygame.display.set_mode((980, 980))

# Start menu function
def start_menu():
    pygame.display.set_caption("WELCOME TO CHARLOTTE'S HOME")
    font = pygame.font.SysFont("Black Chancery", 42)
    spider_background = pygame.image.load('spider_background2.jpg')
    title = font.render("WELCOME TO CHARLOTTE'S HOME", True, (255, 255, 255))
    screen.blit(spider_background, (0, 0))
    screen.blit(title, (270, 200))
    font = pygame.font.SysFont('Black Chancery', 60)
    game_logo = pygame.image.load('spider_logo2.png')
    screen.blit(game_logo, (245, 245))
    start_text = font.render("START", True, (255, 0, 0, 255))
    start_button = pygame.rect.Rect((150, 700), (170, 60))
    pygame.draw.rect(screen, (255, 255, 255), start_button, 0, 5)
    screen.blit(start_text, (170, 710))
    exit_text = font.render("QUIT", True, (255, 0, 0, 255))
    exit_button = pygame.rect.Rect((600, 700), (170, 60))
    pygame.draw.rect(screen, (255, 255, 255), exit_button, 0, 5)
    screen.blit(exit_text, (635, 710))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "yes"
                elif exit_button.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

# Instructions screen with input fields for n, m, s
def instructions():
    font = pygame.font.SysFont('Black Chancery', 60)
    input_font = pygame.font.SysFont('Black Chancery', 40)
    small_font = pygame.font.SysFont('Black Chancery', 30)
    spider_background = pygame.image.load('spider_background2.jpg')
    screen.blit(spider_background, (0, 0))

    # Instructional text
    surface = font.render("Enter values for n, m, s", True, (255, 255, 255))
    screen.blit(surface, (270, 180))

    n_instruction = small_font.render("n: enter strands", True, (255, 255, 255))
    m_instruction = small_font.render("m: enter bridges", True, (255, 255, 255))
    s_instruction = small_font.render("s: enter favorite strand", True, (255, 255, 255))
    screen.blit(n_instruction, (270, 280))
    screen.blit(m_instruction, (270, 380))
    screen.blit(s_instruction, (270, 480))

    # Input boxes
    input_box_n = pygame.rect.Rect((500, 280), (200, 50))
    input_box_m = pygame.rect.Rect((500, 380), (200, 50))
    input_box_s = pygame.rect.Rect((500, 480), (200, 50))

    # Submit and Quit buttons
    submit_button = pygame.rect.Rect((200, 600), (200, 50))
    quit_button = pygame.rect.Rect((600, 600), (200, 50))
    submit_text = font.render("GO!", True, (255, 0, 0, 255))
    quit_text = font.render("Quit", True, (255, 0, 0, 255))

    # Initial text and button colors
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    # Text input
    active_box = None
    text_n = ''
    text_m = ''
    text_s = ''
    txt_surface_n = input_font.render(text_n, True, color)
    txt_surface_m = input_font.render(text_m, True, color)
    txt_surface_s = input_font.render(text_s, True, color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_n.collidepoint(event.pos):
                    active_box = 'n'
                elif input_box_m.collidepoint(event.pos):
                    active_box = 'm'
                elif input_box_s.collidepoint(event.pos):
                    active_box = 's'
                elif submit_button.collidepoint(event.pos):
                    try:
                        n = int(text_n)
                        m = int(text_m)
                        s = int(text_s)
                        return n, m, s
                    except ValueError:
                        continue
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                else:
                    active_box = None
                color = color_active if active_box else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active_box == 'n':
                    if event.key == pygame.K_BACKSPACE:
                        text_n = text_n[:-1]
                    else:
                        text_n += event.unicode
                    txt_surface_n = input_font.render(text_n, True, color)
                elif active_box == 'm':
                    if event.key == pygame.K_BACKSPACE:
                        text_m = text_m[:-1]
                    else:
                        text_m += event.unicode
                    txt_surface_m = input_font.render(text_m, True, color)
                elif active_box == 's':
                    if event.key == pygame.K_BACKSPACE:
                        text_s = text_s[:-1]
                    else:
                        text_s += event.unicode
                    txt_surface_s = input_font.render(text_s, True, color)

        # Redraw the background and input boxes
        screen.blit(spider_background, (0, 0))
        screen.blit(surface, (270, 150))
        screen.blit(n_instruction, (270, 280))
        screen.blit(m_instruction, (270, 380))
        screen.blit(s_instruction, (270, 480))
        screen.blit(txt_surface_n, (input_box_n.x + 20, input_box_n.y + 0))
        pygame.draw.rect(screen, color, input_box_n, 2)
        screen.blit(txt_surface_m, (input_box_m.x + 20, input_box_m.y + 0))
        pygame.draw.rect(screen, color, input_box_m, 2)
        screen.blit(txt_surface_s, (input_box_s.x + 20, input_box_s.y + 0))
        pygame.draw.rect(screen, color, input_box_s, 2)
        pygame.draw.rect(screen, (255, 255, 255), submit_button, 0, 5)
        screen.blit(submit_text, (submit_button.x + 60, submit_button.y + 10))
        pygame.draw.rect(screen, (255, 255, 255), quit_button, 0, 5)
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        pygame.display.update()

# Function to input bridge details
def input_bridges(m):
    font = pygame.font.SysFont('Black Chancery', 40)
    small_font = pygame.font.SysFont('Black Chancery', 30)
    spider_background = pygame.image.load('spider_background2.jpg')
    screen.blit(spider_background, (0, 0))

    # Instructional text
    instruction = small_font.render(f"Enter details for {m} bridges", True, (255, 255, 255))
    screen.blit(instruction, (300, 300))

    # Input boxes for bridge details
    bridge_boxes = [pygame.Rect((300, 200 + i * 60), (100, 50)) for i in range(m)]  # Distance
    strand_boxes = [pygame.Rect((500, 200 + i * 60), (100, 50)) for i in range(m)]  # Strand

    # Submit and Quit buttons
    submit_button = pygame.Rect((200, 200 + m * 60 + 100), (200, 50))
    quit_button = pygame.Rect((600, 200 + m * 60 + 100), (200, 50))
    submit_text = font.render("Submit", True, (255, 0, 0, 255))
    quit_text = font.render("Quit", True, (255, 0, 0, 255))

    # Initial text and button colors
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive

    # Text input
    active_box = None
    bridge_inputs = [''] * m
    strand_inputs = [''] * m
    bridge_surfaces = [font.render(text, True, color) for text in bridge_inputs]
    strand_surfaces = [font.render(text, True, color) for text in strand_inputs]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos):
                    try:
                        bridges = [(int(bridge_inputs[i]), int(strand_inputs[i])) for i in range(m)]
                        return bridges
                    except ValueError:
                        continue
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                
                # Check which input box was clicked
                for i, box in enumerate(bridge_boxes):
                    if box.collidepoint(event.pos):
                        active_box = ('bridge', i)
                        break
                for i, box in enumerate(strand_boxes):
                    if box.collidepoint(event.pos):
                        active_box = ('strand', i)
                        break
                
                if active_box is None:
                    color = color_inactive
                else:
                    color = color_active
                for i, _ in enumerate(bridge_boxes):
                    if active_box == ('bridge', i):
                        color = color_active
                        break
                for i, _ in enumerate(strand_boxes):
                    if active_box == ('strand', i):
                        color = color_active
                        break
                
            elif event.type == pygame.KEYDOWN:
                if active_box:
                    box_type, index = active_box
                    if box_type == 'bridge':
                        if event.key == pygame.K_BACKSPACE:
                            bridge_inputs[index] = bridge_inputs[index][:-1]
                        else:
                            bridge_inputs[index] += event.unicode
                        bridge_surfaces[index] = font.render(bridge_inputs[index], True, color)
                    elif box_type == 'strand':
                        if event.key == pygame.K_BACKSPACE:
                            strand_inputs[index] = strand_inputs[index][:-1]
                        else:
                            strand_inputs[index] += event.unicode
                        strand_surfaces[index] = font.render(strand_inputs[index], True, color)
                    if event.key == pygame.K_RETURN:
                        try:
                            bridges = [(int(bridge_inputs[i]), int(strand_inputs[i])) for i in range(m)]
                            return bridges
                        except ValueError:
                            continue

        # Redraw the background and input boxes
        screen.blit(spider_background, (0, 0))
        screen.blit(instruction, (300, 150))
        for i, box in enumerate(bridge_boxes):
            screen.blit(bridge_surfaces[i], (box.x + 20, box.y + 10))
            pygame.draw.rect(screen, color, box, 2)
        for i, box in enumerate(strand_boxes):
            screen.blit(strand_surfaces[i], (box.x + 20, box.y + 10))
            pygame.draw.rect(screen, color, box, 2)
        pygame.draw.rect(screen, (255, 255, 255), submit_button, 0, 5)
        screen.blit(submit_text, (submit_button.x + 60, submit_button.y + 10))
        pygame.draw.rect(screen, (255, 255, 255), quit_button, 0, 5)
        screen.blit(quit_text, (quit_button.x + 70, quit_button.y + 10))

        pygame.display.update()


def turtleFunction(n, m,s, bridges):
    turtle.setup(width=980, height=720)
    screen = turtle.Screen()
    screen.bgpic("turtlebck2.gif")
    myturtle = turtle.Turtle()
    myturtle.pensize(2)
    myturtle.color("white")
    turtle.register_shape("5Gp9.gif")
    myturtle.shape("5Gp9.gif")
    myturtle.shapesize(2, 2)
    
    angle = 360 / n
    side = 200
    length = 10
    a = side / length
    myturtle.setheading(0)

    # Drawing strands
    for i in range(n):
        myturtle.penup()
        myturtle.goto(0, 0)
        myturtle.pendown()
        myturtle.forward(side)
        myturtle.penup()
        myturtle.goto(0, 0)
        myturtle.left(angle)

    # Drawing bridges
    for bridge in bridges:
        d, t = bridge
        myturtle.penup()
        myturtle.goto(0, 0)
        myturtle.setheading((t - 1) * angle)
        myturtle.forward(d * a)
        myturtle.pendown()
        myturtle.left(90)
        radius = d * a
        myturtle.circle(radius, angle)
    
    # Display message about the shortest path button
    myturtle.penup()
    myturtle.goto(-400, -300)
    myturtle.write("Press 'P' to display the shortest path", font=("Arial", 18, "normal"))
    myturtle.hideturtle()

    # Adding a key press event to display the shortest path
    screen.listen()
    screen.onkey(lambda: display_shortest_path(n,m,s, bridges), "p")

    turtle.mainloop()  # Use mainloop instead of done to keep the window open

# bfs - function to calculate shortest path using BFS
def bfs(n, bridges, start, target):
    adjacency_list = defaultdict(list)
    
    # Build the graph from the bridges
    for d, t in bridges:
        adjacency_list[d].append(t)
        adjacency_list[t].append(d)  # Since it's a bidirectional bridge

    # BFS to find the shortest path
    queue = deque([(start, [start])])  # (current_strand, path_taken)
    visited = set([start])

    while queue:
        current_strand, path = queue.popleft()

        # If we've reached the target, return the path
        if current_strand == target:
            return path

        # Explore neighbors
        for neighbor in adjacency_list[current_strand]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found

def display_shortest_path(n, m,s,bridges):
    turtle.clearscreen()
    turtle.setup(width=980, height=720)
    screen = turtle.Screen()
    screen.bgpic("turtlebck2.gif")
    myturtle = turtle.Turtle()
    myturtle.pensize(3)
    myturtle.color("green")
    
    angle = 360 / n
    side = 200
    length = 10
    a = side / length

    # Set the start and target strand for shortest path calculation
    start_strand = 1  # For example, start from strand 1
    target_strand = s # For example, target is strand n

    # Get the shortest path using BFS
    shortest_path = bfs(n, bridges, start_strand, target_strand)

    if shortest_path is None:
        myturtle.penup()
        myturtle.goto(0, 0)
        myturtle.write("No path found", font=("Arial", 18, "normal"))
        myturtle.hideturtle()
        return

    # Draw the shortest path in green
    myturtle.penup()
    myturtle.goto(0, 0)
    for i in range(len(shortest_path) - 1):
        d = shortest_path[i]
        t = shortest_path[i + 1]
        
        myturtle.setheading((d - 1) * angle)
        myturtle.forward(a * 10)  # Adjust to fit your scale
        myturtle.pendown()
        myturtle.forward(a * 10)  # Adjust to fit your scale
        myturtle.penup()
    
    myturtle.hideturtle()

# Main execution
if __name__ == "__main__":
    start = start_menu()
    if start == "yes":
        n, m, s = instructions()
        bridges = input_bridges(m)
        # Ensure Pygame window is properly closed before starting Turtle graphics
        pygame.quit()
        turtleFunction(n, m, s,bridges)
