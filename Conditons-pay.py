def computepay(h,r):
    if(h<=40):
        pay = h*r
    elif(h>40):
        pay = (h*r)+((h-40)*(r/2))
    return pay


hrs=float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
p=computepay(hrs,rate)
print(p)