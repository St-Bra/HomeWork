with open("text.txt", "r", encoding="utf-8") as f:
    text_file = f.readlines()

res = {}

for i, string in enumerate(text_file, start=1):
    words = string.strip().split()
    word_cnt = {}
    for word in words:
        word_cnt[word] = word_cnt.get(word, 0) + 1
    res[f"String {i}: "] = word_cnt

with open("result.txt", "w", encoding='utf-8') as f:
    for i, (key, value) in enumerate(res.items(), start=1):
        cnt = 0
        seach_word = ""
        for key_word, value_cnt in value.items():
            if value_cnt > cnt:
                cnt = value_cnt
                seach_word = key_word
        f.write(f'In string {i} {seach_word}: {cnt}\n')