x = int( input("Digite um numero e aperte <ENTER>"))
y = int( input("Digite um numero e aperte <ENTER>"))
z = int( input("Digite um numero e aperte <ENTER>"))
if x < y:
    if x < z:
        print (x)
        if y < z:
            print (y)
            print (z)
        else:
            print (z)
            print (y)
    else:
        print (z)
        print (x)
        print (y)
else: 
    if y < z:
        print (y)
        if x < z:
            print (x)
            print (z)
        else:
            print (z)
            print (x)
        
    else:
        print (z)
        print (y)
        print (x)
    
