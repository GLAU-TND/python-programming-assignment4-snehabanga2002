l=eval(input())
p=input()
t=[]
for i in l:
    if i.startswith(p):
       t.append(i)
    else:
       pass
print(t)
