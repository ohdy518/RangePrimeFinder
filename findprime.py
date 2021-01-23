rng = input("Enter a range ([min_num] ~ [max_num]): ").split()  
minnum = int(rng[0])
maxnum = int(rng[2]) + 1
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

        for i in range(2,minnum):

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