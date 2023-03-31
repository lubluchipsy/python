from heapq import *
s = list(map(int, input().split()))
c = 0

for i in range(1, len(s)):
    if s[i] >= s[(i-1)//2]:
        ans = 'True'
    else:
        ans = 'False'
        break

print(ans)



