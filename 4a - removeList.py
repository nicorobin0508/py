color= ['red','green','white','black','pink','yellow']
c=[x for (i,x) in enumerate (color) if i not in(0,2,4,5)]
print(c)
