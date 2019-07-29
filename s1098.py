n=int(input())
for i in range(0,1):
  li=[int(x) for x in input().split()]
  
x=[]
for i in li:
  x.append(i)
x.sort()
for i in range(0,n):
  if(li[i]==x[i]):
    pass
  else:
    print(i)
    break
