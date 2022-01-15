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
# myfile = "sub-position.txt"
myfile = "sub-position-sample.txt"
fwd = 0
up = []
down = []

# returns file object
f = open(myfile, 'r')

mydata = []
# mydata = [
# "forward 9",
# "forward 7",
# ]

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
    mydata.append(line) #convert to int to do number comparissons
    
    # print(mydata)
    """ for l in line:
        if l.isdigit():
            print(f"{l} is digit.") """
        
    digit = get_digits(line)
    if 'forward' in line:
        # print(type(get_digits(line)))
        # digit
        # digit = get_digits(line)
        digit = int(digit)
        # print(type(digit))
        fwd += digit
        # fwd.append(line)
        print(f' {line}. add {digit}') 
    if 'up' in line:
        up.append(line) 
        print(f'{line} means subtract {digit}')
    if 'down' in line:
        down.append(line) 
        print(f'{line} means add {digit} ')
 
# for data in mydata:
#     print(data)

#sum of all 3 categories
#deduct downs from up sum. multiply answer by forward.