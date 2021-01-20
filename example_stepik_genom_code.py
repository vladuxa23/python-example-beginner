f = open('C:\\Users\\vlad_\\Desktop\\dataset_3363_2.txt', 'r')
a = f.read()
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
f.close()
f = open('C:\\Users\\vlad_\\Desktop\\new_dataset.txt', 'w')
new_dataset = ('')
for i in range(len(b)):
    new_dataset = str(new_dataset + (b[i]*int(c[i])))
f.write(str(new_dataset))
f.close()
