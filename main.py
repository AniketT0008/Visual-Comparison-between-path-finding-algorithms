from maze_generator import generate_perfect_maze, open_area_5x5
from visualizer import run_visual_multi

from BFS_Breath_First_Search import solve_maze_BFS
from DFS_Depth_First_Search import solve_maze_DFS
from Astar import astar

from Dual_BFs import solve_maze_dual_BFS
from Dual_DFS import solve_maze_dual_DFS
from Dual_Astar import solve_maze_dual_Astar

import sys
sys.setrecursionlimit(10000)


# ---------------- INPUT ----------------
size = int(input("Enter maze size: "))

maze = generate_perfect_maze(size)

start = (0, 0)
goal = (size - 1, size - 1)

open_area_5x5(maze, *start)
open_area_5x5(maze, *goal)


# ---------------- RUN ALGORITHMS ----------------

print("Running BFS...")
bfs_frames, bfs_path = solve_maze_BFS(size, maze, start, goal)

print("Running DFS...")
dfs_frames, dfs_path = solve_maze_DFS(size, maze, start, goal)

print("Running A*...")
astar_frames, astar_path = astar(size, maze, start, goal)

print("Running Dual BFS...")
dual_bfs_frames, dual_bfs_path = solve_maze_dual_BFS(size, maze, start, goal)

print("Running Dual DFS...")
dual_dfs_frames, dual_dfs_path = solve_maze_dual_DFS(size, maze, start, goal)

print("Running Dual A*...")
dual_astar_frames, dual_astar_path = solve_maze_dual_Astar(size, maze, start, goal)


# ---------------- PACKAGE FOR VISUALIZER ----------------

algorithms_data = [
    {"frames": bfs_frames, "path": bfs_path, "start": start, "goal": goal, "title": "BFS"},
    {"frames": dfs_frames, "path": dfs_path, "start": start, "goal": goal, "title": "DFS"},
    {"frames": astar_frames, "path": astar_path, "start": start, "goal": goal, "title": "A*"},
    {"frames": dual_bfs_frames, "path": dual_bfs_path, "start": start, "goal": goal, "title": "Dual BFS"},
    {"frames": dual_dfs_frames, "path": dual_dfs_path, "start": start, "goal": goal, "title": "Dual DFS"},
    {"frames": dual_astar_frames, "path": dual_astar_path, "start": start, "goal": goal, "title": "Dual A*"},
]


# ---------------- RUN VISUALIZER ----------------

run_visual_multi(maze, algorithms_data)
from pygame.time import delay
delay(2000)

