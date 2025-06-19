def solution(s):
    words = s.split(' ')  # 공백도 살리기 위해 split(' ') 사용
    result = []

    for word in words:
        new_word = ''
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        result.append(new_word)

    return ' '.join(result)
