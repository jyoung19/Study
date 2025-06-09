1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26

	
def solution(abba):
    answer = 0

    f=0
    t = []
    for i in abba:

        a = i
        b=a.replace("aya","1")
        c=b.replace("ye","1")
        d=c.replace("woo","1")
        e=d.replace("ma","1")
        t.append(e)
    a=0
    b=len(t)
    e=0
##    z = "1112323"
    for z in t:
        d = 0
        for i in z:
            if i == "1":
                d=d+1
        if d==len(z):
            e=e+1
    answer=e
    return answer
