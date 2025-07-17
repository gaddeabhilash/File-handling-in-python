#data comparitive deletion
with open("log.txt", 'r') as f:
    lines=f.readlines()
with open("log.txt",'w') as f:
    for line in lines:
        if line.strip()!= '7':
            f.write(line)