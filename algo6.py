# Algo 6
# BFS 그래프 기초 및 실습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def bfs():
    visited_queue = []
    will_visit_queue = []

    visited_queue.append('A')

    for v in graph.values():
        will_visit_queue += v
    while len(will_visit_queue) != 0:
        if will_visit_queue[0] not in visited_queue:
            visited_queue.append(will_visit_queue[0])
            del will_visit_queue[0]
        else:
            del will_visit_queue[0]
    print(visited_queue)


bfs()
