def word_count(s):
    # Implement me.
    ignore = [
        '"', ':', ';', ',', '.', '-', '+', '=', 
        '/', '\\', '|', '[', ']', '{', '}', '(',
         ')', '*', '^', '&'
    ]

    count = dict()

    for word in s.split():
        word = word.lower()
        for char in ignore:
            word = word.replace(char, '')
        if len(word) == 0:
            return count
        if count.get(word):
            count[word] += 1
        else:
            count[word] = 1

    return count

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))