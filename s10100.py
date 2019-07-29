mystring=input()
a=[]
for i in mystring:
  i=int(i)
  a.append(i)
mul=1
for i in a:
  mul=mul*i
print(mul)
