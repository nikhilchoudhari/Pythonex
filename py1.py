hrs = input("Enter Hours:")
rph = input("Enter rate per hours:")
h = float(hrs)
hh = int(hrs)
r = float(rph)
#rr = float(rph)*1.5
if h <= 40:
    print ("The total pay is:", h*r)
else:
    #hh = int(hrs)
    rr = 0
    for i in range (40,hh):
        rr += 1.5*r
    print ((40*r)+rr)