def abc(l1,l2):
    res=False
    for i in l1:
        for j in l2:
           if i==j:
               res=True
        return res        
print(abc([1,11,22],[1,11,22]))
print(abc([2,3],[1,2,11,3,5,4]))
print(abc([2,3,5],[6,7,8]))
