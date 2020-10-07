import numpy as geek

arr = geek.array([1 ,-5 ,3 ,2])

print("Input  array : \n", arr)

out_tpl = geek.nonzero(arr)
print("Indices of non zero elements : ", out_tpl)