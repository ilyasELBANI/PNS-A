def bellman_ford(n_edge, vertices, edges):

	lbl = {v:0 for v in vertices}

	for k in range(1,n_edge):
		for v in vertices:
			d=lbl[v]
			for n in edges[v]:
				d=min(d,lbl[n]+edges[v][n])
			lbl[v]=d

	return -min(lbl.values())