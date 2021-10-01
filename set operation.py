n = int(input())
s = set(map(int, input().split()))
c = int(input())
for x in range(0,c):
    r = input()
    v = r.strip().split(" ")

    if(v[0]=='pop'):
        s.pop()
    if(v[0]=='remove'):
        val = int(v[1])
        s.remove(val)
    if(v[0]=='discard'):
        val = int(v[1])
        s.discard(val)

print(sum(s))
