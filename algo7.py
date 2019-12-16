# Algo 7
# DFS 그래프 기초 및 실습

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


def dfs():
    visited_list = list()
    will_visit_stack = list()

    will_visit_stack.append('A')

    while will_visit_stack:
        if will_visit_stack[-1] not in visited_list:
            visited_list.append(will_visit_stack[-1])
            will_visit_stack.extend(graph[will_visit_stack.pop()])
        else:
            will_visit_stack.pop()
    print(visited_list)


dfs()




