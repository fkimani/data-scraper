
# returns file object
f = open('data.txt', 'r')
#store the data from file in array
mydata = []

# append data from file
for line in f:
    mydata.append(int(line)) #convert to int to do number comparissons
    # print(int(line))


# initialize position of A
i = 0
sums = [] # track the sums
sum_increase = 0 # increase count
sum_decrease = 0
prev_sum = 0
mysum = 0
for d in mydata:    
    # loop thru 3 measures at a time, put each sum in sums[]
    while(i<len(mydata)-2):
        prev_sum=mysum # track previous sum
        a = mydata[i]
        b = mydata[i+1]
        c = mydata[i+2]
        mysum = a+b+c # track current sum
        sums.append(mysum) # add the sum to sums list
     
        # print(f'previous sum is: {prev_sum}')

        # compare the new row in sums[] vs previous. Increase or decrease?
        if(prev_sum == sums[0] or prev_sum == 0):
            print(f'{a}+{b}+{c} = {mysum} (N/A - no previous sum)')
        if(mysum>prev_sum):
            sum_increase +=1
            # print(f'{a}+{b}+{c} = {mysum} (Increased)' )
        if(mysum<prev_sum):
            # print(f'{a}+{b}+{c} = {mysum}  (Decreased) ')
            sum_decrease +=1
        i+=1
        
# print(f'sums list: {sums}')
# print(f'increased {sum_increase} times. Decreaseed {sum_decrease} times.')
print(f'len sums: {len(sums)}')

total = 0
for s in sums:   
    ps = s
    if(s==ps):
        # print("skip")
        continue
    if(s>ps):
        print("increased")
        total+=1
    if(s<ps):
        print("decreased")
        
print(f"TOTAL: {total} ")
# f.close()