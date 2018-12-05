def divide_words(words):
    words += ' lst'
    l = []
    w = ''
    for i in words:
        if i == ' ':
            l.append(w)
            w = ''
        else:
            w += i
        
    return l

if __name__ == '__main__':
    j = 'mama ama kriminal hooligan'
    j = divide_words(j)
    print(j)
    f = j[1]
    print(f)
    print(type(f))
