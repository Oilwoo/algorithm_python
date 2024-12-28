words = list(input())

rot13words = []
for word in words:
    if word.isupper():
        if ord(word) > ord('M'):
            word = chr(ord(word) - 13)
        else:
            word = chr(ord(word) + 13)
    if word.islower():
        if ord(word) > ord('m'):
            word = chr(ord(word) - 13)
        else:
            word = chr(ord(word) + 13)

    rot13words.append(word)

print(''.join(rot13words))

#영어의 알파벳 갯수는 26개
#ABCDEFGHIJKLM 
#M이 13번
#ROT13은 대문자/소문자 영문자를 13글자 앞 또는 뒤로 밀어서 만든 만든 새로운 문자열을 의미합니다.
#13번째 알파벳인 'M'을 기준으로 13을 더하면 'Z'이므로, 14번째 알파벳인 'N'은 13을 더하면 안 되고 'A'로 돌아가야 합니다.