adict = {}
with open("p1/graph.txt") as f:
    for line in f:
        letter = line[:1]
        adict2 = {}
        arr = line[3:-2].replace(" ", "").split(",")  # ["A:0","B:3"]
        for each in arr:
            if each[2:] != "0" and each[2:] != "":
                adict2[each[:1]] = int(each[2:])
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


cheapestPath = []
cheapestCost = 0
paths = {}


def ucs(start, goal):
    global cheapestCost
    global cheapestPath
    curPath = [start]
    curCost = 0
    visited = [start]
    while True:
        cheapestItem = None
        cost = 0
        # find cheapest goto that is not visited
        for item in adict[curPath[-1]]:
            if ','.join(curPath + [item]) not in list(paths.keys()) and (
                    cost == 0 or adict[curPath[-1]][item] < cost) and item not in visited:
                cost = int(adict[curPath[-1]][item])
                cheapestItem = item
                visited.append(item)

        if cost != 0:
            curCost += cost
            curPath.append(cheapestItem)

        if curPath == [start] or curPath == []:  # reached end, no path available
            break;

        if cost == 0 or curPath[-1] == goal:
            if ','.join(curPath) in list(paths.keys()):
                break
            paths[','.join(curPath)] = curCost
            ucs(start, goal)
            if curPath[-1] == goal and (curCost < cheapestCost or cheapestCost == 0):
                cheapestPath = curPath
                cheapestCost = curCost
            break

start_state = input("Please enter the start state : ")
goal_state = input("Please enter the goal state : ")

bfs(start_state, goal_state)
dfs(start_state, goal_state)
ucs(start_state, goal_state)
print("UCS : ", end="")
for i in range(len(cheapestPath) - 1):
    print(cheapestPath[i] + " - ", end="")
print(cheapestPath[-1])