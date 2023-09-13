print("1 add /n 2 sub /n 3 multi /n 4 div")
a=int(input("choose the no."))
x=int(input("enter the no.1"))
y=int(input("enter the no.2"))
if   a==1:
    result=x+y
    print("result")
elif a==2:
    result=x-y
    print("result")
elif a==3:
    result=x*y
    print("result")
elif a==4:
    result=x%y
    print('result')

else:
      print('invalid')
