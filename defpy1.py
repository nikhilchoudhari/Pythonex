def computepay(h,r):
    if h <= 40:
        p = h*r
        return (p)
    else:
        rr = 0
        hh = int(h)
        for i in range(40,hh):
            rr += 1.5*r
        p = ((40*r)+rr)
        return (p)
    #return 42.37

hrs = input("Enter Hours:")
rph = input("Enter rate per hours:")
hrss = float(hrs)
rphh = float(rph)
pp = computepay(hrss,rphh)
print(pp)