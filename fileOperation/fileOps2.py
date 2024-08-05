# 2. Read and display the content of a file

with open('newfileOps1.txt', 'r') as file:
    content = file.read()
    print(content)