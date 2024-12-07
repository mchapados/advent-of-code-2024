f = open('input_files/day7.txt')
equations = []
for line in f:
    equations.append(line.strip())
f.close()

def test_equation(res, nums, pt2 = False) -> int:
    if len(nums) == 2:
        if nums[0]+nums[1] == res or nums[0]*nums[1] == res:
            return res
        elif pt2 and int(str(nums[0])+str(nums[1])) == res:
            return res
        return 0
    elif test_equation(res, [nums[0]+nums[1]]+nums[2:].copy(), pt2) == res:
        return res
    elif test_equation(res, [nums[0]*nums[1]]+nums[2:].copy(), pt2) == res:
        return res
    elif pt2:
        return test_equation(res, [int(str(nums[0])+str(nums[1]))]+nums[2:].copy(), pt2)
    return 0

result = 0
for eq in equations:
    res = int(eq[:eq.find(":")])
    nums = [int(i) for i in eq[eq.find(":")+1:].split()]
    # result += test_equation(res, nums)    # PART 1
    result += test_equation(res, nums, True)
print(result)