# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 100000)
generator = (x//1111 for x in nums)
for x in generator:
    print(x)
    