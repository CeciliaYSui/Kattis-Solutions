class Graph:       
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
        visited[v] = True  
        temp.append(v) 
        for i in self.adj[v]: 
            if visited[i] == False: 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
  
g = Graph(5); 
g.addEdge(1,0) 
g.addEdge(1,2) 
g.addEdge(3,4)
g.addEdge(4,1)
cc = g.connectedComponents() 
print(len(cc))