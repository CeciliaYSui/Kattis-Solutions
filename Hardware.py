from sys import stdin, stdout 
n = int(stdin.readline())
for i in range(n):
    d = dict.fromkeys([str(i) for i in range(10)], 0)
    stdout.write(stdin.readline())
    tmp = stdin.readline()
    stdout.write(tmp)
    tmp = int(tmp.split()[0])
    while(tmp):
        l = stdin.readline().split()
        if l[0] == "+":
            l = [int(i) for i in l[1:]]
            newl = "".join(map(str, list(range(l[0], l[1]+l[2], l[2]))))
            for i in newl: 
                d[i] += 1
            tmp -= ((l[1]-l[0])//l[2] + 1)
        else: 
            for i in l[0]:
                d[i] += 1
            tmp -= 1
    total = sum(d.values())
    stdout.write("\n".join("Make {} digit {}".format(v,k) for k, v in d.items()))
    stdout.write(("\nIn total %d digits\n" % total) if total > 1 else ("\nIn total %d digit\n" % total)) 