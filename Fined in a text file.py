word = "hi"
with open("Paswords.txt", 'r') as p:
    lines = p.readlines()
    for line in lines:
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)