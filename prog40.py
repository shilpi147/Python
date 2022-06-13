'''print((lambda x:(x % 2 and 'odd' or 'even'))(12))
x=2
y=3
print(x | y)
print(bin(3))'''

nums = [1, 2, 3, 4, 5, 6, 7, 8]

nums = list(reduce(lambda x, y : (x, y), nums))

Print(nums)      
