from string import ascii_uppercase as UP
s = input()

nos = [0] * 26

for x in s:
    nos[ord(x) - ord('A')] += 1

Prev = 'a'
ans = []

for i in range(len(s)):
    Possible = ""
    Found = False
    for j in range(26):
        if (not Found and UP[j] != Prev and nos[j] > 0):
            Possible = UP[j]
            Found = True
        if nos[j] > (len(s) - i) // 2:  # will become imposi
            Possible = UP[j]

    if Possible == "":
        print(-1)
        break

    ans.append(Possible)
    nos[ord(Possible) - ord('A')] -= 1
    Prev = Possible
else:
    for i in range(len(s) - 1):
        if ans[i] == ans[i + 1]:
            print(-1)
            break
    else:
        print("".join(ans))
