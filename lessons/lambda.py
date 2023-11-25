from functools import reduce

squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(12))

sum = lambda a, b: a + b

print(sum(10, 8))


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

number = [2, 6, 8, 31, 52, 75, 23]
print(f"\n{number}\n")

pow2List = map(lambda num: num * num, number)
print(f"\n{list(pow2List)}")

evenNumbers = filter(lambda num: num % 2 == 0, number)
print(f"\n{list(evenNumbers)}")

nums = [1, 6, 2, 32, 51]

total_sum = reduce(lambda acc, curr: acc + curr, nums)

print(total_sum)

nameList = ["Dave", "Paul", "Rachel", "Mary", "Josh"]

count_char = reduce(lambda acc, curr: acc + len(curr), nameList, 0)

print(count_char)
