def computepay(h,r):
    if (h <= 40):
        return (h*r)
    else:
        return ((40*r) + (1.5*(h-40)*r))

hrs = input("Enter Hours:")
hrs = float(hrs)
rateph = input("Enter Rate per hour:")
rateph = float(rateph)
p = computepay(hrs,rateph)
print("Pay",p)
