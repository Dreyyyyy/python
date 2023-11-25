# Dictionaries
band = {"vocals": "Plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(type(band2))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# list of key/values as tuples
print(band.items())

# verify if a key exists
print("guitar" in band)
print("bass" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionary
band2 = band.copy()
band2["drums"] = "Dave"

print(band)
print(band2)

# or use dict constructior function
band2 = dict(band)
band2["drums"] = "Dave"

print(band)
print(band2)

# Nested dictionaries
member1 = {"name": "Plant", "insturment": "vocals"}
member2 = {"name": "Page", "insturment": "guitar"}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member2"]["name"])

# Sets
nums = {1, 2, 3, 4}
nums2 = set((5, 6, 7, 8))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

# no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, and False is a dupe of 0
nums = {True, 1, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# add a element to a set
nums.add(8)
print(nums)

# add elements from a set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# merge two sets too create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
