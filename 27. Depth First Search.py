graph={'a':['b','c','d'],'b':['e','f'],'c':['g'],'d':['h','i','j'],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop()
        newelement(m)

def newelement(m):
    for i in graph[m]:
        if i not in visited:
            visited.append(i)
            queue.append(i)


bfs(visited,graph,'a')
print(visited)