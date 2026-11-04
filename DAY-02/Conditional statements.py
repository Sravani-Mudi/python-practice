marks=46
if marks >=90:
    print("a")
elif marks>=80:
    print("b")
elif marks>=70:
    print("c")
elif marks>=60:
    print("d")
else:
    print("f")
    
number=15
if number%3==0:
    print("fizz")
elif number%5==0:
    print("buzz")
else:
    print("fizzbuzz")

#greatest among three numbers
a=int(input())
b=int(input())
c=int(input())
a,b,c=map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:print(c)
