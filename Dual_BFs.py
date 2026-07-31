def solve_maze_dual_BFS(size, maze, start, goal):
    from collections import deque

    visited_start = set([start])
    visited_end = set([goal])

    queue1 = deque([start])
    queue2 = deque([goal])

    parent1 = {}
    parent2 = {}

    def is_valid(x, y):
        return (
            0 <= x < size and
            0 <= y < size and
            maze[x][y] == 0
        )

    frames = []
    meeting = None

    while queue1 and queue2:

        # --- Expand from START side ---
        x1, y1 = queue1.popleft()
        frames.append((set(visited_start), set(visited_end), (x1, y1), None))

        if (x1, y1) in visited_end:
            meeting = (x1, y1)
            break

        for nx, ny in [(x1+1,y1),(x1-1,y1),(x1,y1+1),(x1,y1-1)]:
            if is_valid(nx, ny) and (nx, ny) not in visited_start:
                visited_start.add((nx, ny))
                parent1[(nx, ny)] = (x1, y1)
                queue1.append((nx, ny))

        # --- Expand from GOAL side ---
        x2, y2 = queue2.popleft()
        frames.append((set(visited_start), set(visited_end), None, (x2, y2)))

        if (x2, y2) in visited_start:
            meeting = (x2, y2)
            break

        for nx, ny in [(x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)]:
            if is_valid(nx, ny) and (nx, ny) not in visited_end:
                visited_end.add((nx, ny))
                parent2[(nx, ny)] = (x2, y2)
                queue2.append((nx, ny))

    # --- No meeting found ---
    if meeting is None:
        return frames, []

    # --- Reconstruct path from start → meeting ---
    path_start = []
    node = meeting
    while node != start:
        path_start.append(node)
        node = parent1[node]
    path_start.append(start)
    path_start.reverse()

    # --- Reconstruct path from goal → meeting ---
    path_end = []
    node = meeting
    while node != goal:
        node = parent2[node]
        path_end.append(node)

    full_path = path_start + path_end
    return frames, full_path
