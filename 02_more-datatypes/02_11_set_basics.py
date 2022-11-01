# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets: creates new set with elements that are in s and t   
# - Create a union of both sets: creates new set that contains all elements of s and t
s = {1, 2, 3, 4}
t = {3, 4, 5, 6}
u = s.intersection(t)      #elements found in both sets
print(u)
v = s.union(t)             #all elements from both sets, no duplicates
print(v)
s.update(t)    # elements of t are added to s
print(s)

x = {1, 2, 3, 4}
y = {2, 3, 8, 9}
x.update(y)
print(x)
