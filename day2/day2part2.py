"""
In addition to horizontal position and depth, you'll also 
need to track a third value, aim, which also starts at 0. 
The commands also mean something entirely different than you 
first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.

Using this new interpretation of the commands, calculate 
the horizontal position and depth you would have after 
following the planned course. What do you get if you 
multiply your final horizontal position by your final depth?

"""


# file
myfile = "sub-position.txt"
# myfile = "sub-position-sample.txt"
# myfile = "test.txt"
# track positions
horizontal_position = 0
depth = 0
aim = 0
# mydata = []


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
#         forward X does two things:
#         It increases your horizontal position by X units.
#         It increases your depth by your aim multiplied by X.

        horizontal_position += digit
        
        if(aim==0):
            # print(f'FORWARD {digit} adds {digit} to your horizontal position, a total of {horizontal_position}. Because your aim is {aim}, your depth does not change. ' )
            continue
        if(aim>0):
            aimx = aim*digit
            depth += aimx
            # print(f'FORWARD {digit} adds {digit} to your horizontal position, a total of {horizontal_position}. Because your aim is {aim}, your depth ({depth}) increases by {digit}*{aim}={digit*aim} or {aimx} to a total of {depth}.' )

    if 'up' in line:
        aim -= digit #up X decreases your aim by X units.
        # print(f'UP {digit} decreases your aim by {digit}, resulting in a value of {aim}.')
    if 'down' in line:
        aim += digit#down X increases your aim by X units.
        # print(f'DOWN {digit} adds {digit} to your aim, resulting in a value of {aim}.')

# print(f'After following these new instructions, you would have a horizontal position of {horizontal_position} and a depth of {depth}. (Multiplying these produces {horizontal_position*depth}.)')

print(f'Horizontal position = {horizontal_position}; Depth = {depth}. NEW POSITION ({horizontal_position} * {depth}) = {horizontal_position*depth}')
f.close()
