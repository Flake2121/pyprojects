import math
o=False
n=1
i=2
d=int(input("accuracy: "))
c=0
while True:
    i+=4
    if o:
        n += 1/(i/2)
    else:
        n -= 1/(i/2)
    o = not o
    if round(n*4,d) == round(math.pi,d):
        print("calculated pi: ",n*4)
        print("actual pi    : ",math.pi)
        break
