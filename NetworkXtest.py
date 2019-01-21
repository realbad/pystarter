import networkx as nx
import matplotlib.pyplot as plt

def searchPath(graph, start, end):
    results = []
    _generatePath(graph, [start], end, results)
    results.sort(key=lambda x:len(x))
    return results

def _generatePath(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                # path.append(n)
                _generatePath(graph, path + [n], end, results)

def showPath(results):
    print('The path from' + results[0][0] + "to" + results[0][-1] + "is:")
    for path in results:
        print(path)


if __name__ == '__main__':
    graph = {
        '1': ['2', '3'],
        '2': ['3'],
        '3': ['4', '5', '6'],
        '4': ['1'],
        '5': ['5'],
        '6': ['7'],
        '7': ['7']
    }
    r=searchPath(graph, '1', '7')
    showPath(r)





