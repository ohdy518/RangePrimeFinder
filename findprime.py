ipt = True
minnum = 0
maxnum = 0
chminnum = 0
while ipt:
    try:
        minnum = int(input("Range minimum value: "))
        chminnum = minnum
        maxnum = int(input("Range maximum value: ")) + 1
    except:
        print("Please enter a number.")
    else:
        ipt = False
        break
prime = [
    ""
]
notprime = [
    ""
]
del notprime[0]
del prime[0]
while minnum != maxnum:
    
    if minnum > 1 :  

        for i in range(2, minnum):

            if (minnum % i) == 0:
                notprime.append(minnum)
                break
        else:  
                prime.append(minnum)
    else: 
        notprime.append(minnum)
    minnum += 1
print(f"Prime numbers: {prime}")
print(f"Prime number count: {len(prime)}")
print("-" * 10)
print(f"Not prime: {notprime}")
print(f"Not prime count: {len(notprime)}")
minnum = chminnum
searching = True
nnotprime = notprime
a = True
while a:
    try:
        del nnotprime[nnotprime.index(0)]
    except:
        a = False
        break
    else:
        a = False
        break
a = True
while a:
    try:
        del nnotprime[nnotprime.index(1)]
    except:
        a = False
        break
    else:
        a = False
        break
for i in nnotprime:
    if i < 0:
        del nnotprime[nnotprime.index(i)]
while searching:

    search = input("Search (or .quit to quit): ")
    try:
        try:
            int(search)
        except:
            if search == ".quit":
                searching = False
                break
            else:
                print("Invalid search key.")
        else:
            try:
                intsea = int(search)
                index = prime.index(intsea)
                print(f"{search} is {str(index + 1)}(th) prime.")
            except:
                intsea = int(search)
                notprime.index(intsea)
                print(f"{search} is not a prime.")
                for i in prime:
                    if intsea % i == 0:
                        print(f"{intsea} divides into {i}. ({intsea} / {i} = {intsea / i})")
                for i in nnotprime:
                    if intsea % i == 0:
                        if i == intsea:
                            pass
                        else:
                            print(f"{intsea} divides into {i}. ({intsea} / {i} = {intsea / i})")
                 
    except:
        print("Error: Number out of range")
                    
