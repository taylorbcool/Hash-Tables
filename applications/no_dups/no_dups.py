def no_dups(s):
    # Implement me.
    new_list = []
    words = dict()
    for string in s.split():
        if string not in words:
            words[string] = True
            new_list.append(string)
    return ' '.join(new_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))