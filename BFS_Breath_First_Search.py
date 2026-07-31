def solve_maze_BFS(size, maze, start, goal):

    queue = [start]
    visited = set([start])
    parent = {}

    frames = []

    def valid(x, y):
        return 0 <= x < size and 0 <= y < size and maze[x][y] == 0

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:

        x, y = queue.pop(0)

        frames.append((set(visited), set(), (x, y), None))

        if (x, y) == goal:
            break

        for dx, dy in dirs:

            nx, ny = x+dx, y+dy

            if valid(nx, ny) and (nx, ny) not in visited:

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    if goal not in parent:
        return frames, None

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    return frames, path
