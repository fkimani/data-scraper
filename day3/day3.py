"""
Use the binary numbers in your diagnostic report to 
calculate the gamma rate and epsilon rate, then multiply 
them together. What is the power consumption of the submarine? 
(Be sure to represent your answer in decimal, not binary.) 
"""

# vars
# gamma_rate = 0
# epsilon_rate = 0

# file
myfile = "day3/data-sample.txt"

# returns file object
f = open(myfile, 'r')
mydata = []
gamma_rate = 0
epsilon_rate = 0

for line in f:
    mydata.append(line)   
    # for l in line:
    #     if(l=='0'):
    #         print("\t ",l)
    #         epsilon_rate += 1
    #     if(l=='1'):
    #         print("\t ",l)
    #         gamma_rate += 1
    # ll -= 1
    # i += 1
    # print("------")
for data in mydata:
    for d in data:
        print(d)

    # # print(f'gamma Rate={gamma_rate}; epsilon Rate={epsilon_rate} ')
    # if(gamma_rate>epsilon_rate):
    #     print(f"\tgamma rate is {gamma_rate} (greater)")
    #     champ = 1
    # if(gamma_rate<epsilon_rate):
    #     print(f"\tepsilon rate is {epsilon_rate} (greater)")
    #     champ = 0
    # # if(gamma_rate==epsilon_rate): #may not happen
    # #     print(f"gamma and epsilon rate equal({gamma_rate==epsilon_rate})")
    # print(f"champ: {champ}")
    # print("---") 