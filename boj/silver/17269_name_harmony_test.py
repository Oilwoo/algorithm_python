alphabet_strokes = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
    'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
    'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}
# 딕셔너리
# 딕서녀리 요소는 변수명['key'] 형태로 불러옴

N1, N2 = map(int, input().split())
name1, name2 = map(list, input().split())

for i, alpahbet in enumerate(name1):
    name1[i] = alphabet_strokes[alpahbet]

for i, alpahbet in enumerate(name2):
    name2[i] = alphabet_strokes[alpahbet]

names = []
if N1 < N2:
    for i in range(N1):
        names.append(name1[i])
        names.append(name2[i])
    for i in range(N1, N2, 1):
        names.append(name2[i])
else:
    for i in range(N2):
        names.append(name1[i])
        names.append(name2[i])
    for i in range(N2, N1, 1):
        names.append(name1[i])


while(len(names) > 2):
    new_names = []
    for i in range(len(names) - 1):
        result = names[i] + names[i+1]
        if result >= 10:
            result -= 10
        new_names.append(result)
    names = new_names

if names[0] == 0:
    names[0] = ''
print(f"{names[0]}{names[1]}%")
