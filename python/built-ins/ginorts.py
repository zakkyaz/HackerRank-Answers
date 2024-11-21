S = list(input())
S.sort(key=lambda x: (
    x.isdigit(),
    not x.islower(),
    int(x) % 2 == 0 if x.isdigit() else False,
    x
))
print("".join(S))
