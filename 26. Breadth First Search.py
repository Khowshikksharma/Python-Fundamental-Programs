graph={'s':['a','d'],'a':['b'],'c':['g'],'d':['g'],'g':[],'b':['c','g']}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(" ",m,end=" ")
        newelement(m)

def newelement(m):
    for i in graph[m]:
        if i not in visited:
            visited.append(i)
            queue.append(i)


bfs(visited,graph,'s')