users = ["Dave", "John", "Sarah"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Sarah"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())

del users[0]
print(users)

# del data
# print(data)

data.clear()
print(data)

users.sort()
print(users)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1, 7, 25, 6, 18]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

mycopy = nums.copy()
mycopy.sort()
print(mycopy)

print(type(mycopy))

# list with constructor
clist = list([3, 2, 1])
print(clist)

# Tuples
mytuple = tuple((1, 2, 3))
anothertuple = (4, 5, 6)

print(mytuple)
print(anothertuple)

print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *rest, two) = newtuple
print(one)
print(rest)
print(two)

print(anothertuple.count(2))
