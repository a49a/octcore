# 广度优先遍历
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
    queue = [start]
    explored.add(start)
    while queue:
        vertex = queue.pop(0)
        for x in graph[vertex]:
            if x not in explored:
                explored.add(x)
                queue.append(x)
    return explored


if "__main__" == __name__:
    r = dfs(g, "A")
    print(r)
