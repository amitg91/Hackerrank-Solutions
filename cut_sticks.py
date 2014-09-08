# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input()
h = [int(x) for x in raw_input().split()]
while 1:
    if len(h)>0:
        print len(h)
        h.sort()
        h=filter((lambda x: x > 0), map((lambda x: x-h[0]), h))
	
    else:
        break
