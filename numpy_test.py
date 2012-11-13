from numpy import *

def pe(str):
    r = eval(str)
    print str, ':', r, type(r)

u = array( [1, 2, 3] )
print u, type(u)

v = arange(3)
print v, type(v)

pe('u+v')
pe('u*v')
pe('dot(u,v)')
pe('cross(u,v)')
pe('linalg.norm(v)')

A = arange(64)
A.shape = (8, 8)
print A, type(A)

B = zeros((8, 8))
print B, type(B)

C = ones((8, 8))
print C, type(C)

id = identity(8)
print id, type(id)

mid = matrix(id)
print mid, type(mid)

d = linalg.det(mid)
print d, type(d)

