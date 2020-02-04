g = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def dfs(graph, start):
    explored = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in explored:
            explored.add(v)
            for x in graph[v]:
                if x not in explored:
                    stack.append(x)
    return explored


print(dfs(g, "A"))
