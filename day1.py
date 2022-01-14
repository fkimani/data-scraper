
# returns file object
f = open('data.txt', 'r')
#store the data from file in array
mydata = []

for line in f:
    mydata.append(int(line)) #convert to int to do number comparissons
    # print(int(line))
first = mydata[0] 
last = mydata[len(mydata)-1]
# print(type(first))
print(f'first item {first}') # check
print(f'last item {last}') # check
print(f'len data: {len(mydata)}') # check
print(len(mydata)==2000) # check
g = 0
l = 0
for d in mydata:
    if d == first:
        print(f'{d} skip first item {first}')
    if d > first:
        # print(f'{d} greater than {first}')
        g+=1
    else:
        # print(f'{d} lesser than {first}')  
        l+=1
    first = d

print(f'Greater than count: {g}')
# print(f' Lesser than count: {l}')
# print(g+l)
f.close()