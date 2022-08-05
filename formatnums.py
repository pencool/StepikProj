with open('justnums.txt') as f, open('numsforcopy.txt', 'w') as nums:
    print(*f.read().split(), file=nums)
with open('numsforcopy.txt') as nums:
    print(len(nums.read().split()))