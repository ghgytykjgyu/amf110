month=int(input ("enter month  :"))
name=(input("enter the name :"))

school=(input("enter school name :"))
year=int(input ("enter year  :"))
month=int(input ("enter month  :"))
day=int(input ("enter day  :"))
sum=0
sublist=["math","scince","arbic","english","art","history","computer"]
d1=[100,80,100,100,30,60,30]
v=[]
t=[]
d=[]

def y(d,fd):
    return(d/fd)*100

def grade(p):
    if 85<=p<=100:
        x="a"
    elif 70<=p<85:
        x="b"
    elif 60<=p<70:
        x="c"
    elif 50<=p<60:
        x="d"
    elif p<50:
       x="f"
    return(x)
      
def age(year1):
    print("age=",year1-year)
age(2023)

for i in range(7):
    p=int(input(f"enter the {sublist[i]} d :"))
    d.append(p)
    c= y(d[i],d1[i])
    v.append(c)
    marwan = grade(c)
    t.append(marwan)
    sum=sum+p    

z= y(sum,500)
marwan1 = grade(z)

print("name=",name)     
print("schoolName=",school)
print(v)
print(t)
print(sum)
print(z)
print(marwan1)

print("------------------------------------------------------------------------")
print("subject\t\t\t\t\tmark")
print("------------------------------------------------------------------------")

print("math\t\t\t\t\t",d[0])

print("scince\t\t\t\t\t",d[1])

print("arabic\t\t\t\t\t",d[2])

print("english\t\t\t\t\t",d[3])

print("art\t\t\t\t\t",d[4])

print("computer\t\t\t\t",d[6])

print("history\t\t\t\t\t",d[5])
