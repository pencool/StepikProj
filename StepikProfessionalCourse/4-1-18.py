import sys

nums = [int(i) for i in sys.stdin]
trfl = []
for i in range(len(nums) - 2):
    if nums[i+1] - nums[i] == nums[i + 2] - nums[i + 1] and nums[1] + nums[0] == nums[2]:
        trfl.append(True)
    elif nums[i+1] / nums[i] == nums[i + 2] / nums[i+1]:
        trfl.append(False)
    else:
        print('Не прогрессия')
        break
if len(trfl) == len(nums) - 2:
    if all(trfl):
        print('Арифметическая прогрессия')
    elif all(i == False for i in trfl):
        print('Геометрическая прогрессия')
