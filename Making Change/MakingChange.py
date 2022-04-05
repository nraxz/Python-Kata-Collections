changes = [50,25,10,5,1]

def making_change(n):
    for x in changes:
        if(n >= x):
            print(x,'s: ', int(n / x))
            n = n % x
        else:
            print(x,'s: ', int(n / x))
making_change(0)