import sys

if __name__ == '__main__':
    N = int(input())
    
    lines = [line.strip() for line in sys.stdin]
    arr = []

    for cmd in lines:
        cmdarr = cmd.split()
        if cmdarr[0] == 'append':
            arr.append(int(cmdarr[1]))
        elif cmdarr[0] == 'insert':
            arr.insert(int(cmdarr[1]), int(cmdarr[2]))
        elif cmdarr[0] == 'pop':
            arr.pop()
        elif cmdarr[0] == 'remove':
            arr.remove(int(cmdarr[1]))
        elif cmdarr[0] == 'reverse':
            arr.reverse()
        elif cmdarr[0] == 'sort':
            arr.sort()
        elif cmdarr[0] == 'print':
            print(arr)
