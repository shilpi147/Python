s="the problem with india is the problem with the people"
d={}
p=s.split()
print(p)
for i in p:
    c=p.count(i)
    d[i]=c
print(d)
p[-1]="PM"
print(' '.join(p))


