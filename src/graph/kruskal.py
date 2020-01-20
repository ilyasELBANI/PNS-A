def kruskal(edges):
	"""
	edges: is like [(n1,n2,weight),...]
	return: the total length of the minimum spanning tree
	"""

	parent = dict()
	rank = dict()

	def make_set(x):
		parent[x]=x
		rank[x]=0

	def union(x,y):
		gx,gy = find(x), find(y)
		if gx != gy:
			if rank[gx] < rank[gy]:
				parent[gx] = gy
			else:
				parent[gy] = gx
				if rank[gx] == rank[gy]:
					rank[gx]+=1

	def find(x):
		if parent[x]!=x:
			parent[x] = find(parent[x])
		return parent[x]

	for n1,n2,d in edges:
		make_set(n1)
		make_set(n2)

	edges = sorted(edges, key=lambda x:x[2])

	mst_l=0
	for n1,n2,d in edges:
		if find(n1) != find(n2):
			mst_l+=d
			union(n1,n2)
	return mst_l