""" mydata = [
    187,
    195,
    199,
    218,
    221,
    222,
    219,
    225,
    226,
    227
] """

# returns file object
f = open('data.txt', 'r')

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

mysum = mydata[0]+mydata[1]+mydata[2]
prev_sum = mysum
# print(len(mydata))
j=len(mydata)

for d in mydata:    
    
    # loop thru 3 measures at a time, put each sum in sums[]
    while(j>2):
        a = mydata[i]
        b = mydata[i+1]
        c = mydata[i+2]
        mysum = a+b+c # track current sum
        sums.append(mysum) # add the sum to sums list
     

        # compare the new row in sums[] vs previous. Increase or decrease?
        if(len(sums)==1 ):
            print(f'{a}+{b}+{c} = {mysum} (N/A - no previous sum)')
        if(mysum>prev_sum):
            sum_increase +=1
            print(f'{a}+{b}+{c} = {mysum} (Increased from {prev_sum}. {mysum>prev_sum})' )
        if(mysum<prev_sum):
            print(f'{a}+{b}+{c} = {mysum}  (Decreased from {prev_sum}.  {mysum>prev_sum}) ')
            sum_decrease +=1
        i+=1
        j-=1
        prev_sum = mysum
        
print(f'sums list: {sums}')
print(f'increased {sum_increase} times. Decreaseed {sum_decrease} times.')
print(f'len sums: {len(sums)}')


