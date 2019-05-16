x = int ( input ("digite um numero e tecle <enter>" ))
y = int ( input ("digite um numero e tecle <enter>" ))
if x < y:
    while x < y + 1:
        print (x)
        x = x + 1
else:
    while x > y - 1:
        print (x)
        x = x - 1
