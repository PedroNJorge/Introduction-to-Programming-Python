r, k = [int(num) for num in input().split(" ")]
g = input()

# padding g
g = "." + g + "."
g_copy = g

r = bin(r)[2:]
r = map(lambda x: "." if x == "0" else "#", "0"*(8-len(r)) + r)
r_ch = ""

for ch in r:
    r_ch += ch

dic = {"###": r_ch[0],
       "##.": r_ch[1],
       "#.#": r_ch[2],
       "#..": r_ch[3],
       ".##": r_ch[4],
       ".#.": r_ch[5],
       "..#": r_ch[6],
       "...": r_ch[7]}

for i in range(k):
    for j in range(1, len(g) - 1):
        change = g[j-1] + g[j] + g[j+1]
        g_copy = g_copy[:j] + dic[change] + g_copy[j+1:]
    g = g_copy
    print(g[1:-1])
