def permutations(nums):
    res = []
    nums.sort()
    def backtrack(current,used):
        if len(current) == len(nums):
            res.append(current[:])
            return
        for i in range(len(nums)):

            if i in used:
                continue
            if i>0 and nums[i]==nums[i-1] and (i-1) in used:
                continue
            used.add(i)
            current.append(nums[i])
            backtrack(current, used)
            current.pop()
            used.remove(i)

    backtrack([],set())
    return res

print(permutations([1,1,2,3]))


