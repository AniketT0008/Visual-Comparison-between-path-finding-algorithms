import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_maze_dual_Astar(size, maze, start, goal):

    rows, cols = len(maze), len(maze[0])

    pq1 = [(0, start)]
    pq2 = [(0, goal)]

    g_cost1 = {start: 0}
    g_cost2 = {goal: 0}

    came_from1 = {}
    came_from2 = {}

    closed1 = set()
    closed2 = set()

    frames = []
    meetpoint = None

    while pq1 and pq2:

        # --- Expand forward ---
        _, current1 = heapq.heappop(pq1)
        closed1.add(current1)

        # meetpoint check
        if current1 in closed2:
            meetpoint = current1
            break

        # --- Expand backward ---
        _, current2 = heapq.heappop(pq2)
        closed2.add(current2)

        if current2 in closed1:
            meetpoint = current2
            break

        frames.append((set(closed1), set(closed2), current1, current2))

        # neighbors
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

            # forward expansion
            nx, ny = current1[0] + dx, current1[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_g = g_cost1[current1] + 1
                if (nx, ny) not in g_cost1 or new_g < g_cost1[(nx, ny)]:
                    g_cost1[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(pq1, (f, (nx, ny)))
                    came_from1[(nx, ny)] = current1

            # backward expansion
            nx, ny = current2[0] + dx, current2[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_g = g_cost2[current2] + 1
                if (nx, ny) not in g_cost2 or new_g < g_cost2[(nx, ny)]:
                    g_cost2[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), start)
                    heapq.heappush(pq2, (f, (nx, ny)))
                    came_from2[(nx, ny)] = current2

    # no meetpoint
    if meetpoint is None:
        return frames, None

    # reconstruct forward path
    path1 = []
    node = meetpoint
    while node != start:
        path1.append(node)
        node = came_from1[node]
    path1.append(start)
    path1.reverse()

    # reconstruct backward path
    path2 = []
    node = meetpoint
    while node != goal:
        path2.append(node)
        node = came_from2[node]
    path2.append(goal)

    # combine
    full_path = path1 + path2[1:]

    return frames, full_path
