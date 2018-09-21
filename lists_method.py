l = [1,3,5]
s = [2,4,6]

c = s + l
print(c)
e ='a b c d z'
d ='a b c d e f g h'
c = d.split()
print(c)

if e in d:
    print('Yes')
else:
    print('No')

for i in c:
    print(i)

q = [7,3,5,1,2,13,17]
q.sort()
print(q)
q.reverse()
print(q)

print(q.count(13))
print(q.index(3))
print(len(q))
print(max(q))
print(min(q))
