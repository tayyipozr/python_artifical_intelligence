adict = {}
with open("p1/graph.txt") as f:
    for line in f:
        letter = line[:1]
        adict2 = {}
        arr = line[3:-2].replace(" ", "").split(",")  # ["A:0","B:3"]
        for each in arr:
            if each[2:] != "0" and each[2:] != "":
                adict2[each[:1]] = each[2:]
        adict[letter] = adict2


def bfs(start, goal):
    paths = {}
    queue = [start]
    visited = [start]
    print("BFS : ", end="")
    while len(queue) > 0:
        queItem = queue.pop(0)
        if queItem == goal:
            break
        for way in adict[queItem]:
            if way not in visited:
                paths[way] = queItem
                queue.append(way)
                visited.append(way)
    path = findPath(paths, start, goal)
    print(path[0], end="")
    for item in path[1:]:
        print(" - " + item, end="")
    print()


def findPath(paths, start, end):
    path = [end]
    while path[-1] != start:
        path.append(paths[path[-1]])
    path.reverse()
    return path


visited_dfs = []
stack_dfs = []


def dfs(start, goal):
    stack_dfs.append(start)
    visited_dfs.append(start)
    goal_state = start
    if start == goal:
        print("DFS : ", end="")
        stack_dfs.pop(-1)
        for i in stack_dfs:
            print(i + " - ", end="")
        print(start)
    else:
        for node in adict[start]:
            if node not in visited_dfs:
                goal_state = node
        return dfs(goal_state, goal)

def ucs(start, goal):
    last_list = []
    visited = [start]
    cost = 0
    for item in adict[start]:
        if item not in visited:

bfs("A", "F")
dfs("A", "F")
ucs("A", "F")
ucs("A", "F")
