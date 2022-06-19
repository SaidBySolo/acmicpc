from queue import LifoQueue

q: LifoQueue[str] = LifoQueue()

for i in ["c=", "c-", "d-", "lj", "nj", "s=", "z=", "dz="]:
    q.put(i)

c = input()
rc = 0

while not q.empty():
    i = q.get(True)
    if i in c:
        c = c.replace(i, "|", 1)
        rc += 1
        if i in c:
            q.put(i)

c = c.replace("|", "")
print(rc + len(list(c)))
