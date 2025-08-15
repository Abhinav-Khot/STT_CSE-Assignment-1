from string import ascii_uppercase as UP

s = input()

nos = [0] * 26

for x in s:
    nos[ord(x) - ord('A')] += 1

prev = 'a'
ans = []

for i in range(len(s)):
    possible = ""
    found = False
    for j in range(26):
        if not found and UP[j] != prev and nos[j] > 0:
            possible = UP[j]
            found = True
        if nos[j] > (len(s) - i) // 2:  # will become impossible
            possible = UP[j]

    if possible == "":
        print(-1)
        break

    ans.append(possible)
    nos[ord(possible) - ord('A')] -= 1
    prev = possible
else:
    for i in range(len(s) - 1):
        if ans[i] == ans[i + 1]:
            print(-1)
            break
    else:
        print("".join(ans))
