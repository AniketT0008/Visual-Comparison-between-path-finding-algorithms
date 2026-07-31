def run_visual_multi(maze, algorithms_data):
    import pygame

    pygame.init()
    clock = pygame.time.Clock()

    # -------- AUTO-SCALE CELL SIZE --------
    TARGET_W = 1000
    TARGET_H = 700

    rows, cols = len(maze), len(maze[0])

    GRID_COLS = 3
    GRID_ROWS = 2

    CELL = min(
        TARGET_W // (cols * GRID_COLS),
        (TARGET_H - 10) // (rows * GRID_ROWS)   # leave room for titles
    )
    CELL = max(1, CELL)

    WIDTH = cols * CELL * GRID_COLS
    HEIGHT = rows * CELL * GRID_ROWS + 20 * GRID_ROWS  # space for titles

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    PURPLE = (160, 32, 240)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)

    FONT = pygame.font.SysFont("Arial", 16)

    running = True
    step = 0

    # -------- GLOBAL MAX STEPS --------
    max_steps = max(len(data["frames"]) for data in algorithms_data)

    def draw_grid(surface, frame, offset_x, offset_y, start, goal, path_set):
        visited_start = set()
        visited_end = set()
        current1 = None
        current2 = None

        if len(frame) == 0:
            pass
        elif len(frame) == 2:
            visited_start, current1 = frame
        elif len(frame) == 4:
            visited_start, visited_end, current1, current2 = frame

        for i in range(rows):
            for j in range(cols):

                color = WHITE if maze[i][j] == 0 else BLACK

                if (i, j) in visited_start:
                    color = BLUE
                if (i, j) in visited_end:
                    color = PURPLE

                if (i, j) == current1:
                    color = ORANGE
                if current2 and (i, j) == current2:
                    color = YELLOW

                if (i, j) == start or (i, j) == goal:
                    color = RED

                if (i, j) in path_set:
                    color = GREEN

                pygame.draw.rect(
                    surface,
                    color,
                    (offset_x + j * CELL, offset_y + i * CELL, CELL, CELL)
                )

    # -------- MAIN LOOP --------
    while running:

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for idx, data in enumerate(algorithms_data):

            frames = data["frames"]
            path = data["path"]
            start = data["start"]
            goal = data["goal"]
            title = data.get("title", f"Algo {idx+1}")

            # Clamp step to algorithm's frame count
            if step < len(frames):
                local_step = step
            else:
                local_step = len(frames) - 1
            frame = frames[local_step]

            # Only show path after algorithm finishes
            if local_step == len(frames) - 1:
                path_set = set(path) if path else set()
            else:
                path_set = set()

            # 3×2 layout
            col = idx % GRID_COLS
            row = idx // GRID_COLS

            x = col * cols * CELL
            y = row * (rows * CELL + 20)  # 20px title bar

            # Draw title
            text_surface = FONT.render(title, True, BLACK)
            screen.blit(text_surface, (x + 5, y))

            # Draw maze under title
            draw_grid(screen, frame, x, y + 20, start, goal, path_set)

        step += 1
        if step >= max_steps:
            step = max_steps - 1  # hold final frame

        pygame.display.update()
        clock.tick(0)
        

