x=input("text goes here: ");c=0;a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(a)):
    if x[0]==a[i]:
        c=str(i+1)
print(str(c)+"th letter")
