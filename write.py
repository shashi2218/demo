with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)

    with open('test.txt', 'w') as writter:
        for line in reversed(content):
          writter.write(line)


