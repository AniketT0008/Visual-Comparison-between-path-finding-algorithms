def solve_maze_dual_DFS(size, maze, start, goal):

    stack1 = [start]
    stack2 = [goal]

    visited1 = set([start])
    visited2 = set([goal])

    parent1 = {}
    parent2 = {}

    frames = []
    meetpoint = None

    def valid(x, y):
        return 0 <= x < size and 0 <= y < size and maze[x][y] == 0

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while stack1 and stack2:

        # --- Forward DFS step ---
        x1, y1 = stack1.pop()
        visited1.add((x1, y1))

        # meetpoint check
        if (x1, y1) in visited2:
            meetpoint = (x1, y1)
            break

        # expand forward
        for dx, dy in dirs:
            nx, ny = x1 + dx, y1 + dy
            if valid(nx, ny) and (nx, ny) not in visited1:
                visited1.add((nx, ny))
                parent1[(nx, ny)] = (x1, y1)
                stack1.append((nx, ny))

        # --- Backward DFS step ---
        x2, y2 = stack2.pop()
        visited2.add((x2, y2))

        if (x2, y2) in visited1:
            meetpoint = (x2, y2)
            break

        # expand backward
        for dx, dy in dirs:
            nx, ny = x2 + dx, y2 + dy
            if valid(nx, ny) and (nx, ny) not in visited2:
                visited2.add((nx, ny))
                parent2[(nx, ny)] = (x2, y2)
                stack2.append((nx, ny))

        # record frame for visualization
        frames.append((set(visited1), set(visited2), (x1, y1), (x2, y2)))

    # no meetpoint
    if meetpoint is None:
        return frames, None

    # --- reconstruct forward path ---
    path1 = []
    node = meetpoint
    while node != start:
        path1.append(node)
        node = parent1[node]
    path1.append(start)
    path1.reverse()

    # --- reconstruct backward path ---
    path2 = []
    node = meetpoint
    while node != goal:
        path2.append(node)
        node = parent2[node]
    path2.append(goal)

    # combine (avoid double meetpoint)
    full_path = path1 + path2[1:]

    return frames, full_path
