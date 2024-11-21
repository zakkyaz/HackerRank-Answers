lines = [input() for _ in range(2)]
if all(num > 0 for num in list(map(int, lines[1].split()))) and any(string == string[::-1] for string in lines[1].split()): print(True)
else: print(False)
