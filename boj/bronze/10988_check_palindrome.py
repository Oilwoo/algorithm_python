word = list(input())
word_reverse = list(reversed(word))

if word == word_reverse:
    print(1)
else:
    print(0)
    
# reverse는 list타입에서 제공하는 함수이다.
# reverse는 값을 반환하지 않고, 단순히 해당 list를 뒤섞어준다.
# reversed는 내장함수로, list에서 제공하는 함수가 아니다.
# reversed는 ‘reversed’ 객체를 반환한다.