# http://blog.kzfmix.com/entry/1256559854
from numpy import *
inputs = array([[0,0],[0,1],[1,0],[1,1]])
targets = array([[0],[1],[1],[1]])

nIterations = 6
eta = 0.25
nData = shape(inputs)[0]
nIn = shape(inputs)[1]
nOut  = shape(targets)[1]
weights = random.rand(nIn+1,nOut)

inputs = concatenate((inputs,-ones((nData,1))),axis=1)

for i in range(nIterations):
    outputs = where(dot(inputs,weights)>0,1,0)
    weights += eta*dot(transpose(inputs),targets-outputs)
    print "Iter: %d" % i
    print weights

print "Final outputs are:"
print where(dot(inputs,weights)>0,1,0) 
