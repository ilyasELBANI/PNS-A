from functools import cmp_to_key
    
    def compute_convex_hull(pts):
        """
        pts: a list of tuple coordinates
        return: the list of the convex hull of all the points under a list of coordinates
        """
        def area(c1, c2, c3):
            return (c2[0] - c1[0]) * (c3[1] - c1[1]) - (c3[0] - c1[0]) * (c2[1] - c1[1])
    
        def is_inside(c1, c2, c3):
            a = area(c1, c2, c3)
            if a == 0:
                return max(c1[0], c2[0]) >= c3[0] >= min(c1[0], c2[0])
            else:
                return a > 0
    
        def dist(c1,c2):
            return ((c2[0]-c1[0])**2)+((c2[1]-c1[1])**2)
    
        pivot=min(pts, key=cmp_to_key(lambda c1,c2: c1[0]-c2[0] if c1[1]==c2[1] 
            else c1[1]-c2[1]))
        pts.remove(pivot)
        vertices=sorted(pts,key=cmp_to_key(lambda c1,c2: area(pivot,c2,c1)))
        hull = [pivot]
        yield hull
        idx=0
        for v in vertices:
            if len(hull) < 2:
                hull.append(v)
            else:
                ar = area(hull[-2], hull[-1], v)
                if ar==0:
                    hull[-1]=max(v,hull[-1],key=lambda x:dist(hull[-2],x))
                    continue
                while ar<=0 and len(hull)>1:
                    hull.pop()
                    ar=area(hull[-2], hull[-1], v)
                hull.append(v)
            yield hull
        hull.append(hull[0])
        return hull