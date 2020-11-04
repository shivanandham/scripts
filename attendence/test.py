f = open("data.txt", 'r')
data = f.readlines()
# for i in data:
#     print(i, end='')
print(data[0].rstrip(),end='')
print(data[1].rstrip(),end='')
# l = []
# num = input()
# l.append(num+'\n')
# apikey = input()
# l.append(apikey)
# f = open('data.txt', 'w')
# f.writelines(l)