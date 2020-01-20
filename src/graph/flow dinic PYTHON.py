#From algorithmie efficace
    from collections import deque
    
    def dinic(graph, capacity, source, target):
    	assert (source!=target)
    	add_reverse_arcs(graph, capacity)
    	Q=deque()
    	total=0
    	n=len(graph)
    	flow=[[0]*n for u in range(n)]
    	while True:
    		Q.appendleft(source)
    		lev = [None]*n
    		lev[source]=0
    		while Q:
    			u=Q.pop()
    			for v in graph[u]:
    				if lev[v] is None and capacity[u][v] > flow[u][v]:
    					lev[v] = lev[u] + 1
    					Q.appendleft(v)
    		if lev[target] is None:
    			return flow, total
    		#UB = borne sup
    		UB = sum(capacity[source][v] for v in graph[source]) - total
    		total+= _dinic_step(graph, capacity, lev, flow, source, target, UB)
    
    def _dinic_step(graph, capacity, lev, flow, u, target, limit):
    	if limit <=0:
    		return 0
    	if u == target:
    		return limit
    	val = 0
    	for v in graph[u]:
    		residuel = capacity[u][v] - flow[u][v]
    		if lev[v] == lev[u] + 1 and residuel > 0:
    			z=min(limit, residuel)
    			aug = _dinic_step(graph, capacity, lev, flow, v, target, z)
    			flow[u][v]+=aug
    			flow[v][u]-=aug
    			val+=aug
    			limit-=aug
    		if val==0:
    			lev[u]=None #Sommet non frachissable à enlever
    		return val