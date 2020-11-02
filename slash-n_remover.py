fr = open("Your_text.txt", 'r')
f = open("removed.txt",'w')
for i in fr:
    f.write(i.rstrip('\n'))