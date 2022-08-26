"""
Exercises given by Manoj sir in  the class
"""

def pr(a,b):
    print(f"Value {b}={a} and ID ={id(a)}")


def problem4():###
    def mystery(l):
        l = l[2:]
        return l
    mylist = [7,11,13,17,19,21]
    mystery(mylist)
    pr(mylist,'mylist')
problem4()

def problem5():
    def h(x):
        (d,n)=(1,0)
        while d <= x:
            (d,n) = (d*3,n+1)
        return(n)
    print(h(27993))

def problem6():
    def g(n):
        s=0
        for i in range(2,n):
            if n% i ==0:
                #pr(i,i)
                s=s+1
        return (s)
    print(g(60) - g(48))

def problem7():
    def f(n):
        s=0
        for i in range(1,n+1):
            if n//i == i  and n%i ==0:
                s=1
        return (s%2==1)
    print(f(8))
#composite numbers - A number that is divisible by a number other than 1 and the number itself, is called a composite number
#Prime numbers are the numbers that have only two factors, that are, 1 and the number itself

def problem8():
    def foo(m):
        if m==0:
            return(0)
        else:
            return ( m+ foo(m-1))
    print(foo(8))



def problem3(): #8a
    startmsg="anaconda"
    endmsg=""
    for i in range(1,1+len(startmsg)):
        endmsg = endmsg + startmsg[-i]
    print(endmsg)


def problem2():#3
    b=[43,99,65,105,4]
    a=b[2:]  #65,105,4
    d=b[1:] #99,65,105,4
    c=b #43,99,65,105,4

    d[1]=95  #99,95,105,4
    b[2]=47 #43,99,47,73,4
    c[3]=73 #43,99,65,73,4

    print(a[0]) #65
    print(b[3]) #73
    print(c[3]) #73
    print(d[1])#95
    print("#####")
    for i in range (1,9):
        print(i)


def Problem1():#st7
    x=[[3,5],"mismy",2,"borgrove",1] #statement1
    y=x[0:50] #statement2
    z=y
    w=x
    x[1]=x[1][:5] + 'ery'
    y[1]=4
    a12=w[1][:3]
    a12 +='fea' ####
    pr(a12,'a12')
    z[4]=42
    x[0][0]=555
    a=(x[3][1] == 1)


