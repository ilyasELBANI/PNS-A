def pgss(L):
    """
    L: a list of integers
    return: the longest increasing subsequence of L
    """
	S=[(0,L[0])]
	hist = {(0,L[0]) : None}

	for t in enumerate(L[1:]):
		a,b = 0,len(S)-1
		while a<=b:
			p = (a+b)//2
			if S[p][1]<t[1]:
				a=p+1
			else:
				b=p-1

		if a>=len(S):
			S.append(t)
		else:
			S[a] = t
		hist[t] = S[a-1] if a>0 else None

	v = S[-1]
	L = []
	while v is not None:
		L.append(v[1])
		v=hist[v]
	return L[::-1]