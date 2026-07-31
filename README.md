# Visual Comparison of Pathfinding Algorithms

Run **six** maze solvers on the *same* maze at once and watch them race in a 3×2 grid: single-source **BFS / DFS / A\***, and their **bidirectional (dual)** versions that search from the start and goal simultaneously.

Built with Python + Pygame.

## Why

Reading pseudocode doesn't show *how differently* these algorithms explore. Running them side-by-side on one maze makes the trade-offs obvious:

- **BFS** — expands level by level, guarantees the shortest path, explores a lot.
- **DFS** — dives deep first, fast to move but rarely optimal.
- **A\*** — Manhattan heuristic pulls the search toward the goal, expanding far fewer cells.
- **Dual (bidirectional)** — two frontiers grow from start and goal and meet in the middle, usually visiting fewer cells than the single-source version.

## Layout

```
main.py                        # Generate maze, run all 6 algorithms, launch visualizer
maze_generator.py              # Recursive-backtracker maze + loops
visualizer.py                  # 3x2 side-by-side pygame animation
BFS_Breath_First_Search.py     # single-source BFS
DFS_Depth_First_Search.py      # single-source DFS
Astar.py                       # single-source A*
Dual_BFs.py                    # bidirectional BFS
Dual_DFS.py                    # bidirectional DFS
Dual_Astar.py                  # bidirectional A*
requirements.txt
```

## Run

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

Enter a maze size when prompted (e.g. `31`). A window opens with all six searches animating together, then each panel holds its final green path.

## Color key

| Color | Meaning |
|-------|---------|
| Black | Wall |
| White | Open path |
| Red | Start / goal |
| Blue | Visited (start side) |
| Purple | Visited (goal side, dual search) |
| Orange | Current node (start side) |
| Yellow | Current node (goal side, dual search) |
| Green | Final path |

## Notes

- Odd maze sizes carve most cleanly with the recursive backtracker.
- `open_area_5x5` clears a pocket around the start and goal so they're always reachable.
- Frame speed is uncapped (`clock.tick(0)`); lower it in `visualizer.py` if the animation is too fast on your machine.

## Related

A follow-up project drives a physical **ESP32-S3 + L298N** robot along the solved path:
[pathfinding-visualizer](https://github.com/AniketT0008/pathfinding-visualizer)
