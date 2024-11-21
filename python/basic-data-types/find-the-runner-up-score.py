if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
c = list(arr)
c.sort(reverse=True)
for x in c:
    if x != max(c):
        runner = x
        break
print(runner)
