#  forward 1, down 2, or up 3
"""
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

# gameplan: Iterate through the data, for each line, add or sub the step taken

# file
myfile = "day2/sub-position.txt"
# myfile = "day2/sub-position-sample.txt"
# track computations
fwd = 0
up = 0
down = 0
mydata = []

# returns file object
f = open(myfile, 'r')

# get digit from the row text
#  https://stackoverflow.com/questions/12005558/python-find-digits-in-a-string/12005674
def get_digits(str1):
    c = ""
    for i in str1:
        if i.isdigit():
            c += i
    return c

# append data from file
for line in f:
    # mydata.append(line)
    digit = get_digits(line)
    digit = int(digit)
    if 'forward' in line:
        # print(f'{fwd} + {digit} = {fwd+digit}') 
        fwd += digit
    if 'up' in line:
        # print(f' UP   {up} + {digit} = {up+digit}') 
        up += digit
    if 'down' in line: 
        # print(f'    {down} + {digit} = {down+digit}') 
        down += digit
 
# for data in mydata:
#     print(data)

#sum of all 3 categories
#deduct downs from up sum. multiply answer by forward.
print(f'Up: {up} ; Down: {down} ; Fwd: {fwd}')
down=down-up
print(f'submarine horizontal position {down}* depth {fwd} = {down*fwd}')
f.close()