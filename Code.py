import networkx as nx                           
import matplotlib.pyplot as plt                       

G = nx.Graph()

AB=float(input("Enter cost from A to B:"))
AC=float(input("Enter cost from A to C:"))                           
BC=float(input("Enter cost from B to C:"))
BD=float(input("Enter cost from B to D:"))          
CD=float(input("Enter cost from C to D:"))              

start1=input("Choose start state:" "\n" "1. A""\n" "2. B" "\n" "3. C ""\n" "4. D""\n")
end1=input("Choose end state:" "\n" "1. A""\n" "2. B" "\n" "3. C ""\n" "4. D""\n")            

G.add_weighted_edges_from([
    ('A', 'B', AB),
    ('A', 'C', AC),               
    ('B', 'C', BC),
    ('B', 'D', BD),         
    ('C', 'D', CD)
])            

def find_all_paths(graph, start1, end1, path=[]):                       
    
    path = path + [start1]
                    
    if start1 == end1:       
        return [path]
    
    paths = []                 
    for node in graph.neighbors(start1):
        
        
        if node not in path:                   
            new_paths = find_all_paths(graph, node, end1, path)
            for p in new_paths:
                paths.append(p)                                                                                    
    return paths

def path_cost(graph, path):                
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]['weight']              
    return cost

all_paths = find_all_paths(G, start1, end1)

min_cost = float('inf')                   
shortest_path = None
         
for p in all_paths:
    cost = path_cost(G, p)
    print(f"Path: {p}, Cost: {cost}")
    
    if cost < min_cost:
        min_cost = cost                                   
        shortest_path = p

print("\nShortest Path:", shortest_path)
print("Minimum Cost:", min_cost)

pos = nx.spring_layout(G)       
nx.draw(G, pos, with_labels=True, node_color='lightblue')                                     
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()                 