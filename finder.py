import heapq
from collections import deque
# # from dave beaz cookbook 1.4: Finding largest or smallest N items
# make a list of largest or smallest N items in a collection.

portfolio = [
    {"name": "IBM", "shares":100, "price":91.1},
    {"name": "AAPL", "shares":50, "price":543.22},
    {"name": "FB", "shares":200, "price":21.09},
    {"name": "HPQ", "shares":35, "price":31.75},
    {"name": "YHOO", "shares":45, "price":16.35},
    {"name": "ACME", "shares":75, "price":115.65}
]

nums = [1,4,3,7,90,4,-3]
q = deque(maxlen=10)
q.append(3)
q.append(100)
print(q)
q.appendleft(200) #appends to start of queue
print(q)
r = q.pop() #removes last item, stores it in a var r
print(q, r)


# print(heapq.nsmallest(2, nums))
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(3, portfolio, key=lambda s:s['price']))
# print(heapq.nlargest(3, portfolio, key=lambda s:s['price']))