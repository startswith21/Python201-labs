# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 100000)
generator = (x for x in nums if x % 1111 == 0)
for x in generator:
    print(x)

