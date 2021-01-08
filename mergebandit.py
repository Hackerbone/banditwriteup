filename = []

for i in range(3,24):
    filename.append(f"bandit{i}txt")

l = open("READM.md","a+")

for file in filename:
    with open(file,'r') as f:
        text = f.read()
        l.write(
            f"# {file}\n\n#### Password\n{text}\n\n================================================================\n\n")
