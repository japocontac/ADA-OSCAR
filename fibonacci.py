print "ingrese cuantos números quiere ver"
n=input()
print "-------------------------------"
a=0
b=1
c=2
print a
print b
s=a+b

while c<n:
    c=c+1
    s=a+b
    a=b
    b=s
    print s

    if c==n:

        print "gracias"
