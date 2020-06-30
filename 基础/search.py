def linear_search(li,val):
  for ind,v in enumerate(li):
    if  v==val:
      return ind
    else:
      return None

seq = ['one', 'two', 'three']
print(linear_search(seq,'one'))
